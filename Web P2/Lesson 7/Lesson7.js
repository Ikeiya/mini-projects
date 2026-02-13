function lesson7OpenNewWindow(){
    window.open("","","width=800, height=600"); // opens a new window (by adding width and height)
}

function lesson7OpenNewTab(){
    window.open("https://www.w3schools.com"); //open new tab
}

function lesson7WindowContents(){
    lesson7newWindow = window.open("","", "width=800, height=600");
    var windowText = "<p>width = 800</p><p>height = 600</p>";
    lesson7newWindow.document.write(windowText);
}

function lesson7closeWindow(){
    lesson7newWindow.close();
}

function lesson7resizeWindow(){
    lesson7newWindow.resizeTo(500, 300)
    var windowText = "<p>width = 500</p><p>height = 300</p>"
    lesson7newWindow.document.write(windowText);
}

function lesson7findWindowWidth(){
    document.getElementById("innerWindowWidth").innerHTML += "window.innerWidth: " + window.innerWidth;
}

function lesson7findWindowHeight(){
    document.getElementById("innerWindowHeight").innerHTML += "window.innerHeight: " + window.innerHeight;
}

function lesson7findScreenWidth(){
    document.getElementById("innerScreenWidth").innerHTML += "screen.width: " + screen.width;
}

function lesson7findScreenHeight(){
    document.getElementById("innerScreenHeight").innerHTML += "screen.height: " + screen.height;
}

function lesson7changeColor(){
    //document.getElementsByClassName("color")[0].getElementsByClassName.color = "orange"; Only for first item
    var colorElement = document.getElementsByClassName("color");
    for (var i = 0; i < colorElement.length; i++) {
        colorElement[i].style.color = "orange";
    }
}

function lesson7changeListTag(){
    var listItems = document.getElementsByTagName("li");
    for (var i = 0; i < listItems.length; i++) {
        if (listItems[i].style["list-style-type"] != "circle") {
            listItems[i].style.listStyleType = "circle";
        }   else    {
            listItems[i].style.listStyleType = "disc";
        }
    } 
}

function prevImgLesson8() {
    currentSrc = document.getElementsByTagName("img")[0].src;
    slashPosition = currentSrc.lastIndexOf('/'); //finds the last index of the array currentSrc
    currentImageName = currentSrc.substring(slashPosition+1, currentSrc.length);
    console.log(currentImageName);
    if  (currentImageName == 'ad3.jpg')   {
        currentSrc = currentSrc.replace(currentImageName,'ad2.jpg');
        document.getElementsByTagName("img")[0].src = currentSrc;
        document.getElementsByTagName("img")[0].alt = 'ad2';
    }   else if (currentImageName == 'ad2.jpg') {
        currentSrc = currentSrc.replace(currentImageName,'ad1.jpg');
        document.getElementsByTagName("img")[0].src = currentSrc;
        document.getElementsByTagName("img")[0].alt = 'ad1';
    }   else if (currentImageName == 'ad1.jpg') {
        currentSrc = currentSrc.replace(currentImageName,'ad3.jpg');
        document.getElementsByTagName("img")[0].src = currentSrc;
        document.getElementsByTagName("img")[0].alt = 'ad3';
    }
}


function conImgLesson8() {
    currentSrc = document.getElementsByTagName("img")[0].src;
    slashPosition = currentSrc.lastIndexOf('/'); //finds the last index of the array currentSrc
    currentImageName = currentSrc.substring(slashPosition+1, currentSrc.length);
    console.log(currentImageName);
    if  (currentImageName == 'ad3.jpg')   {
        currentSrc = currentSrc.replace(currentImageName,'ad1.jpg');
        document.getElementsByTagName("img")[0].src = currentSrc;
        document.getElementsByTagName("img")[0].alt = 'ad1';
    }   else if (currentImageName == 'ad2.jpg') {
        currentSrc = currentSrc.replace(currentImageName,'ad3.jpg');
        document.getElementsByTagName("img")[0].src = currentSrc;
        document.getElementsByTagName("img")[0].alt = 'ad3';
    }   else if (currentImageName == 'ad1.jpg') {
        currentSrc = currentSrc.replace(currentImageName,'ad2.jpg');
        document.getElementsByTagName("img")[0].src = currentSrc;
        document.getElementsByTagName("img")[0].alt = 'ad2';
    }
}

