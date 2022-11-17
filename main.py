from fastapi import FastAPI, Header, HTTPException
from pymongo import MongoClient
import csv
import pprint
from bson.son import SON

app = FastAPI()

# Creating a MongoDB connection
@app.get("/connect_mongo", status_code=200, description="Connects to MongoDB!")
async def start_browser(
    username: str = Header(
        default=None,
        description="MongoDB username",
    ),
    password: str = Header(
        default=None, description="MongoDB password"
    ),
):
    URI = "mongodb://" + username + ":" + password + "@localhost:27017/"
    try:
        mc = MongoClient(URI)
        return "MongoDB connection successful"
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)


# Fetch Collection Data
@app.get("/fetch_data", status_code=200, description="Fetch the data available in the collection!")
async def start_browser(
    username: str = Header(
        default=None,
        description="MongoDB username",
    ),
    password: str = Header(
        default=None, description="MongoDB password",
    ),
    code_sequence: str = Header(
        default=216,
        description="MongoDB code sequence"
    )
):
    URI = "mongodb://" + username + ":" + password + "@localhost:27017/"
    dataset_location = "/Users/venkateshdharmapuri/Desktop/Zomato_Restaurants_Data/zomato.csv"
    try:
        mc = MongoClient(URI)
        print("MongoDB connection successful")
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)
    
    zomato_db = mc["zomato"]
    zomato_coll = zomato_db["zomcoll"]

    cursor = zomato_coll.find({ "Country Code": { "$eq": code_sequence } }).limit(10)
    for document in cursor: return document

# Insert Audit Records
@app.get("/fetch_data", status_code=200, description="Fetch the data available in the collection!")
async def start_browser(
    username: str = Header(
        default=None,
        description="MongoDB username",
    ),
    password: str = Header(
        default=None, description="MongoDB password",
    ),
    audit_by: str = Header(
        default="venkatesh",
        description="Auditor Name"
    ),
    audit_on: str = Header(
        default="None",
        description="When the audit was done"
    )
):
    URI = "mongodb://" + username + ":" + password + "@localhost:27017/"
    dataset_location = "/Users/venkateshdharmapuri/Desktop/Zomato_Restaurants_Data/zomato.csv"
    try:
        mc = MongoClient(URI)
        print("MongoDB connection successful")
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)
    
    zomato_db = mc["zomato"]
    zomato_coll = zomato_db["zomcoll"]

    mydict = { "purpose": "assignment audit", "auditor": audit_by, "audit date": audit_on }
    x = zomato_coll.insert_one(mydict)
    
    return x