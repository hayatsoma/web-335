/**
 * Soma - Hands-On 6.1
 * Queries for MongoDB operations on the students and houses collections.
 * 
 * Author: Hayat Soma
 * Date: 9/21/2024
 */

// a. Display all students
db.students.find()

// b. Add a new student (Harry Potter)
db.students.insertOne({
    firstName: "Harry",
    lastName: "Potter",
    studentId: "s1019",
    houseId: "h1007"
})

// Verify Harry Potter was added
db.students.find({ firstName: "Harry", lastName: "Potter" })

// c. Update Harry Potter's houseId to Slytherin
db.students.updateOne(
    { studentId: "s1019" }, 
    { $set: { houseId: "h1010" } }
)

// Verify the update
db.students.find({ studentId: "s1019" })

// d. Delete Harry Potter from the students collection
db.students.deleteOne({ studentId: "s1019" })

// Verify the deletion
db.students.find({ studentId: "s1019" })

// e. Display all students by house (grouped by mascot)
db.students.aggregate([
    { $lookup: {
        from: "houses",
        localField: "houseId",
        foreignField: "houseId",
        as: "houseDetails"
    }},
    { $unwind: "$houseDetails" },
    { $group: { _id: "$houseDetails.mascot", students: { $push: "$$ROOT" } } }
])

// f. Display all students in Gryffindor house (houseId h1007)
db.students.find({ houseId: "h1007" })

// g. Display all students in the house with an Eagle mascot
db.students.aggregate([
    { $lookup: {
        from: "houses",
        localField: "houseId",
        foreignField: "houseId",
        as: "houseDetails"
    }},
    { $match: { "houseDetails.mascot": "Eagle" } }
])
