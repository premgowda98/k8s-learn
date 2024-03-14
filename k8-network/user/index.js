const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');

const app = express()
app.use(bodyParser.json());

app.post('/login', async (req,res)=>{
	const { username, password } = req.body;

	if (password=='123'){
		const response = await axios.get(`http://${process.env.AUTH_ADDR}/auth`)
		if (response){
			res.json({message: 'Verified and also auth verified'});
		}
		res.json({message: 'Verified'});
	} else {
		res.status(401).json({message: 'Invalid Cred'})
	}
}
);

app.post('/singup', (req,res)=>{
	const { username, password } = req.body;

	res.json({message: 'User Creadted'});
}
);


app.listen(8503, ()=>console.log('Running at port 8503'))
