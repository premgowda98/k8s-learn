const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');

const app = express()
app.use(bodyParser.json());

app.get('/task', async (req,res)=>{

	try {
		const response = await axios.get(`http://${process.env.AUTH_ADDR}/auth`)
		if (response.status===200){
			return res.json({message: 'Task got and also auth verified'});
		}
		return res.json({message: 'Taskify'});
	} catch {
		return res.json({message: 'Something went wrong in tasks'});
	}
}
);


app.listen(8502, ()=>console.log('Running at port 8502'))
