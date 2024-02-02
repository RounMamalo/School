const mongoose = require('mongoose')

const UserSchema = new mongoose.Schema({
    name: String,
    course: String,
    college: String,
    idNum: Number,
    age: Number
})

const UserModel = mongoose.model("students", UserSchema)

module.exports = UserModel;