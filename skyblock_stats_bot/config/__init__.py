from dotenv import load_dotenv
import os

load_dotenv()

guild_id_string = os.getenv('GUILD_ID')
if not guild_id_string:
	raise ValueError('GUILD_ID environment variable not set')
GUILD_ID = int(guild_id_string)
TOKEN = os.getenv('TOKEN')
if not TOKEN:
	raise ValueError('TOKEN environment variable not set')
