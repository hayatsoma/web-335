// Soma-HandsOn5.1.js

// 1. Adding a new user to the collection
db.users.insertOne({
    firstName: "Ludwig",
    lastName: "Beethoven",
    email: "beethoven@music.com",
    age: 57,
    profession: "Composer"
});

// 2. Updating Mozart's email address
db.users.updateOne(
    { lastName: "Mozart" },  // Finds Mozart
    { $set: { email: "mozart@me.com" } }  // Updates email
);

// 3. Displaying users with only first name, last name, and email
db.users.find(
    {},
    { _id: 0, firstName: 1, lastName: 1, email: 1 }  // Hides _id, shows name and email
);
