const express = require('express');
const axios = require('axios');

const app = express()

app.get('/auth', (req,res)=>{
	return res.json({token: 'yes'});
}
);

app.listen(8501, ()=>console.log('Running at port 8501'))
