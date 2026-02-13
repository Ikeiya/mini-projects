var lesson6Array = [1, 3, 5, 6, 7, 9, 10];
var lesson6Array2 = [2, 5, 7, 10, 12, 14, 15, 9, 20];

function createNewArray(){
    var newArray = lesson6Array + lesson6Array2;
    document.getElementById("lesson6_arr").innerHTML = newArray;
}

function addBetweenArrays(){
    var newArray = [];
    for (var i = 0; i < lesson6Array.length-1; i++)   {
        newArray.push(lesson6Array[i] + lesson6Array2[i]);
    }
    document.getElementById("arrSum").innerHTML = newArray;
}

function skipNumbersInArrays(){
    var newArray = [];
    for (var i = 0; i < lesson6Array.length-1; i++)   {
        if (lesson6Array2[i] == 15) {
            break
        }   else if (lesson6Array2[i] > 12)    {
            continue
        }   else    {
            newArray.push(lesson6Array2[i]);
        }
    }
    document.getElementById("skipped").innerHTML = newArray;
}

function createArrayInArray(){
    nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
    document.getElementById("arrInArr").innerHTML = nested[0] + "<br>" + nested[1] + "<br>" + nested[2];
}

function findNumberSix(){
    nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
    document.getElementById("result").innerHTML = nested[1][2]
}

function findNumberEight(){
    nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
    for (var i = 0; i < nested.length; i++)   {
        for (var j = 0; j < nested.length; j++)   {
            if (nested[i][j] == 8)  {
                document.getElementById("result").innerHTML = nested[i][j];
                break
            }   else    {
                continue
            }
        }
    }   
}

function replacingIfElse(){
    var number = document.getElementById("dayNum").value;
    if (number == 1)  {
        document.getElementById("dayName").innerHTML = "Monday";
    }   else if (number == 2)  {
        document.getElementById("dayName").innerHTML = "Tuesday";
    }   else if (number == 3)  {
        document.getElementById("dayName").innerHTML = "Wednesday";
    }   else if (number == 4)  {
        document.getElementById("dayName").innerHTML = "Thursday";
    }   else if (number == 5)  {
        document.getElementById("dayName").innerHTML = "Friday";
    }   else if (number == 6)  {
        document.getElementById("dayName").innerHTML = "Saturday";
    }   else if (number == 7)  {
        document.getElementById("dayName").innerHTML = "Sunday";
    }   else    {
        document.getElementById("dayName").innerHTML = "Wrong!";
    }
}

function replacingSwitch(dayNum){
    switch(dayNum){
        case "1":
            document.getElementById("dayName2").innerHTML = "Monday";
            break;
        case "2":
            document.getElementById("dayName2").innerHTML = "Tuesday";
            break;
        case "3":
            document.getElementById("dayName2").innerHTML = "Wednesday";
            break;
        case "4":
            document.getElementById("dayName2").innerHTML = "Thursday";
            break;
        case "5":
            document.getElementById("dayName2").innerHTML = "Friday";
            break;
        case "6":
            document.getElementById("dayName2").innerHTML = "Saturday";
            break;
        case "7":
            document.getElementById("dayName2").innerHTML = "Sunday";
            break;
        default:
            document.getElementById("dayName2").innerHTML = "Wrong!";
    }
}