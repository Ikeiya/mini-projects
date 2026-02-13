//var foodOrderInput = document.getElementById("Food")

function addField(){
    document.getElementById("Food").innerHTML += "<br>";
    var newField = document.createElement("input")
    newField.setAttribute("type", "text");
    newField.setAttribute("name", "food");
    newField.setAttribute("placeholder", "Food Order");
    document.getElementById("Food").appendChild(newField);
}

function addTypeNumber(){
    var num1 = 20
    var num2 = 33
    var stringNum1 = num1.toString();
    var stringNum2 = num2.toString();
    document.getElementById("number1").innerHTML = "20 + 33 = " + (num1+num2) + "(Type:number)";
    document.getElementById("number2").innerHTML = "20 + 33 = " + (stringNum1+stringNum2) + "(Type:string)";

    // float
    var target1 = 3.14
    target = document.getElementById("target");
    target.innerHTML = "First float is " + target1;
    float1 = document.getElementById("float1");
    float1.innerHTML = "Type of float1: " + typeof float1;

    var result0 = 15;
    resultType0 = document.getElementById("m")
    resultType0.innerHTML = "Type of object is " + typeof result0 + " target support to be number"

    var result = null;
    resultType1 = document.getElementById("n")
    resultType1.innerHTML = "Type of object is " + typeof result + " target suppose to be null";

    var result2;
    resultType2 = document.getElementById("o")
    resultType2.innerHTML = "Type of object is " + typeof result2 + " target suppose to be undefined";   
}