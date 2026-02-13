const app = new PIXI.Application({
    width: 704,
    height: 704,
    resolution: window.devicePixelRatio || 1
});
document.body.appendChild(app.view);
win = false

var playerFrames = ["Assets/player/1.png",
                    "Assets/player/2.png",
                    "Assets/player/3.png",
                    "Assets/player/4.png"
                ]

let background = new PIXI.Sprite.from('Assets/game1Map.png');
let treasure = new PIXI.Sprite.from('Assets/chest.png');
let hole = new PIXI.Sprite.from('Assets/hole.png');
let door = new PIXI.Sprite.from('Assets/door.png');
let msg = new PIXI.Sprite.from('Assets/msg.png');
var player = PIXI.AnimatedSprite.fromFrames(playerFrames);

player.width = 40;
player.height = 40;

hole.width = 44;
hole.height = 44;

treasure.width = 44;
treasure.height = 44;

background.width = 704;
background.height = 704;

door.width = 88;
door.height = 88;

background.anchor.set(0.5);
player.anchor.set(0.5);
treasure.anchor.set(0.5);
hole.anchor.set(0.5);
door.anchor.set(0.5);
msg.anchor.set(0.5)

background.x = 352;
background.y = 352;

treasure.x = 242;
treasure.y = 506;

player.x = 682;
player.y = 110;

hole.x = 506;
hole.y = 198;

door.x = 660;
door.y = 44;

msg.x = 352;
msg.y = 352;

door.visible = true;
msg.visible = false

app.stage.addChild(background);
app.stage.addChild(player);
app.stage.addChild(treasure);
app.stage.addChild(hole);
app.stage.addChild(door);
app.stage.addChild(msg);

function testForCollision(object1, object2) {
    const bounds1 = object1.getBounds();
    const bounds2 = object2.getBounds();

    return bounds1.x < bounds2.x + bounds2.width
        && bounds1.x + bounds1.width > bounds2.x
        && bounds1.y < bounds2.y + bounds2.height
        && bounds1.y + bounds1.height > bounds2.y;
};

function random()  {
    randomNum = Math.floor(2 * Math.random() + 225);
};

function testForCollision2(object1, object2) {
    const bounds1 = object1.getBounds();
    const bounds2 = object2.getBounds();

    return bounds1.x - 44 < bounds2.x + bounds2.width
        && bounds1.x - 44 + bounds1.width > bounds2.x
        && bounds1.y < bounds2.y + bounds2.height
        && bounds1.y + bounds1.height > bounds2.y;
};

$(document).on("keydown", function(e) {
    if (win == false)    {
        if (e.keyCode == 65 && player.x >= 25)    {
            player.play();
            player.direction = "left";
            player.facingDirection = "left"
            player.x -= 44;
        }
        else if (e.keyCode == 68 && player.x <= 681)   {
            player.play()
            player.direction = "right"
            player.facingDirection = "right"
            player.x += 44;
        }
        else if (e.keyCode == 87 && player.y >= 25)   {
            player.play()
            player.direction = "up"
            player.y -= 44;
        }
        else if (e.keyCode == 83 && player.y <= 681)   {
            player.play()
            player.direction = "down"
            player.y += 44;
        }
        else    {
            player.stop()
            player.direction = "none"
        }
    }
    else if (win == true){
        if (e.keyCode == 65 && player.x >= 25)    {
            player.play();
            player.direction = "left";
            player.facingDirection = "left"
            player.x -= 44;
        }
        else if (e.keyCode == 68 && player.x <= 681)   {
            player.play()
            player.direction = "right"
            player.facingDirection = "right"
            if (testForCollision2(door, player) == false){
                player.x += 44;
            };
        }
        else if (e.keyCode == 87 && player.y >= 25)   {
            player.play()
            player.direction = "up"
            player.y -= 44;
        }
        else if (e.keyCode == 83 && player.y <= 681)   {
            player.play()
            player.direction = "down"
            player.y += 44;
        }
        else    {
            player.stop()
            player.direction = "none"
        }
    }
});


app.ticker.add(function(){
    player.animationSpeed = 0.16;

    if(player.facingDirection == "left") {
        player.texture.rotate = 12;
    }   else {
        player.texture.rotate = 0
    };

    if(testForCollision(player, treasure) == true){
        if (player.direction == "up")    {
            treasure.y -= 44
        }
        else if (player.direction == "down")    {
            treasure.y += 44
        }
        else if (player.direction == "left")    {
            treasure.x -= 44
        }
        else if (player.direction == "right")    {
            treasure.x += 44
        }
    }

    if(testForCollision(hole, treasure) == true){
        door.visible = true;
        treasure.visible = false;
        win = true;
    };

    if(testForCollision(player, door) == true && win == true)
        setTimeout(function(){
            window.location.href = "../2-lobby"
        })
});