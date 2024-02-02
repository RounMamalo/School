const express = require('express')
const mongoose = require('mongoose')
const StudentModel = require('./Students')

const app = express()
const port = 3000

app.use(express.json())

//connect to database
mongoose.connect('mongodb+srv://admin:admin@cluster0.ddehdzh.mongodb.net/practice')
    .then(db => console.log('DB is connected'))
    .catch(err => console.log(err))

//Getting all Students in the Database

//Start
app.get('/', (req, res) => {
    StudentModel.find()
        .then(students => res.json(students))
        .catch(err => res.status(500).json(err));
});
//End

//Get Student with id
//Start
app.get('/get/:id', (req, res) => {
    const id = req.params.id
    StudentModel.findById({_id: id})
        .then(post => res.json(post))
        .catch(err => console.log(err))
})
//End

//Get Student with idNum
//Start
app.get('/getid/:idNum', (req, res) => {
    const idNum = parseInt(req.params.idNum);
    StudentModel.findOne({idNum: idNum})
        .then(post => res.json(post))
        .catch(err => console.log(err))
})
//End

//Creating a new Student
//Start
app.post('/create', (req, res) => {
    StudentModel.create(req.body)
        .then(user => res.json(user))
        .catch(err => res.json(err))
})  
//End

//Update a Students information
//Start
app.put('/update/:id', (req, res) => {
    const id = req.params.id
    StudentModel.findByIdAndUpdate({_id: id},{
        name: req.body.name,
        idNum: req.body.idNum,
        course: req.body.course,
        college: req.body.college,
        age: req.body.age 
    }).then(user => res.json(user))
        .catch(err => res.json(err))
})
//End

//Delete a Student
//Start
app.delete('/deleteuser/:id', (req, res) => {
    const id = req.params.id
    StudentModel.findByIdAndDelete({_id: id})
        .then(response => res.json(response))
        .catch(err => res.json(err))
})
//End :)

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})