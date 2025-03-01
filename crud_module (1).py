from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self):
        # Connection Variables
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 33591
        DB = 'AAC'  # Correct database name
        COL = 'aac_animals'  # Fixed collection name
        
        # Initialize Connection
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}/{DB}?authSource=admin')
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        """Inserts a document into the MongoDB collection."""
        if data:
            result = self.collection.insert_one(data)
            return result.acknowledged
        else:
            raise ValueError("Data cannot be empty")

    def read(self, query=None):
        """Queries for documents in the MongoDB collection. Returns all if no query is provided."""
        if not query:
            query = {}  # Allow empty query to return all documents
        results = list(self.collection.find(query))
        return results

    def update(self, filter_key, filter_value, update_key, update_value):
        """Updates a document in the collection."""
        if filter_key and filter_value and update_key and update_value:
            result = self.collection.update_one({filter_key: filter_value}, {"$set": {update_key: update_value}})
            return result.modified_count  # Number of updated documents
        else:
            raise ValueError("Update parameters cannot be empty")

    def delete(self, filter_key, filter_value):
        """Deletes a document from the collection."""
        if filter_key and filter_value:
            result = self.collection.delete_one({filter_key: filter_value})
            return result.deleted_count  # Number of deleted documents
        else:
            raise ValueError("Delete parameters cannot be empty")

# ✅ **Test Script If Run Directly**
if __name__ == "__main__":
    shelter = AnimalShelter()
    
    # ✅ Read All Documents (New Default Behavior)
    print("Fetching all records...")
    results = shelter.read()
    print(f"Total records found: {len(results)}")
    
    # ✅ Create
    data = {
        "animal_id": "A733653",
        "animal_type": "Cat",
        "breed": "Siamese Mix",
        "color": "Seal Point",
        "date_of_birth": "2016-01-25",
        "outcome_type": "Adoption"
    }
    insert_success = shelter.create(data)
    print(f"Insert Successful: {insert_success}")

    # ✅ Read Specific Query
    query = {"breed": "Siamese Mix"}
    results = shelter.read(query)
    print(f"Query Results: {results}")

    # ✅ Update
    update_result = shelter.update("animal_id", "A733653", "color", "Chocolate Point")
    print(f"Documents updated: {update_result}")

    # ✅ Delete
    delete_result = shelter.delete("animal_id", "A733653")
    print(f"Documents deleted: {delete_result}")
