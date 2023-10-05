from arango import ArangoClient
import json 
from json import loads
import re

# Connect to Arango
user = "root"
pw = "jalapeno"
dbname = "jalapeno"

client = ArangoClient(hosts='http://10.200.99.202:30852')
db = client.db(dbname, username=user, password=pw)

# Create Arango collection if it doesn't already exist
print("connecting to arango")
if db.has_collection('test'):
    test_coll = db.collection('test')
else:
    test_coll = db.create_collection('test')

f = open("test.json")
# convert json string to dict
ld = json.load(f)

id_list = []
res = [ sub['_key'] for sub in ld ]
for i in res:
    id = "test/" + i
    id_list.append(id)
    #print(id_list)

# initializing _id Dict Key 
K = "_id"
 
# using enumerate() to iterate for index and values
for idx, ele in enumerate(ld):
    ele[K] = id_list[idx]
    #print(ld)

for i in ld:

    # upload document to DB
    if db.has_document(id):
        metadata = test_coll.update(i)
        print("document exists, updating timestamp: ", i['_key'])
    else:
        metadata = test_coll.insert(i)

        print("document added: ", i['_key'])