#!/usr/bin/node

const $ = window.$;
$("#red_header").click(function(){
    $("header").css("color", "#FF0000");
    $(this).addClass('red');
});