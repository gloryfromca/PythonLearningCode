import requests # web POST and GET requests.
from pymongo import MongoClient # the mongo driver / connector
from bson import ObjectId # to generate bson object for MongoDB
from multiprocessing import Pool # for the multithreading

def get_user(userid):
    params = {"userid": userid}
    rv = requests.get("https://exampleapi.com/getUser", params=params)
    json = rv.json()
    return json['content']

# It is advised to create a MongoClient once for each process and not share the same client for each process.
# This is because MongoClient also handles multiple connections from a process using connection pooling and isn't fork-safe.
def create_connect():
    return MongoClient(
       'mongodb://192.168.0.1:27017,192.168.0.2:27017/?replicaSet=rs0', maxPoolSize=20
    )

def consumer(index_line):
    client = create_connect()
    users = client.database.users

    user = get_user(index_line["_id"])
    if user:
        users.insert(user)

def main():

    # limit to 100,000 lines of data each loop
    limited = 100
    # skip number of lines for the loop (getting updated)
    skipped = 0
    client = create_connect()
    index = client.database.index
    # initialize the process Pool once outside of the loop and map processes within the loop.
    # multiprocessing.Pool.map waits until child processes complete and return so joining the pool will result in an exception.
    # You may consider using multiprocessing.Pool.async_map if you'll like to run child processes asynchronously.
    pool = Pool(10)

    count = index.count()

    while True:

        if skipped > count:
            break

        cursor = index.find({}).skip(skipped).limit(limited)

        pool.map(consumer, cursor)

        skipped = skipped + limited
        print("[-] Skipping {}".format(skipped))

if __name__ == '__main__':
    main()