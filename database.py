from pymongo import MongoClient

from utils.constants import DB_NAME


class Database:
    """Class for managing the Database"""

    db = None

    @staticmethod
    def init_database():
        """Connect to MongoDB"""

        # TODO: Configure with env once application is in test
        mongo_uri = "mongodb://localhost:27017"

        client = MongoClient(mongo_uri)

        Database.db = client[DB_NAME]

    @staticmethod
    def get_document(collection_name, key):
        """Find document with given key in a collection"""
        if Database.db is None:
            raise Exception("Database is not connected. Call init_database() first.")

        collection = Database.db[collection_name]

        document = collection.find_one({"key": key})
        if document:
            print(f"Document found: {document}")
        else:
            print(f"No document found with key '{key}'")
        return document

    @staticmethod
    def get_all_documents(collection_name):
        """Find all documents in a given collection"""
        if Database.db is None:
            raise Exception("Database is not connected. Call init_database() first.")

        collection = Database.db[collection_name]

        documents = collection.find()

        if documents:
            print("Documents found!")
        else:
            print(f"No documents found in collecition '{collection_name}'")
            return []

        return documents

    @staticmethod
    def insert_document(collection_name, document):
        """Insert a document into a specified collection"""
        if Database.db is None:
            raise Exception("Database is not connected. Call init_database() first.")

        collection = Database.db[collection_name]
        insert_result = collection.insert_one(document)
        print(f"Inserted document ID: {insert_result.inserted_id}")
        return insert_result

    @staticmethod
    def update_document(collection_name, document):
        """Update a document in a specific collection"""
        if Database.db is None:
            raise Exception("Database is not connected. Call init_database() first.")

        collection = Database.db[collection_name]
        update_result = collection.update_one(document)
        print(f"Inserted document ID: {update_result.inserted_id}")
        return update_result
