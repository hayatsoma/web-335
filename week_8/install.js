use WhatABook;

// Drop the collections if they exist
db.books.drop();
db.authors.drop();
db.genres.drop();
db.wishlist.drop();
db.customers.drop();

// Create collections
db.createCollection("books");
db.createCollection("authors");
db.createCollection("genres");
db.createCollection("wishlist");
db.createCollection("customers");

// Insert sample data into collections
db.books.insertMany([
  { bookId: 1, title: "The Catcher in the Rye", authorId: 1, genreId: 1 },
  { bookId: 2, title: "To Kill a Mockingbird", authorId: 2, genreId: 2 },
  { bookId: 3, title: "1984", authorId: 3, genreId: 1 }
]);

db.authors.insertMany([
  { authorId: 1, name: "J.D. Salinger" },
  { authorId: 2, name: "Harper Lee" },
  { authorId: 3, name: "George Orwell" }
]);

db.genres.insertMany([
  { genreId: 1, name: "Classic" },
  { genreId: 2, name: "Drama" }
]);

db.customers.insertOne({ customerId: 1, name: "Emma Carter", wishlist: [] });

print("Database setup complete.");
