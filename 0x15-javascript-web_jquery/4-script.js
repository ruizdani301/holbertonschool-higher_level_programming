#!/usr/bin/node

const $ = window.$;

$("#toggle_header").click(function(){

  $('header').toggleClass('red green');

});
