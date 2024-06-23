# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "25425840"))
    API_HASH = getenv("API_HASH", "e6ea2eca4aa38e965511f323e5ffa578")
    BOT_TOKEN = getenv("BOT_TOKEN", "7371906343:AAEGJvta0CZ0CFqY5Ye3pP9Z2W_Nh62o8eI")
    FSUB = getenv("FSUB", "Primemoviebd")
    CHID = int(getenv("CHID", "-1002043502363"))
    SUDO = list(map(int, getenv("SUDO", "5926160191").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sushankm16:4i1WAfPYKWyqPIDD@cluster0.sngp9pz.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
