#!/usr/bin/node

const list = require("./100-data").list;

const new_list = list.map((x, index) => x * index);
console.log(list)
console.log(new_list)