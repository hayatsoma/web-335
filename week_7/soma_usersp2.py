"""
Title: soma_usersp2.py
Author: Hayat Soma>
Date: 9/29/2024
Description: Hands-On 5.2 Python with MongoDB Part II - Perform CRUD operations
"""

# Import the MongoClient
from pymongo import MongoClient
import datetime

# Build a connection string to connect to your MongoDB database
client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DB?retryWrites=true&w=majority")

# Configure a variable to access the web335DB
db = client['web335DB']

# Step 3: Create a new user document
new_user = {
    "firstName": "Ludwig",
    "lastName": "Beethoven",
    "employeeId": "1040",
    "email": "lbeethoven@music.com",
    "dateCreated": datetime.datetime.utcnow()
}

# Insert the document into the users collection
new_user_id = db.users.insert_one(new_user).inserted_id

# Step 4: Prove the document was created
print("Document created with ID:", new_user_id)
print("Created Document:", db.users.find_one({"employeeId": "1040"}))

# Step 5: Update the email address of the document created in step 3
db.users.update_one(
    {"employeeId": "1040"},
    {
        "$set": {
            "email": "ludwig.beethoven@music.com"
        }
    }
)

# Step 6: Prove the document was updated
print("Updated Document:", db.users.find_one({"employeeId": "1040"}))

# Step 7: Delete the document that was created in step 3
delete_result = db.users.delete_one({"employeeId": "1040"})

# Step 8: Prove the document was deleted
print("Delete operation acknowledged:", delete_result.acknowledged)
print("Deleted Document Search Result:", db.users.find_one({"employeeId": "1040"}))
