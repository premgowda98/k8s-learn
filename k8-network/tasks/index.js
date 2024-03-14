const express = require('express');
const axios = require('axios');

const app = express()

app.get('/', (req,res)=>{
	res.send(`<h1>Hello Guru, Code Changed</h1>`);
}
);


app.listen(8502, ()=>console.log('Running at port 8502'))
