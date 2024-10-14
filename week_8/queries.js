// Query 1: Display a list of books
print("List of all books:");
db.books.find().forEach(printjson);

// Query 2: Display a list of books by genre
print("Books by genre:");
db.books.aggregate([
  { $lookup: { from: "genres", localField: "genreId", foreignField: "genreId", as: "genre" } },
  { $unwind: "$genre" },
  { $project: { title: 1, "genre.name": 1 } }
]).forEach(printjson);

// Query 3: Display a list of books by author
print("Books by author:");
db.books.aggregate([
  { $lookup: { from: "authors", localField: "authorId", foreignField: "authorId", as: "author" } },
  { $unwind: "$author" },
  { $project: { title: 1, "author.name": 1 } }
]).forEach(printjson);

// Query 4: Display a book by bookId
print("Book with bookId 1:");
db.books.find({ bookId: 1 }).forEach(printjson);
