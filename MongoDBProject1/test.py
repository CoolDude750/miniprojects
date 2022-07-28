import pymongo

client = pymongo.MongoClient("mongodb+srv://rakeshuikey2407:DrU2407@cluster0.hawmw.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['my_info1']
collection = database["my_collection1"]

list_of_records1 = [
    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'},

    {'companyName': 'iNeuron1',
     'product': 'Affordable AI',
     'courseOffered': 'Deep Learning for NLP and Computer vision'},

    {'companyName': 'iNeuron',
     'product': 'Master Program',
     'courseOffered': 'Data Science Masters Program',
     "test": "ffsdfsffsf",
     "complex": [{"name": "sudhanshu", "list": [554, 545, 454, 54, 5, 4]}, {"email_id": "sudhanshu@dffsf"},
                 {"phone_no": 345345345353}, [4, 54, 534, 5, 45, 5, 45, 4]]

     }]

rec = collection.insert_many(list_of_records1)

data1 = collection.find({'companyName': 'iNeuron1'})
for i in data1:
    print(i)