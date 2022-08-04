import os
from os import environ
from os import getenv

class Config(object):
	API_ID = "8657438"
	API_HASH = "ea8263e0393b6c06d4cf83ca6c5014ad"
	BOT_TOKEN = "5475622635:AAFZZX8UWW5eEH0eSSYqn2FN0Hy-LBZpniU"
	BOT_USERNAME = "gbimsath_bot" 
	BOT_OWNER = "1404096450"
	SESSION_STRING = environ.get("SESSION_STRING", None)
	OWNER = "1404096450"
	MONGODB_URI = "mongodb+srv://gbimsathx:gbimsathx@gbimsathx.zzn83.mongodb.net/?retryWrites=true&w=majority"
	LOG_CHANNEL = "-1001590908979"
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY"))
	ARQ_API_KEY = "XLGGZR-OPTXKU-WRIYVD-ULFTGZ-ARQ"

