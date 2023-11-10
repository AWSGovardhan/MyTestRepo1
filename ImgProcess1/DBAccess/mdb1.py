import pymongo as pm
client = pm.MongoClient("mongodb://localhost:27017/")  # You can specify the MongoDB connection URI
db = client["local"]
collection = db["persons"]
# Query documents from the collection
# result = collection.find({"key1": "value1"})

result = collection.find()
for document in result:
    # print(type(document.key(),":",document.value()))
    print(document)


# result = collection.find({'pname':1,'age':1})
# for document in result:
#     # print(type(document.key(),":",document.value()))
#     print(document)

client.close()