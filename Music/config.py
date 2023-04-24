##Config

from os import getenv

from dotenv import load_dotenv

load_dotenv()
SESSION_NAME = getenv('SESSION_NAME', 'AgAGFRW8AN9biZhAIB_X7rubbTCwNtc48oa-geXlaVsQbV9M1emAEV_iGPw_W-lNP1HGbOuQgF9NAUIxlp8-6rgN16-7Upuhst2wCxewyx0VP7Cxb5k_9EXap6_xeU2v4So9RZMt95XYxhGc4hWO_ikd9P46iHLMjXW8GjQAnGvY-bIrM6XqIXF1yeC3vixEa8knOHGkedZU3FYyLhEILy8TV6eH5jOGvsyw5o7xFElb2zZId_vlYO--B3xSWIMUR6zyH8wozehe9tIn0jZptYjY1rqWOMoYS9wtqvBThVazL60nrgL-KdikJC9beDJLLR0C-wzuAtARPCZ-JK6oG-gVAAAAAUM3evYA')
BOT_TOKEN = getenv('BOT_TOKEN', '5204315005:AAF98O-HHNpo2qnyzQLV4wbw8fveiPZq2gY')
API_ID = int(getenv('API_ID', '8934899'))
API_HASH = getenv('API_HASH','bf3e98d2c351e4ad06946b4897374a1e')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '54000'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ . , : ; !').split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '1854384004').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001847569598'))
ASS_ID = int(getenv("ASS_ID", '5422676726'))
OWNER_ID = list(map(int, getenv('OWNER_ID', '1854384004').split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "xl444")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "xl444")
GROUP = getenv("GROUP", "GodfatherSupport")
CHANNEL = getenv("CHANNEL", "The_Godfather_Network")
