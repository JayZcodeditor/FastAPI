from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi

uri = "mongodb+srv://Thammakit:qweasdzxc@cluster0.88ruy.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(
    uri,
    server_api=ServerApi('1'),
    tls=True,
    tlsCAFile=certifi.where()
)

db = client.todo_db
# ในกรณีที่ต้องการใช้งานหลาย collection  
collection_todo = db["todo_data"]
collection_another = db["another_collection"]

print(collection_todo.find_one())
print(collection_another.find_one())
