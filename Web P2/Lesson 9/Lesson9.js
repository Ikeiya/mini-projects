function init(){
    formula = document.getElementsByClassName("display");
    for (var i = 0; i < formula.length; i++) {
        formula[i].value = "";
        formula[i].disabled = true;
        formula[i].style.height = "20px"
    }
    btns = document.getElementsByClassName("simpleCalculatorInput");
    for (var i = 0; i < btns.length; i++) {
        btns[i].style.padding = "50px";
        btns[i].style.fontsize = "5px";
        btns[i].style.width = "70px";
    }
    advInput = document.getElementsByClassName("advCalculatorInput");
    for (var i = 0; i < btns.length; i++) {
        advInput[i].value = "";
        advInput[i].style.width = "50px";
    }
    advBtns = document.getElementsByClassName("advCalculator");
    for (var i = 0; i < advBtns.length; i++) {
        advBtns[i].style.padding = "8px";
        advBtns[i].style.fontsize = "12px";
        advBtns[i].style.width = "100px";
    }
}

opState = false
function enteredFunction(number){
    input1 = document.getElementById("input1");
    input2 = document.getElementById("input2");
    if (opState == false) {
        input1.value += number;
    } else {
        input2.value += number;
    }
}

function enteredOperator(actualOperator) {
    opState = true;
    operatorInput = document.getElementById("operator");
    operatorInput.value += actualOperator;
}

function getFormula() {
    num1 = document.getElementsByClassName("display")[0].value;
    opVal = document.getElementsByClassName("display")[1].value;
    num3 = document.getElementsByClassName("display")[2].value;

    formula = num1+opVal+num3;
    return formula
}

function calculate() {
    try {
        answer = eval(getFormula());
        if (answer == Infinity) {
            throw "Please don't break the calculator with infinity"
        }
    }
    catch(err) {
        alert(err)
    }
    finally {
        document.getElementsByClassName("display")[3].value = answer;
    }
}

function clearFunction() {
    displayedNumber = document.getElementsByClassName("display");
    for (var i = 0; i < displayedNumber.length; i++) {
        displayedNumber[i].value = ""
    }
}

function mathPower() {
    base = document.getElementById("advCalculatorInput").value;
    power = document.getElementById("advCalculatorInput2").value;

    answer = Math.pow(base, power);
    document.getElementById("answer").innerHTML = answer; 
}