'''import pykafka import KafkaClient
import datetime as dt
import pymongo
import sys
import re

def db_exists(client,db_name):
    dblist = client.list_database_names()
    if db_name in dblist:
        print("The database '{0}' exists.".format(db_name))
        return True
    else:
        print("The database '{0}' doesn't exists".format(db_name))
        return False

def col_exists(db,col_name):
    collist = db.list_collection_names()
    if col_name in collist:
        print("The collection '{0}' exists.".format(col_name))
        return True
    else:
        print("The collection '{0}' doesn't exists.".format(col_name))
        return False
        
    
print("Hello, World!")

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
try:
    myclient.admin.command('ping')
    print("Connection established")
except:
    sys.exit("Connection failed to be established")

mydb = myclient["SensorData"] 

db_exists(myclient,"SensorData")

mycol = mydb["data"] 

assert col_exists(mydb,"data"), "Database and/or collection failed to be created"

kafka_client = KafkaClient(hosts='localhost:9092')
kafka_topic = kafka_client.topics['climateInfo']
kafka_consumer = kafka_topic.get_simple_consumer() #no consumer_timeout_ms, waits forever if iterating

for msg in kafka_consumer:
    print(msg.value)
    payload = str(msg.value)
    datetime, remainder = payload.split("|")
    remainder = remainder[2:] #remainder = ["T:", TEMPERATURE, "U:", UMIDITY, SENSOR_NAME]
    remainder = remainder.split(" ")
    input_dict = {"_id": remainder[4] + "|" + datetime, "T": remainder[1], "U": remainder[3]}
    print(input_dict)
    print("-------------------------------------------------------------------------------")
    
    mycol.insert_one(mydict)'''