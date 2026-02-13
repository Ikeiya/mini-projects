function checkValueOfNameLesson8(name) {
    value = document.getElementById("name");
    value.style.backgroundColor = "white";
    if (name == "") {
        value.style.border = "2px solid red"
    }   else    {
        value.style.border = "2px solid green"
    }
}

function  highlightLesson8() {
    nameBox = document.getElementById("name");
    nameBox.style.backgroundColor = "lightgreen";
}

function clearFormLesson8() {
    document.forms["questions"]["name"].value = "";
    subject = document.forms["questions"]["subject"];
    subjectChecked = 0;
    for (var i = 0; i < subject.length; i++) {
        subject[i].checked = false;
    }
    document.forms["questions"]["grade"].value = "default";
}

function subjectLesson8(subject) {
    if (subject == "Chinese") {
        document.getElementsByTagName("img")[0].src = "chinese.jpg";
        document.getElementsByTagName("img")[0].alt = "chinese";
    } else if (subject == "English") {
        document.getElementsByTagName("img")[0].src = "english.jpg";
        document.getElementsByTagName("img")[0].alt = "english";
    } else if (subject == "Maths") {
        document.getElementsByTagName("img")[0].src = "math.jpg";
        document.getElementsByTagName("img")[0].alt = "math";
    }
}

function validateAll() {

    studentName = document.forms["questions"]["name"].value
    subjectName = document.forms["questions"]["subject"]
    grade = document.forms["questions"]["grade"].value
    if (studentName == "") {
        alert("Enter your name")
    } else if(subjectName == ) {

    }
}