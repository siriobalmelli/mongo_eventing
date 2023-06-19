##
# common file for database connection
# import 'db' directly
##
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://cluster0.jf8lhh3.mongodb.net",
    authMechanism="MONGODB-X509",
    authSource="$external",
    tls=True,
    tlsCertificateKeyFile="./X509-cert-6977471360154941700.pem",
)

db = client["Cluster0"]
