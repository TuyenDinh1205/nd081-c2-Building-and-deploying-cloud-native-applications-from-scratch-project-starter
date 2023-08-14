import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://tuyendinhdb:dxqTyOSjquDHaSURZvMrcAW1wyHtCIsWjCFGot5uAukxGhUFEF2kIS2lMlxGRLGymAdWBBvBXXI2ACDb3cbU1Q==@tuyendinhdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@tuyendinhdb@"  
        # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['tuyendinhdb']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)