//want to fix shaun/grass overlapping each other (ex. shaun over shaun)

let canvasWidth = 400;
let canvasHeight = 400;
let cellWidth = 100;
let cellHeight = 100;


function setup() {
  createCanvas(canvasWidth, canvasHeight);
  noLoop();
  background("green");
}

function draw() {
  function drawGrass(x, y){
  stroke('lightgreen');
  strokeWeight(2);
  line(x-5, y, x, y+10);
  line(x+10, y, x+10, y+10);
  line(x+25, y, x+20, y+10);
}
  
  function drawShaun(x, y){
    //legs
    for (let i = 0; i < 2; i++){
      fill("black");
      noStroke();
      rect((x+25*i), y+20, 5, 20);
      rect((x+25*i)+10, y+20, 5, 20);
    }
    
    //body
    for (let i=0; i<3; i++){
      fill("white");
      noStroke();
      ellipse(x+20*i, y, 30);
    }
    for (let i=0; i<2; i++){
      fill("white");
      noStroke();
      ellipse((x+10)+20*i, y+15, 30);
    }
    
    //tail
    fill("white");
    noStroke();
    ellipse(x+55, y+12, 15, 25);
    
    //face
    fill("black");
    ellipse(x-10, y+5, 20, 30)
    
    //ears
    fill("black");
    ellipse(x-25, y, 15, 5)
    ellipse(x+5, y, 15, 5)
    
    //hair
    for (let i=0; i<2; i++){
      fill("white");
      noStroke();
      ellipse((x-13)+7*i, y-7, 10)
    }
    
  }

    //grass
    for (let i=0; i<10; i++){
      grassX = random(20, canvasWidth - 50);
      grassY = random(20, canvasHeight - 50);
      drawGrass(grassX, grassY);
    }
  
    //shaun
    for (let i=0; i<3; i++){
      shaunX = random(20, canvasWidth - 100);
      shaunY = random(20, canvasHeight - 50);
      drawShaun(shaunX, shaunY);
    }
}