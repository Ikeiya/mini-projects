const app = new PIXI.Application({
    width: 800, 
    height: 700,
    backgroundColor: 0x1099bb,
    resolution: window.devicePixelRatio || 1
});

document.body.appendChild(app.view);

const style = new PIXI.TextStyle({
    fill: "#001642",
    fillGradientType: 1,
    fontFamily: "\"Arial Black\", Gadget, sans-serif",
    fontSize: 30,
    fontWeight: "bolder"
});


var colorLabel = new PIXI.Text('a ', style);
var pointsLabel = new PIXI.Text('', style);

let dot1 = PIXI.Sprite.from('Assets/dot1.png');
let dot2 = PIXI.Sprite.from('Assets/dot2.png');
let dot3 = PIXI.Sprite.from('Assets/dot3.png');
let dot4 = PIXI.Sprite.from('Assets/dot4.png');
let dot5 = PIXI.Sprite.from('Assets/dot5.png');
let startButton = PIXI.Sprite.from('Assets/startButton.png')
let restartButton = PIXI.Sprite.from('Assets/restartButton.png')

dot1.anchor.set(0.5);
dot2.anchor.set(0.5);
dot3.anchor.set(0.5);
dot4.anchor.set(0.5);
dot5.anchor.set(0.5);
pointsLabel.anchor.set(0.5);
colorLabel.anchor.set(0.5);
startButton.anchor.set(0.5);
restartButton.anchor.set(0.5);


dot1.x = 100;
dot1.y = 300;
dot2.x = 220;
dot2.y = 300;
dot3.x = 340;
dot3.y = 300;
dot4.x = 460;
dot4.y = 300;
dot5.x = 580;
dot5.y = 300;
pointsLabel.x = 340;
pointsLabel.y = 500;
colorLabel.x = 340;
colorLabel.y = 50
startButton.x = 400
startButton.y = 400
restartButton.x = 400
restartButton.y = 400

dot1.visible = false;
dot2.visible = false;
dot3.visible = false;
dot4.visible = false;
dot5.visible = false;
restartButton.visible = false;
colorLabel.visible = false;
pointsLabel.visible = false;

startButton.interactive = true;
startButton.buttonMode = true;
restartButton.interactive = false;
restartButton.buttonMode = false;

app.stage.addChild(dot1);
app.stage.addChild(dot2);
app.stage.addChild(dot3);
app.stage.addChild(dot4);
app.stage.addChild(dot5);
app.stage.addChild(colorLabel);
app.stage.addChild(pointsLabel);
app.stage.addChild(startButton);
app.stage.addChild(restartButton);

startButton.on("click", function(){
    dot1.visible = true;
    dot2.visible = true;
    dot3.visible = true;
    dot4.visible = true;
    dot5.visible = true;
    colorLabel.visible = true;
    startButton.visible = false;
    pointsLabel.visible = true;
    dot1.interactive = true;
    dot1.buttonMode = true;
    dot2.interactive = true;
    dot2.buttonMode = true;
    dot3.interactive = true;
    dot3.buttonMode = true;
    dot4.interactive = true;
    dot4.buttonMode = true;
    dot5.interactive = true;
    dot5.buttonMode = true;
    startButton.interactive = false;
    startButton.buttonMode = false;
});

var point = 0;
randomNum = Math.floor(5 * Math.random());
checkColor(randomNum);
var label = randomNum

function checkColor(randomNum){
    if (randomNum == 0){
        colorLabel.text = "red"
    }   else if (randomNum == 1){
        colorLabel.text = "yellow"
    }   else if (randomNum == 2){
        colorLabel.text = "blue"
    }   else if (randomNum == 3){
        colorLabel.text = "purple"
    }   else    {
        colorLabel.text = "pink"
    }
}

function checkPoint(label, randomNum, point){
    if  (randomNum == label)    {
        point++;
        pointsLabel.text = "your current amount of point is " + point;
    }   else    {
        point--;
        pointsLabel.text = "your current amount of point is " + point;
    }
    if (point < 11)  {
        return point
    }   else    {
        dot1.visible = false;
        dot2.visible = false;
        dot3.visible = false;
        dot4.visible = false;
        dot5.visible = false;
        restartButton.visible = true;
        colorLabel.visible = false;
        pointsLabel.visible = false;
        restartButton.interactive = true;
        restartButton.buttonMode = true;
    }
}


dot1.on("click", function(){
    label = 0
    point = checkPoint(label, randomNum, point)
    randomNum = Math.floor(5 * Math.random());
    checkColor(randomNum)
});

dot2.on("click",function(){
    label = 1
    point = checkPoint(label, randomNum, point)
    randomNum = Math.floor(5 * Math.random());
    checkColor(randomNum)
});

dot3.on("click",function(){
    label = 2
    point = checkPoint(label, randomNum, point)
    randomNum = Math.floor(5 * Math.random());
    checkColor(randomNum)
});

dot4.on("click",function(){
    label = 3
    point = checkPoint(label, randomNum, point)
    randomNum = Math.floor(5 * Math.random());
    checkColor(randomNum)
});

dot5.on("click",function(){
    label = 4
    point = checkPoint(label, randomNum, point)
    randomNum = Math.floor(5 * Math.random());
    checkColor(randomNum)
});

 