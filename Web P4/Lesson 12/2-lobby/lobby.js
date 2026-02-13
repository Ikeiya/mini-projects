const app = new PIXI.Application({
    width: 700,
    height: 700,
});

document.body.appendChild(app.view);
let background = new PIXI.TilingSprite.from('assets/background.png', {width: 700, height: 700});
let door1 = PIXI.Sprite.from('assets/door.png');
let door2 = PIXI.Sprite.from('assets/door.png');
let door3 = PIXI.Sprite.from('assets/door.png');
var playerFrames = ["assets/player/1.png",
                    "assets/player/2.png",
                    "assets/player/3.png",
                    "assets/player/4.png"
                ]

var player = PIXI.AnimatedSprite.fromFrames(playerFrames);

bgm = PIXI.sound.Sound.from("assets/song2.mp3")
bgm.play({
    loop: true
});

player.width = 40;
player.height = 40;

gameCounter = localStorage.getItem("gameCounter")

background.anchor.set(0.5);
door1.anchor.set(0.5);
door2.anchor.set(0.5);
door3.anchor.set(0.5);
player.anchor.set(0.5)

background.x = 350;
background.y = 350;
door1.x = 130;
door1.y = 560;
door2.x = 350;
door2.y = 560;
door3.x = 570;
door3.y = 560;
player.x = 240;
player.y = 630;

app.stage.addChild(background);
app.stage.addChild(door1);
app.stage.addChild(door2);
app.stage.addChild(door3);
app.stage.addChild(player);

$(document).on("keydown", function(e) {
    if (e.keyCode == 65 && player.x >= 25)    {
        player.play();
        player.direction = "left";
        player.facingDirection = "left"
    }
    else if (e.keyCode == 68 && player.x <= 775)   {
        player.play()
        player.direction = "right"
        player.facingDirection = "right"
    }
    else    {
        player.stop()
        player.direction = "none"
    }

    if (e.keyCode == 87){
        player.direction = "up"
    }
});

function testForCollision(object1, object2) {
    const bounds1 = object1.getBounds();
    const bounds2 = object2.getBounds();

    return bounds1.x < bounds2.x + bounds2.width
        && bounds1.x + bounds1.width > bounds2.x
        && bounds1.y < bounds2.y + bounds2.height
        && bounds1.y + bounds1.height > bounds2.y;
};


$(document).on("keyup", function(){
    player.stop();
    player.direction = "none";
})

app.ticker.add(function(){
    player.animationSpeed = 0.16;

    if(player.direction == "left"){
        player.x -= 4;
    }
    else if (player.direction == "right") {
        player.x +=4;
    };

    if(player.direction == "up"){
        if (gameCounter == null){
            if (testForCollision(player, door1) == true){
                window.location.href = "../3-game1"
                localStorage.setItem("gameCounter", "1")
            }
        }   else if (gameCounter == "1")  {
            if (testForCollision(player, door2) == true){
                window.location.href = "../4-game2"
                localStorage.setItem("gameCounter", "2")
            }
        }   else    {
            if (testForCollision(player, door3) == true){
                window.location.href = "../5-game3"
            }
        }
    }

    if(player.facingDirection == "left") {
        player.texture.rotate = 12;
    }   else {
        player.texture.rotate = 0
    }
});