const app = new PIXI.Application({
    width: 800, 
    height: 700,
    backgroundColor: 0x1099bb,
    resolution: window.devicePixelRatio || 1
});

document.body.appendChild(app.view);

let dot1 = PIXI.Sprite.from('Assets/dot1.png');
let dot2 = PIXI.Sprite.from('Assets/dot2.png');
let dot3 = PIXI.Sprite.from('Assets/dot3.png');
let dot4 = PIXI.Sprite.from('Assets/dot4.png');
let dot5 = PIXI.Sprite.from('Assets/dot5.png');

dot1.anchor.set(0.5);
dot2.anchor.set(0.5);
dot3.anchor.set(0.5);
dot4.anchor.set(0.5);
dot5.anchor.set(0.5);

dot1.x = 100;
dot1.y = 80;
dot2.x = 220;
dot2.y = 80;
dot3.x = 340;
dot3.y = 80;
dot4.x = 460;
dot4.y = 80;
dot5.x = 580;
dot5.y = 80;


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


app.stage.addChild(dot1);
app.stage.addChild(dot2);
app.stage.addChild(dot3);
app.stage.addChild(dot4);
app.stage.addChild(dot5);

randomNum = Math.floor(5 * Math.random());
point = 0;
console.log("Your button to pick is", randomNum + 1);

dot1.on("click", function(){
    console.log('0');
    if (randomNum == 0){
        point++
        console.log("you've scored a point, your current amount of point is " + point);
    }   else    {
        point--
        console.log("you've lost a point, your current amount of point is " + point);
    };
    randomNum = Math.floor(5 * Math.random());
    console.log("Your button to pick is ", randomNum + 1);
});

dot2.on("click",function(){
    console.log('1');
    if (randomNum == 1) {
        point++
        console.log("you've scored a point, your current amount of point is " + point);
    }   else    {
        point--
        console.log("you've lost a point, your current amount of point is " + point);
    };
    randomNum = Math.floor(5 * Math.random());
    console.log("Your button to pick is ", randomNum + 1);
});

dot3.on("click",function(){
    console.log('2');
    if (randomNum == 2) {
        point++
        console.log("you've scored a point, your current amount of point is " + point);
    }   else    {
        point--
        console.log("you've lost a point, your current amount of point is " + point);
    };
    randomNum = Math.floor(5 * Math.random());
    console.log("Your button to pick is ", randomNum + 1);
});

dot4.on("click",function(){
    console.log('3');
    if (randomNum == 3) {
        point++
        console.log("you've scored a point, your current amount of point is " + point);
    }   else    {
        point--
        console.log("you've lost a point, your current amount of point is " + point);
    };
    randomNum = Math.floor(5 * Math.random());
    console.log("Your button to pick is ", randomNum + 1);
});

dot5.on("click",function(){
    console.log('4');
    if (randomNum == 4) {
        point++
        console.log("you've scored a point, your current amount of point is " + point);
    }   else    {
        point--
        console.log("you've lost a point, your current amount of point is " + point);
    };
    randomNum = Math.floor(5 * Math.random());
    console.log("Your button to pick is ", randomNum + 1);
});
