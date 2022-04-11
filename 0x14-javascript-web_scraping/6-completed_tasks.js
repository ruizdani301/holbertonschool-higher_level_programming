#!/usr/bin/node

const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';

request(url, function (error, results, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(typeof (body));
    const data = JSON.parse(body);
    console.log(typeof (data));

    const newDic = {};

    for (let i = 0; i < data.length - 1; i++) {
      if (data[i].completed === true) {
        if (!newDic[data[i].userId]) {
          newDic[data[i].userId] = 1;
        } else {
          newDic[data[i].userId]++;
        }
      }
    }
    console.log(newDic);
  }
});
