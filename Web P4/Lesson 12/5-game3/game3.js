const app = new PIXI.Application({
    width: 704,
    height: 704,
    resolution: window.devicePixelRatio || 1
});
document.body.appendChild(app.view);

bgm = PIXI.sound.Sound.from("assets/song5.mp3")
bgm.play({
    loop: true
});

var playerFrame = ["Assets/player/1.png",
                    "Assets/player/2.png",
                    "Assets/player/3.png",
                    "Assets/player/4.png"
                ]

var monsterFrame1 = ["Assets/monster1/1.png",
                "Assets/monster1/2.png",
                "Assets/monster1/3.png",
                "Assets/monster1/4.png"
            ]

var monsterFrame2 = ["Assets/monster2/1.png",
                    "Assets/monster2/2.png",
                    "Assets/monster2/3.png",
                    "Assets/monster2/4.png"
                ]
var monsterFrame3 = ["Assets/monster3/1.png",
                "Assets/monster3/2.png",
                "Assets/monster3/3.png",
                "Assets/monster3/4.png"
            ]

var coinFrame = ["Assets/coin/1.png",
            "Assets/coin/2.png",
            "Assets/coin/3.png",
            "Assets/coin/4.png"
        ]

let background = new PIXI.Sprite.from('Assets/game3Map.png');
let successMsg = new PIXI.Sprite.from('Assets/msg.png')
let failMsg = new PIXI.Sprite.from('Assets/failMsg.png')
let door = new PIXI.Sprite.from('Assets/door.png')
var player = PIXI.AnimatedSprite.fromFrames(playerFrame);
var monster1 = PIXI.AnimatedSprite.fromFrames(monsterFrame1);
var monster2 = PIXI.AnimatedSprite.fromFrames(monsterFrame2);
var monster3 = PIXI.AnimatedSprite.fromFrames(monsterFrame3);
var coin1 = PIXI.AnimatedSprite.fromFrames(coinFrame);
var coin2 = PIXI.AnimatedSprite.fromFrames(coinFrame);
var coin3 = PIXI.AnimatedSprite.fromFrames(coinFrame);
var coin4 = PIXI.AnimatedSprite.fromFrames(coinFrame);

var score = 0
counter1 = 0;
counter2 = 0;
counter3 = 0;
counter4 = 0;
movement = 0

background.width = 704;
background.height = 704;

player.width = 40;
player.height = 40;

monster1.width = 44;
monster1.height = 44;

monster2.width = 44;
monster2.height = 44;

monster3.width = 44;
monster3.height = 44;

coin1.width = 44;
coin1.height = 44;

coin2.width = 44;
coin2.height = 44;

coin3.width = 44;
coin3.height = 44;

coin4.width = 44;
coin4.height = 44;

background.anchor.set(0.5);
player.anchor.set(0.5);
monster1.anchor.set(0.5);
monster2.anchor.set(0.5);
monster3.anchor.set(0.5);
coin1.anchor.set(0.5)
coin2.anchor.set(0.5)
coin3.anchor.set(0.5)
coin4.anchor.set(0.5)
door.anchor.set(0.5)

background.x = 352;
background.y = 352;

player.x = 352;
player.y = 110;

coin1.x = 176;
coin1.y = 154;

coin2.x = 528;
coin2.y = 154;

coin3.x = 176;
coin3.y = 550;

coin4.x = 528;
coin4.y = 550;

monster1.x = 132;
monster1.y = 98;

monster2.x = 132;
monster2.y = 608;

monster3.x = 590;
monster3.y = 608;

app.stage.addChild(background);
app.stage.addChild(player);
app.stage.addChild(monster1);
app.stage.addChild(monster2);
app.stage.addChild(monster3);
app.stage.addChild(coin1);
app.stage.addChild(coin2);
app.stage.addChild(coin3);
app.stage.addChild(coin4);
app.stage.addChild(door);

