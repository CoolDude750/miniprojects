import pymongo

client = pymongo.MongoClient("mongodb+srv://rakeshuikey2407:DrU2407@cluster0.hawmw.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name":"rakesh",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "uikey"
}
db1 = client['mongotest1']
coll = db1['test2']
coll.insert_one(d )

