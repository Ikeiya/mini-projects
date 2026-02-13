const app = new PIXI.Application({
    width: 700,
    height: 700,
    resolution: window.devicePixelRatio || 1
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

player.width = 40;
player.height = 40;

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