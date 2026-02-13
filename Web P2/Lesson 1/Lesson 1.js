// document.getElementById(a)

var counter = 0;

function changeContent(){
    var change = document.getElementById("div1")

    change.innerHTML = "heyheyhey!!";
}

function alertOnLoad(){
    var whenLoad = alert("Welcome to Lesson 1 page")
}

function askName(){
    var askName = prompt("What is your name")
}

function requestConfirm(){
    var confirmation = confirm("Pay us 100$")
    document.write("Pay us 100$:"+confirmation+"Thank you")
}

function addNumber(){ 
    var addNumber = document.getElementById("div2");
    addNumber.innerHTML = counter;
    counter++;
}

function changeColor(){
    var colorA = document.getElementById("a");
    var colorB = document.getElementById("b");
    colorA.style.color = "lime";
    colorB.style.color = "blue";

    //colorA.style["color"] = "lime";
    //colorB.style["color"] = "lime";
}