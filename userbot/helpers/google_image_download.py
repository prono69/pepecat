import os
import random
import time

import requests
from googleapiclient.discovery import build


def create_directories(main_directory, dir_name):
    # make a search keyword  directory
    try:
        if not os.path.exists(main_directory):
            os.makedirs(main_directory)
            time.sleep(0.15)
        path = dir_name
        sub_directory = os.path.join(main_directory, path)
        if not os.path.exists(sub_directory):
            os.makedirs(sub_directory)

        return sub_directory
    except OSError as e:
        if e.errno != 17:
            raise
    return


def search_and_download_images(query, api_key, cse_id, num_images=3):
    service = build("customsearch", "v1", developerKey=api_key)

    try:
        res = service.cse().list(q=query, cx=cse_id, searchType="image", num=num_images).execute()
    except Exception as e:
        print(f"An error occurred while searching: {e}")
        return

    if "items" not in res:
        print("No image results found.")
        return

    subDir = f"{query.replace(" ","_")}_{random.randint(1000,9999)}"

    # Create a directory for the images
    sub_directory = create_directories("downloads", subDir)

    errors = []

    for i, item in enumerate(res["items"]):
        try:
            # Get the image URL
            image_url = item["link"]

            # Download the image
            response = requests.get(image_url)

            # Check if the request was successful
            if response.status_code == 200:
                # Get the file extension
                file_extension = os.path.splitext(image_url)[1]
                if file_extension == "":
                    file_extension = ".jpg"  # Default to .jpg if no extension found

                # Save the image
                with open(f"{sub_directory}/image_{i+1}{file_extension}", "wb") as file:
                    file.write(response.content)
                print(f"Downloaded: image_{i+1}{file_extension}")
            else:
                print(f"Failed to download image {i+1}")

        except Exception as e:
            errors.append(f"An error occurred while downloading image {i+1}: {e}")

    return {
        "download_path": sub_directory,
        "errors": errors,
    }
