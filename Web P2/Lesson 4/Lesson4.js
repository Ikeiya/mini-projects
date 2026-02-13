var newArray = [];

function findWordsInString(){
    var word = document.getElementById("word").value;
    //find length of word
    var lengthOfWord = word.length;
    document.getElementById("wordOutput").innerHTML += "The length of the word is " + lengthOfWord;
}

function showIndexOfString(){
    var word = document.getElementById("word2").value;
    var lengthOfWord = word.length;
    var counter = 0;
    document.getElementById("allIndex").innerHTML += "Original word is " + word + "<br>"
    while(counter < lengthOfWord) {
        //word[counter] finds index
        document.getElementById("allIndex").innerHTML += "Letter " + counter + " is : " + word[counter] + "<br>"
        counter += 1
    }
}

function findIndexOfWord(){
    var letter = document.getElementById("target").value;
    var target = document.getElementById("originalTarget1").innerHTML;
    //indexOf finds the number of word in the sentence
    document.getElementById("index").innerHTML += "The index of the word " + letter + " in the setence is " + target.indexOf(letter);
}

function splicingString(){
    var sentence = document.getElementById("word3").value;
    document.getElementById("extracted").innerHTML += "slice(2,8): " + sentence.slice(2, 8) + "<br>";
    document.getElementById("extracted").innerHTML += "slice(-5,-1): " + sentence.slice(-5,-1) + "<br>";
    document.getElementById("extracted").innerHTML += "substring(2,8): " + sentence.substring(2, 8) + "<br>";
    document.getElementById("extracted").innerHTML += "substring(-5,-1): " + sentence.slice(-5, -1) + "<br>";
    document.getElementById("extracted").innerHTML += "substr(2,8): " + sentence.substr(2,8) + "<br>";
    document.getElementById("extracted").innerHTML += "substr(-1,8): " + sentence.substr(-1, 8) + "<br>";
}

function showArray(){
    var arr = [9, "a", 300, "qwerty", "a", 33, "heelo", "@@"];
    document.getElementById("arr").innerHTML = arr;
}

function hideArray(){
    var arr = [];
    document.getElementById("arr").innerHTML = arr;
}

function createArray(){
    document.getElementById("arrMsg").innerHTML = "Array created!";
}

function addItem(){
    var newcounter = 0;
    newArray.push(newcounter);
    newcounter++;
    document.getElementById("arr2").innerHTML = newArray;
}

function removeItem(){
    newArray.pop();
    document.getElementById("arr2").innerHTML = newArray;
}

function addFirstItem(){
    newArray.unshift("First");
    document.getElementById("arr2").innerHTML = newArray;
}

function removeFirstItem(){
    newArray.shift();
    document.getElementById("arr2").innerHTML = newArray;
}