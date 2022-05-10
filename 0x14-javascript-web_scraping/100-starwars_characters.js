#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, results, body) {
  if (error) {
    console.log(error);
  } else {
    /*const urlDos = [];*/
    const data = (JSON.parse(body).characters);

    for (let i = 0; i < data.length; i++) {
      let urlDos = ('');
      urlDos = (data[i]);

      request(urlDos, function (error, results, body) {
        if (error) {
          console.log(error);
        } else {
          const dataDos = (JSON.parse(body));
          console.log(dataDos.name);
        }
      });
    }
  }
});
