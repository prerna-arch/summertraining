"""
MONGODB CRUD operations



"""
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://prernasablok:omsairam3008@cluster0.xbwze2r.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# get reference to the database
db= client['summertraining']

#get collection names for database
collections=db.list_collection_names()

for collection in collections:
    print(collection)
# get data from documents
documents= db['python'].find()
print(documents)

for document in documents:
    print(document)