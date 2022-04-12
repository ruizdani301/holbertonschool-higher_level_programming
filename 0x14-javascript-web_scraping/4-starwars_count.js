#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
request(url, function (error, results, body) {
  if (error) {
    console.log(error);
  } else {
    let cont = 0;
    const movieData = JSON.parse(body).results;

    for (let i = 0; i < movieData.length - 1; i++) {
      const chart = (movieData[i].characters);
      for (let j = 0; j < chart.length - 1; j++) {
        if (chart[j].includes('https://swapi-api.hbtn.io/api/people/18/')) {
          cont++;
        }
      }
    }
    console.log(cont);
  }
});
