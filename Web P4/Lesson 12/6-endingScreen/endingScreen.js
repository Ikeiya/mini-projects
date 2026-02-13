const app = new PIXI.Application({
    width: 700,
    height: 700,
    resolution: window.devicePixelRatio || 1
});

const style = new PIXI.TextStyle({
    fillGradientType: 1,
    fontFamily: "pixelText",
    fontSize: 50,
    fontWeight: "bolder"
});

bgm = PIXI.sound.Sound.from("assets/song6.mp3")
bgm.play({
    loop: true
});

document.body.appendChild(app.view);
let background = new PIXI.TilingSprite.from('Assets/background.png', {width: 700, height: 700});
var title = new PIXI.Text("RPG\n\n\nThank you for playing\n\n\nCredits:\n\n\n\nCode:Lacus Lee, Google,\nRobocode demo code\n\n\nOther stuff: Lacus Lee", style)
var blurFilter = new PIXI.filters.BlurFilter();
var blurCounter = 0;
var blurSpeed = 0;

background.anchor.set(0.5);
title.anchor.set(0.5)

background.x = 350;
background.y = 350;
title.x = 350
title.y = 1200

app.stage.addChild(background);
app.stage.addChild(title);

app.ticker.add(function(){
    background.tilePosition.x += 2;
    title.y -= 3
})
