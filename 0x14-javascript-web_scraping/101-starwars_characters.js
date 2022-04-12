#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, results, body) {
  if (error) {
    console.log(error);
  } else {
    const data = (JSON.parse(body).characters);
    function nombres (data) {
      const actual = data.shift();
      if (actual == null) {
        return;
      }
      request(actual, function (error, result, body) {
        if (error) {
          console.log(error);
        } else {
          const dataDos = (JSON.parse(body));
          console.log(dataDos.name);
          nombres(data);
        }
      });
    }
    nombres(data);
  }
});
