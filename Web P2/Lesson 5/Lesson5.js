function addNumbersToArray(){
    var newArray = [];
    for (var i = 0; i < 10; i++) {
        newArray.push(i);
    }
    document.getElementById("Lesson5_input").innerHTML = newArray;
}

function addRanNumbersToArray(){
    var newArray = [];
    for (var i = 0; i < 10; i++) {
        random = Math.floor(Math.random() * 100);
        newArray.push(random);
    }
    document.getElementById("Lesson5_input1").innerHTML = newArray;
}

function findValueOfFirstItem(){
    var newArray = [1, 2, 3, 4, 5, 6, 10, 9, 8];
    document.getElementById("Lesson5_input2").innerHTML = "Original Array is " + newArray + ", 1st value is " + newArray[0];
}

function findValueOfLastItem(){
    var newArray = [1, 2, 3, 4, 5, 6, 10, 9, 8];
    document.getElementById("Lesson5_input3").innerHTML = "Original Array is " + newArray + ", last value is " + newArray[newArray.length - 1];
}

function find5InArray(){
    var arrayWithFive = [1, 2, 3, 4, 5, 6, 10, 9, 8];
    for (var i = 0; i <arrayWithFive.length; i++) {
        if (arrayWithFive[i] == 5) {
            document.getElementById("Lesson5_input4").innerHTML = arrayWithFive + " contains 5";
            break;
        }   else    {
            document.getElementById("Lesson5_input4").innerHTML = arrayWithFive + " doesn't contain 5";
        }
    }
}

function isTheNumber5(){
    var arrayWithFive = [1, 2, 3, 4, 5, 6, 10, 9, 8];
    var resultArray = [];
    for (var i = 0; i <arrayWithFive.length; i++) {
        if (arrayWithFive[i] == 5) {
            resultArray.push("true");
        }   else    {
            resultArray.push("false");
        }
    }
    document.getElementById("Lesson5_input4").innerHTML = "Original Array is " + arrayWithFive + ", the result is " + resultArray;
}

function findEvenNumber(){
    var newArray = [1, 2, 3, 4, 5, 6, 10, 9, 8];
    var resultArray = [];
    for (var i = 0; i < newArray.length; i++) {
        if (newArray[i] % 2 == 0) {
            resultArray.push(" even");
        }   else    {
            resultArray.push(" odd");
        }
    }
    document.getElementById("Lesson5_input5").innerHTML = "Original Array is " + newArray + ", the result is " + resultArray;
}

function displayOnCondition(){
    var newArray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
    var resultArray = [];
    var resultArray2 = [];
    var resultArray3 = [];
    for (var i = 0; i < newArray.length; i++) {
        if (newArray[i] % 2 == 0 && newArray[i] % 5 == 0) {
            resultArray.push(newArray[i]);
        }
    }
    for (var i = 0; i < newArray.length; i++) {
        if (newArray[i] % 3 == 0) {
            continue
        }   else    {
            resultArray2.push(newArray[i]);
        }
    }
    for (var i = 0; i < newArray.length; i++) {
        if (newArray[i] < 8 && newArray[i] > 3) {
            continue
        }   else    {
            resultArray3.push(newArray[i]);
        }
    }
    document.getElementById("Lesson5_input6").innerHTML = "The numbers " + resultArray + " follows statement 1";
    document.getElementById("Lesson5_input6").style.color = 'red';
    document.getElementById("Lesson5_input7").innerHTML = "The numbers " + resultArray2 + " follows statement 2";
    document.getElementById("Lesson5_input7").style.backgroundColor = 'green';
    document.getElementById("Lesson5_input8").innerHTML = "The numbers " + resultArray3 + " follows statement 3";
}