door.visible = false;

function testForCollision(object1, object2) {
    const bounds1 = object1.getBounds();
    const bounds2 = object2.getBounds();

    return bounds1.x < bounds2.x + bounds2.width
        && bounds1.x + bounds1.width > bounds2.x
        && bounds1.y < bounds2.y + bounds2.height
        && bounds1.y + bounds1.height > bounds2.y;
};

function random()  {
    randomNum = Math.floor(2 * Math.random());
    return randomNum
};

$(document).on("keydown", function(e) {
    if (e.keyCode == 65 && player.x >= 25)    {
        player.play();
        player.direction = "left";
        player.facingDirection = "left"
        player.x -= 44;
        movement += 1;
    }
    else if (e.keyCode == 68 && player.x <= 681)   {
        player.play()
        player.direction = "right"
        player.facingDirection = "right"
        player.x += 44;
        movement += 1;
    }
    else if (e.keyCode == 87 && player.y >= 25)   {
        player.play()
        player.direction = "up"
        player.y -= 44;
        movement += 1;
    }
    else if (e.keyCode == 83 && player.y <= 681)   {
        player.play()
        player.direction = "down"
        player.y += 44;
        movement += 1;
    }
    else    {
        player.stop()
        player.direction = "none"
    }
});

app.ticker.add(function(){
    player.animationSpeed = 0.16;
    if (testForCollision(player, coin1) == true && counter1 == 0){
        coin1.visible = false;
        score += 1;
        counter1 = 1;
    };
    if (testForCollision(player, coin2) == true && counter2 == 0){
        coin2.visible = false;
        score += 1;
        counter2 = 1;
    };
    if (testForCollision(player, coin3) == true && counter3 == 0){
        coin3.visible = false;
        score += 1;
        counter3 = 1;
    };
    if (testForCollision(player, coin4) == true && counter4 == 0){
        coin4.visible = false;
        score += 1;
        counter4 = 1;
    };
    if (score == 4){

    };

    if(movement % 5 == 0 && movement != 0){
        if(random() == 0)   {
            if(monster1.x < player.x)   {
                monster1.x += 44
                movement += 1;
            };
            if(monster2.x < player.x)   {
                monster2.x += 44
                movement += 1;
            };
            if(monster3.x < player.x)   {
                monster3.x += 44
                movement += 1;
            };
    
            if(monster1.x > player.x)   {
                monster1.x -= 44
                movement += 1;
            };
            if(monster2.x > player.x)   {
                monster2.x -= 44
                movement += 1;
            };
            if(monster3.x > player.x)   {
                monster3.x -= 44
                movement += 1;
            };
        }
        else{
            if(monster1.y < player.y)   {
                monster1.y += 44
                movement += 1;
            };
            if(monster2.y < player.y)   {
                monster2.y += 44
                movement += 1;
            };
            if(monster3.y < player.y)   {
                monster3.y += 44
                movement += 1;
            };
    
            if(monster1.y > player.y)   {
                monster1.y -= 44
                movement += 1;
            };
            if(monster2.y > player.y)   {
                monster2.y -= 44
                movement += 1;
            };
            if(monster3.y > player.y)   {
                monster3.y -= 44
                movement += 1;
            };
        }
    }
    if(score == 4){
        successMsg.visible = true
        setTimeout(function(){
            window.location.href = "../6-endingScreen"
        }, 200)
    }

    if (testForCollision(player, monster1) == true){
        failMsg.visible = true
        setTimeout(function(){
            window.location.href = "../2-lobby"
        }, 400);
    };

    if (testForCollision(player, monster2) == true){
        failMsg.visible = true
        setTimeout(function(){
            window.location.href = "../2-lobby"
        }, 400);
    };

    if (testForCollision(player, monster3) == true){
        failMsg.visible = true
        setTimeout(function(){
            window.location.href = "../2-lobby"
        }, 400);
    };
});