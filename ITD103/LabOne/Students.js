const mongoose = require('mongoose')

const StudentSchema = new mongoose.Schema({
    name: String,
    idNum: String,
    course: String,
    college: String,
    age: String 
    //Dont follow, create your own version
    //{name, email, age}
})

const StudentModel = mongoose.model("students", StudentSchema)
module.exports = StudentModel