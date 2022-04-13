#!/usr/bin/node

const $ = window.$;
$("#add_item").click(function(){

  $('UL.my_list').append('<li>item</li>');

});
