var intWindowWidth = window.innerWidth;
var intWindowHeight = window.innerHeight;


const app = new PIXI.Application({
    width: intWindowWidth,
    height: intWindowHeight,
    backgroundColor: 0x1099bb,
    resolution: window.devicePixelRatio || 1
});

document.body.appendChild(app.view);

let background = PIXI.Sprite.from('assets/background.png');
let bird = PIXI.Sprite.from('assets/bird.png');
let pipeDown = PIXI.Sprite.from('assets/pipe-down.png');
let pipeUp = PIXI.Sprite.from('assets/pipe-up.png');

bird.fallingspeed = 0

pipeUp.height += 700;
pipeDown.height += 700;

background.anchor.set(0.5);
bird.anchor.set(0.5);
pipeDown.anchor.set(0, 0);
pipeUp.anchor.set(0, 1);

background.visible = false;

background.x = 100;
background.y = 300;
bird.x = 220;
bird.y = 300;
pipeUp.x = 1500;
pipeUp.y = 700;
pipeDown.x = 1500;
pipeDown.y = 550;

app.stage.addChild(background);
app.stage.addChild(bird);
app.stage.addChild(pipeDown);
app.stage.addChild(pipeUp);

function setPipePosition(pipeUp, pipeDown)  {
    randomNum = Math.floor(100 * Math.random() + 225);
    randomNum2 = Math.floor(250 * Math.random() + 500);
    pipeDown.y = randomNum2;
    pipeUp.y = randomNum2 - randomNum;
};

setPipePosition(pipeUp, pipeDown);

$(document).on("keydown",function(event){
    if (event.keyCode == 32)    {
        bird.fallingspeed = -10;
        console.log(bird.y)
    }
});

app.ticker.add(function(){
    bird.fallingspeed += 0.5;
    bird.y += bird.fallingspeed;

    pipeUp.x -= 10;
    pipeDown.x -= 10;
    if(pipeUp.x < 20)   {
        pipeUp.x = intWindowWidth;
        pipeDown.x = intWindowWidth; 
        setPipePosition(pipeUp, pipeDown)
    }

});

