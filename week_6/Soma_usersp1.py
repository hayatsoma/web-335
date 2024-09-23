"""
Title: Soma_usersp1.py
Author: Hayat Soma
Date: 22 September 2024
Description: Python program to interact with MongoDB and perform operations on the users collection.
"""

# Import the MongoClient from pymongo
from pymongo import MongoClient

# Establish the connection to MongoDB
client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DB?retryWrites=true&w=majority")

# Connect to the web335DB database
db = client['web335DB']

# 1. Display all documents in the users collection
print("Displaying all users:")
for user in db.users.find({}):
    print(user)

# 2. Find a document where employeeId is 1011
print("\nDisplaying user with employeeId 1011:")
user_by_employee_id = db.users.find_one({"employeeId": "1011"})
print(user_by_employee_id)

# 3. Find a document where lastName is Mozart
print("\nDisplaying user with lastName 'Mozart':")
user_by_last_name = db.users.find_one({"lastName": "Mozart"})
print(user_by_last_name)
