from pymongo import MongoClient
from werkzeug.security import generate_password_hash
import certifi
from Flask_Chat.user import User



ca = certifi.where()



client = MongoClient("mongodb+srv://aman:aman123@cluster0.o1i9q6n.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=ca)

chat_db = client.get_database("TestMongo")
users_collection = chat_db.get_collection("ChatDB")

def save_user(username, email, passowrd):
    passowrd_hash = generate_password_hash(passowrd)
    users_collection.insert_one({"_id":username,"email":email,"password":passowrd_hash})

#save_user("aman","aman@gmail.com","test")


def get_user(username):
    user_data = users_collection.find_one({'_id':username})
    return User(user_data['_id'], user_data['email'], user_data['password']) if user_data else None
    