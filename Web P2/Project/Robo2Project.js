var word = "";
var arr = [];
var lives = 7;

function startGame(){
    var dictionary = document.getElementById("input").value;
    var selectText = dictionary.split(" ");
    word = selectText[Math.floor(Math.random()*selectText.length)];
    counter = word.length;
    console.log(word)
    for(i = 0; i < word.length; i++) {
        arr.push("_ ")
    }
    document.getElementById("wordLength").innerHTML = arr
    
    document.getElementById("input").value = ""
}

function checkword(){
    var numHearts = document.getElementsByClassName("hearts");
    console.log(numHearts)
    var letter = document.getElementById("guess").value;
    var tempArray = [];
    var correctness = true;
    for(i = 0; i < word.length; i++) {
        if (letter == word[i]) {
            if (arr[i] != letter + " ") {
                arr[i] = letter + " ";
                document.getElementById("wordLength").innerHTML = arr;
                tempArray.push(i);
                counter = counter - 1;
            }
        }

    }
    
    if(tempArray.length > 0){
        document.getElementById("response").innerHTML = "The letter " + letter + " is correct";
    } else {
        document.getElementById("response").innerHTML = "The letter " + letter + " is incorrect";
        lives = lives - 1
        numHearts[lives].style.visibility = "hidden";
    }

    if (lives == 0) {
        document.getElementById("worldDestruction").style.visibility = "hidden";
        document.getElementById("theLoserDiv").style.visibility = "visible";
    }
    console.log(counter)

    if (counter == 0) {
        document.getElementById("worldDestruction").style.visibility = "hidden";
        document.getElementById("theLastDiv").style.visibility = "visible";
    }

    document.getElementById("guess").value = ""
}

function reset(){
    location.reload();
}

function startPage(){
    document.getElementById("theLastDiv").style.visibility = "hidden";
    document.getElementById("theLoserDiv").style.visibility = "hidden";
}