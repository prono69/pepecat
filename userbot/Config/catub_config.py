# config values will be loaded from here

import os

if ENV := bool(os.environ.get("ENV", False)):
    from sample_config import Config  # noqa
elif os.path.exists("config.py"):
    from config import Development as Config  # noqa
