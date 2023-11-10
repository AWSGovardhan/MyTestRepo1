from pymongo import MongoClient


def mongo_conn():
    try :
        conn = MongoClient("localhost",port=27017)
        print("MongoDB Conn Established!")
        return conn.local #This is the database name
    
    except Exception as err:
        print(f"Trouble establishing the connection {err}")

def upload_file(file_loc, file_name, fs):
    



