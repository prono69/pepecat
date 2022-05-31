FROM sandy1709/catuserbot:slim-buster

#clonning repo 
RUN git clone https://github.com/sandy1709/catuserbot.git /root/userbot
#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","userbot"]
© 2022 GitHub, Inc.
Terms
