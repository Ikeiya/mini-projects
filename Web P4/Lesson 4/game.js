var intWindowWidth = window.innerWidth;
var intWindowHeight = window.innerHeight;
var gameState = true
var score = 0

const app = new PIXI.Application({
    width: intWindowWidth,
    height: intWindowHeight,
    backgroundColor: 0x1099bb,
    resolution: window.devicePixelRatio || 1
});

const style = new PIXI.TextStyle({
    fill: "#001642",
    fillGradientType: 1,
    fontFamily: "\"Arial Black\", Gadget, sans-serif",
    fontSize: 30,
    fontWeight: "bolder"
});

document.body.appendChild(app.view);
var scoreLabel = new PIXI.Text("Score:"+score, style);


let background = PIXI.Sprite.from('assets/background.png');
let bird = PIXI.Sprite.from('assets/bird.png');
let pipe1Down = PIXI.Sprite.from('assets/pipe-down.png');
let pipe1Up = PIXI.Sprite.from('assets/pipe-up.png');
let pipe2Down = PIXI.Sprite.from('assets/pipe-down.png');
let pipe2Up = PIXI.Sprite.from('assets/pipe-up.png');
let pipe3Down = PIXI.Sprite.from('assets/pipe-down.png');
let pipe3Up = PIXI.Sprite.from('assets/pipe-up.png');
let pipe4Down = PIXI.Sprite.from('assets/pipe-down.png');
let pipe4Up = PIXI.Sprite.from('assets/pipe-up.png');

bird.fallingspeed = 0

pipe1Up.height += 700;
pipe1Down.height += 700;

pipe2Up.height += 700;
pipe2Down.height += 700;

pipe3Up.height += 700;
pipe3Down.height += 700;

pipe4Up.height += 700;
pipe4Down.height += 700;

background.anchor.set(0.5);
bird.anchor.set(0.5);
pipe1Down.anchor.set(0, 0);
pipe1Up.anchor.set(0, 1);
pipe2Down.anchor.set(0, 0);
pipe2Up.anchor.set(0, 1);
pipe3Down.anchor.set(0, 0);
pipe3Up.anchor.set(0, 1);
pipe4Down.anchor.set(0, 0);
pipe4Up.anchor.set(0, 1);
scoreLabel.anchor.set(0.5)



background.visible = false;

background.x = 100;
background.y = 300;
bird.x = 220;
bird.y = 300;

pipe1Up.x = 2000;
pipe1Up.y = 700;
pipe1Down.x = 2000;
pipe1Down.y = 550;

pipe2Up.x = 2500;
pipe2Up.y = 700;
pipe2Down.x = 2500;
pipe2Down.y = 550;

pipe3Up.x = 3000;
pipe3Up.y = 700;
pipe3Down.x = 3000;
pipe3Down.y = 550;

pipe4Up.x = 1500;
pipe4Up.y = 700;
pipe4Down.x = 1500;
pipe4Down.y = 550;

scoreLabel.x = 100;
scoreLabel.y = 10;

app.stage.addChild(background);
app.stage.addChild(bird);
app.stage.addChild(pipe1Down);
app.stage.addChild(pipe1Up);
app.stage.addChild(pipe2Down);
app.stage.addChild(pipe2Up);
app.stage.addChild(pipe3Down);
app.stage.addChild(pipe3Up);
app.stage.addChild(pipe4Down);
app.stage.addChild(pipe4Up);
app.stage.addChild(scoreLabel);

function setPipePosition(pipeUp, pipeDown)  {
    randomNum = Math.floor(100 * Math.random() + 225);
    randomNum2 = Math.floor(250 * Math.random() + 500);
    pipeDown.y = randomNum2;
    pipeUp.y = randomNum2 - randomNum;
};

function testForCollision(object1, object2) {
    const bounds1 = object1.getBounds();
    const bounds2 = object2.getBounds();

    return bounds1.x < bounds2.x + bounds2.width
        && bounds1.x + bounds1.width > bounds2.x
        && bounds1.y < bounds2.y + bounds2.height
        && bounds1.y + bounds1.height > bounds2.y;
}


setPipePosition(pipe1Up, pipe1Down);
setPipePosition(pipe2Up, pipe2Down);
setPipePosition(pipe3Up, pipe3Down);
setPipePosition(pipe4Up, pipe4Down);


$(document).on("keydown",function(event){
    if (gameState == true)  {
        if (event.keyCode == 32)    {
            bird.fallingspeed = -15;
            console.log(bird.y)
        };
    };
    bird.angle = -45
});

app.ticker.add(function(){

    bird.fallingspeed += 0.9;
    bird.y += bird.fallingspeed;
    if (gameState == true)  {

        pipe1Up.x -= 10;
        pipe1Down.x -= 10;
        if(pipe1Up.x < 20)   {
            pipe1Up.x = intWindowWidth;
            pipe1Down.x = intWindowWidth; 
            setPipePosition(pipe1Up, pipe1Down)
            score += 1
        }
        
        pipe2Up.x -= 10;
        pipe2Down.x -= 10;
        if(pipe2Up.x < 20)   {
            pipe2Up.x = intWindowWidth;
            pipe2Down.x = intWindowWidth; 
            setPipePosition(pipe2Up, pipe2Down)
            score += 1
        }

        pipe3Up.x -= 10;
        pipe3Down.x -= 10;
        if(pipe3Up.x < 20)   {
            pipe3Up.x = intWindowWidth;
            pipe3Down.x = intWindowWidth; 
            setPipePosition(pipe3Up, pipe3Down)
            score += 1
        }

        pipe4Up.x -= 10;
        pipe4Down.x -= 10;
        if(pipe4Up.x < 20)   {
            pipe4Up.x = intWindowWidth;
            pipe4Down.x = intWindowWidth; 
            setPipePosition(pipe4Up, pipe4Down)
            score += 1
        }

        if (bird.angle < 45)    {
            bird.angle += 3
        }
    }

    if (testForCollision(bird, pipe1Up) == true || testForCollision(bird, pipe1Down) == true)   {
        gameState = false

        if (bird.angle < 91)    {
            bird.angle += 3
        };
    }

    if (testForCollision(bird, pipe2Up) == true || testForCollision(bird, pipe2Down) == true)   {
        gameState = false

        if (bird.angle < 91)    {
            bird.angle += 3
        };
    }

    if (testForCollision(bird, pipe3Up) == true || testForCollision(bird, pipe3Down) == true)   {
        gameState = false

        if (bird.angle < 91)    {
            bird.angle += 3
        };
    }

    if (testForCollision(bird, pipe4Up) == true || testForCollision(bird, pipe4Down) == true)   {
        gameState = false

        if (bird.angle < 91)    {
            bird.angle += 3
        };
    }

    if (bird.y < 40) {
        gameState = false
    }
    scoreLabel.text = "Score: " + score;
});
