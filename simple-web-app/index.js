const express = require('express')

const app = express()

app.get('/', (req,res)=>{
	res.send(`<h1>Hello Guru, Code Changed</h1>`);
}
);

app.get('/error', (req,resp)=>{
	process.exit(1);
}
);

app.listen(8080, ()=>console.log('Running at port 8080'))
