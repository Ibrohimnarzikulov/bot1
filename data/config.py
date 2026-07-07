from dotenv import load_dotenv
import os
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

BOT_TOKEN=os.getenv("8691461678:AAHhwt7HU6E8dUssSg6QtwhY-V2pN2dwFR8")
ADMINS=os.getenv("ADMINS").split(",")

