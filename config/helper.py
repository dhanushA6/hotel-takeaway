from dotenv import load_dotenv
import os

# Load from env config
load_dotenv()

# Path Constants
CONFIG_PATH = os.path.dirname(os.path.realpath(__file__))
APP_PATH = os.path.abspath(os.path.join(CONFIG_PATH, '..'))

def getAppConfig():
    config = {
        "NAME": os.getenv("APP_NAME"),
        "PORT": os.getenv("APP_PORT"),
        "SECRET_KEY": os.getenv("APP_SECRET_KEY")
    }
    return config

def getMailConfig():
    config = {
        "SERVER": os.getenv("MAIL_SERVER"),
        "PORT": os.getenv("MAIL_PORT"),
        "USER": os.getenv("MAIL_USERNAME"),
        "PASS": os.getenv("MAIL_PASSWORD")
    }
    return config

def rename_config_file():
    old_name = "example.env"
    new_name = ".env"
    old_file_path = os.path.join(CONFIG_PATH, old_name)
    new_file_path = os.path.join(CONFIG_PATH, new_name)

    try:
        os.rename(old_file_path, new_file_path)
    except FileNotFoundError:
        return f"The example env file was not found."
    except FileExistsError:
        return f"The env file already exists."
    
    return True