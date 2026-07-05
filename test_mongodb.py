from pymongo import MongoClient
uri = "mongodb+srv://Rishabh_user:<password>@cluster0.hmbqyxw.mongodb.net/?appName=Cluster0"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)