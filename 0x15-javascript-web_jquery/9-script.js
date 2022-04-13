#!/usr/bin/node
const $ = window.$;
$.get('https://fourtonfish.com/hellosalut/?lang=fr', (data) => {
  $('DIV#hello').append('<li>' + data.hello + '</li>');
});
