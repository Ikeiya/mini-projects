function changeToNumber(){
    var input ="15.5";
    var intNumber = parseInt(input);
    document.getElementById("1").innerHTML += input + " is a type of " + typeof input + "<br>" + "After parseInt(): " + " is " + typeof intNumber;
}

function changeToString(){
    var input = 15.5;
    var stringNumber = toString(input);
    document.getElementById("2").innerHTML += input + " is a type of " + typeof input + "<br>" + "After toString(): " + " is " + typeof stringNumber;
}

function changeToFloat(){
    var input = 15.5;
    var floatNumber = parseFloat(input);
    document.getElementById("3").innerHTML += input + " is a type of " + typeof input + "<br>" + "After toFloat(): " + " is " + typeof floatNumber;
}

function convertToUpperCase(){
    input = document.getElementById("4").value;
    newUpperCase = input.toUpperCase(input);
    document.getElementById("5").innerHTML += input + " after .toUpperCase() is " + newUpperCase;
}

function convertToLowerCase(){
    input = document.getElementById("4").value;
    newLowerCase = input.toLowerCase(input);
    document.getElementById("7").innerHTML += input + " after .toLowerCase() is " + newLowerCase;
}

function trimWhiteSpace(){
    input = document.getElementById("8").value;
    trimmedInput = input.trim();
    document.getElementById("9").innerHTML += input + " after .trim() is " + trimmedInput;
}

function getCharacterFromString(){
    input = document.getElementById("10").value;
    firstCharacter = input[0]
    document.getElementById("11").innerHTML += input + "'s first character is " + firstCharacter;
}

function addTwoCharacters(){
    input = document.getElementById("12").value;
    secondInput = document.getElementById("13").value;
    document.getElementById("14").innerHTML += parseInt(input) + parseInt(secondInput);
    document.getElementById("12").disabled = true;
    document.getElementById("13").disabled = true;
}

function reset(){
    document.getElementById("12").disabled = false;
    document.getElementById("13").disabled = false;
}