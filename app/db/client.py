from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb+srv://Karina1014:Junio30k.2023@cluster0.zetck.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "UPC"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

