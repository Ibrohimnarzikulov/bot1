from dotenv import load_dotenv
import os
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

BOT_TOKEN=os.getenv("8745550471:AAH9F_0RV6Dmwe8ncU11zTSqSjLkNqurI_Y")
ADMINS=os.getenv("ADMINS").split(",")

