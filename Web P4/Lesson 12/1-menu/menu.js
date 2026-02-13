const app = new PIXI.Application({
    width: 700,
    height: 700,
    resolution: window.devicePixelRatio || 1
});

const style = new PIXI.TextStyle({
    fillGradientType: 1,
    fontFamily: "pixelText",
    fontSize: 150,
    fontWeight: "bolder"
});

localStorage.clear()

document.body.appendChild(app.view);
let background = new PIXI.TilingSprite.from('assets/background.png', {width: 700, height: 700});
let startButton = PIXI.Sprite.from("assets/startButton.png")


bgm = PIXI.sound.Sound.from("assets/song1.mp3")
bgm.play({
    loop: true
});

var title = new PIXI.Text("RPG", style)
var start = new PIXI.Text("Start", style)
var blurFilter = new PIXI.filters.BlurFilter();
var blurCounter = 0;
var blurSpeed = 0;

background.anchor.set(0.5);
title.anchor.set(0.5)
startButton.anchor.set(0.5)

background.x = 350;
background.y = 350;
title.x = 350
title.y = 230
startButton.x = 350
startButton.y = 478

app.stage.addChild(background);
app.stage.addChild(title);
app.stage.addChild(startButton);

startButton.interactive = true;
startButton.buttonMode = true;

app.ticker.add(function(){
    background.tilePosition.x += 2;
})

startButton.on("click", function(){
    background.filters = [blurFilter];
    title.filters = [blurFilter]
    startButton.filters = [blurFilter]

    while(blurCounter < 15) {
        setTimeout(function(){
            blurSpeed += 0.05
            blurFilter.blur = blurSpeed * blurCounter;
        }, 100)
        blurCounter += 1
    }

    setTimeout(function(){
        window.location.href = "../2-lobby"
    }, 200)
})