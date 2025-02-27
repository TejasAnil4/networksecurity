from pymongo.mongo_client import MongoClient

# Replace with your actual username, password, and cluster details
uri = "mongodb+srv://tejasanil2021:admin123@cluster0.vahet.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = MongoClient(uri)
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("An error occurred:", e)