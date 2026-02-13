"use strict";
var d = new Date()

function initLesson10(){
    document.getElementById("current").innerHTML = d
    var year = d.getFullYear();
    var month = d.getMonth();
    var day = d.getDate();
    var hour = d.getHours();
    var minute = d.getMinutes();
    var second = d.getSeconds();
    document.getElementById("yearLesson10").innerHTML = year;
    document.getElementById("monthLesson10").innerHTML = month;
    document.getElementById("dayLesson10").innerHTML = day;
    document.getElementById("hourLesson10").innerHTML = hour;
    document.getElementById("minuteLesson10").innerHTML = minute;
    document.getElementById("secondLesson10").innerHTML = second;
}

function getDateOf10Days(){
    var today = d.getTime();
    var after10 = today + (1000 * 60 * 60 * 24 * 10)
    var after10 = new Date(after10);
    document.getElementById("afterTenDays").innerHTML = "Ten Days Later: " + after10
}

function datediff(){
    var firstDate = document.getElementById("date1").value;
    var secondDate = document.getElementById("date2").value;

    //convert inputs into Date object & in ms format (for calculation)
    var firstDate = new Date(firstDate).getTime();
    var secondDate = new Date(secondDate).getTime();

    //find date difference in ms
    var diff = secondDate - firstDate;
    var diff = (diff/1000) / 3600 / 24;
    document.getElementById("dateChange").innerHTML = diff + " days";
}

function createRecordTable(){
    var month = d.getMonth() + 1;
    var name = document.getElementById("nameLesson10").value;
    var birthday = document.getElementById("birthdayLesson10").value;
    var table = document.getElementById("tableLesson10");
    var row = table.insertRow(-1);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var firstDate = document.getElementById("birthdayLesson10").value;
    var firstDate = new Date(firstDate).getMonth() + 1;

    console.log(month)
    if (month == firstDate) {
        cell3.innerHTML = "<img src='openedGift.jpg'>"
    }   else    {
        cell3.innerHTML = "<img src='unopenedGift.jpg'>" 
    }

    if (isNaN(name) == true) {
        alert("There is a number in your name!")
    }

    cell1.innerHTML = name;
    cell2.innerHTML = birthday;
}