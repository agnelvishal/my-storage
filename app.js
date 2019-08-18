'use strict';

var express = require('express');
var app = express();


app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*"); // update to match the domain you will make the request from
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");

    next();
  });
  app.use(express.json());       // to support JSON-encoded bodies
  app.use(express.urlencoded({ extended: false })); // to support URL-encoded bodies



app.get('/random', function(req, res) {
  console.log("a ");
  const rand = Math.random() < 0.5
  res.json({random:rand});
});

var mysql = require('mysql');


app.post('/insert', function(req, res) {
  console.log("b ");

  const output =req.body.output;
  const txnHash =req.body.txnHash;
  let input =req.body.input;
  input = (input === 'true');

  //db conenction
  var connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'trust'
  })
  connection.connect()
  connection.query('INSERT INTO trust (input, output, txnHash) VALUES (?, ?, ?)', [input, output, txnHash], function (err, rows, fields) {
    if (err) throw err
  //    console.log('The solution is: ', rows[0]);  
  })
  connection.end();
  console.log("c ");

});

app.listen(3000, function() {
  console.log('Example app listening on port 4000!');
});