const app = new PIXI.Application({
    width: 704,
    height: 704,
    resolution: window.devicePixelRatio || 1
});

document.body.appendChild(app.view);
win = false;
mousePos = 0;
originalX = 0;
originalY = 0
counter = 0

array = [null, null, null, null];

var background = new PIXI.Sprite.from("Assets/background.png")

var puzzle1 = new PIXI.Sprite.from("Assets/Puzzle/1.png")
var puzzle2 = new PIXI.Sprite.from("Assets/Puzzle/2.png")
var puzzle3 = new PIXI.Sprite.from("Assets/Puzzle/3.png")
var puzzle4 = new PIXI.Sprite.from("Assets/Puzzle/4.png")
var msg = new PIXI.Sprite.from("Assets/msg.png")

background.height = 704;
background.width = 704;

background.anchor.set(0.5);
puzzle1.anchor.set(0.5);
puzzle2.anchor.set(0.5);
puzzle3.anchor.set(0.5);
puzzle4.anchor.set(0.5);
msg.anchor.set(0.5);

background.x = 352;
background.y = 352;

puzzle1.x = 88;
puzzle1.y = 88;

puzzle2.x = 618;
puzzle2.y = 88;

puzzle3.x = 88;
puzzle3.y = 618;

puzzle4.x = 618;
puzzle4.y = 618;

msg.x = 352;
msg.y = 352;

msg.visible = false

app.stage.addChild(background);
app.stage.addChild(puzzle1);
app.stage.addChild(puzzle2);
app.stage.addChild(puzzle3);
app.stage.addChild(puzzle4);
app.stage.addChild(msg)

puzzle1.interactive = true;
puzzle1.buttonMode = true;

puzzle2.interactive = true;
puzzle2.buttonMode = true;

puzzle3.interactive = true;
puzzle3.buttonMode = true;

puzzle4.interactive = true;
puzzle4.buttonMode = true;

puzzle1.mouseData = null;
puzzle1.selected = false;
puzzle1.snapped = 0;

puzzle2.mouseData = null;
puzzle2.selected = false;
puzzle2.snapped = 0;

puzzle3.mouseData = null;
puzzle3.selected = false;
puzzle3.snapped = 0;

puzzle4.mouseData = null;
puzzle4.selected = false;
puzzle4.snapped = 0;

function initialRotation() {
    return rotation = 2*(Math.floor(Math.random() * 3));
};

function changeDirection() {
    if (this.snapped && !win && originalX == this.x && originalY == this.y)    {
        if (this.texture.rotate == 6){
            this.texture.rotate = 0
        }   else   {
            this.texture.rotate += 2
        };
    };
};

function dragStart(e) {
    if(!win) {
        this.mouseData = e.data;
        this.alpha = 0.5;
        this.selected = true;
        this.snapped = 0;
        mousePos = this.mouseData.getLocalPosition(app.stage);
    }

    if (counter == 0)   {
        originalX = this.x;
        originalY = this.y;
        counter = 1;
    }
};

function dragMove(){
    if (this.selected && !win){
        mousePos = this.mouseData.getLocalPosition(app.stage);
        this.x = mousePos.x;
        this.y = mousePos.y;
    };
    
};

function dragStop(){
    counter = 0
    if (!win) {
        if (176 <= mousePos.x && mousePos.x <= 352 && 176 <= mousePos.y && mousePos.y <= 352) {
            this.x = 264;
            this.y = 264;
            this.snapped = 1;
        }   else if (176 <= mousePos.x && mousePos.x <= 352 && 352 <= mousePos.y && mousePos.y <= 528)  {
            this.x = 264;
            this.y = 440;
            this.snapped = 2;
        }   else if (352 <= mousePos.x && mousePos.x <= 528 && 176 <= mousePos.y && mousePos.y <= 352)  {
            this.x = 440;
            this.y = 264;
            this.snapped = 3;
        }   else if (352 <= mousePos.x && mousePos.x <= 528 && 352 <= mousePos.y && mousePos.y <= 528)  {
            this.x = 440;
            this.y = 440;
            this.snapped = 4;
        };
    }
    this.selected = false
    this.alpha = 1;
};

puzzle1.texture.rotate = initialRotation()
puzzle2.texture.rotate = initialRotation()
puzzle3.texture.rotate = initialRotation()
puzzle4.texture.rotate = initialRotation()

puzzle1.on("click", changeDirection)
puzzle2.on("click", changeDirection)
puzzle3.on("click", changeDirection)
puzzle4.on("click", changeDirection)

puzzle1.on("mousedown", dragStart)
puzzle2.on("mousedown", dragStart)
puzzle3.on("mousedown", dragStart)
puzzle4.on("mousedown", dragStart)

puzzle1.on("mousemove", dragMove)
puzzle2.on("mousemove", dragMove)
puzzle3.on("mousemove", dragMove)
puzzle4.on("mousemove", dragMove)

puzzle1.on("mouseup", dragStop)
puzzle2.on("mouseup", dragStop)
puzzle3.on("mouseup", dragStop)
puzzle4.on("mouseup", dragStop)

app.ticker.add(function(){
    if(puzzle1.snapped == 4 && puzzle2.snapped == 2 && puzzle3.snapped == 3 && puzzle4.snapped == 1)    {
        if(puzzle1.texture.rotate == 0 && puzzle2.texture.rotate == 0 && puzzle3.texture.rotate == 0 && puzzle4.texture.rotate == 0){
            win = true;
            msg.visible = true;
            setTimeout(function(){
                window.location.href = "../2-lobby"
            }, 1000)
        }
    }
});