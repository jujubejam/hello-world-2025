let x = [];
let y = [];

let bodyEasing = [];
let bodyNum = 7;
let easing = 0.1;


let gColor = [];

let randNumber = [];


function setup() {
  createCanvas(720, 480);
  
  //random color of body
  for (let i=0; i<bodyNum; i++){
    gColor[i] = random(120,190);
  }
  
  //randomize size of body
  for (let i=0; i<bodyNum; i++){
    randNumber[i] = random(0.8, 1.0);
  }
  
  //body easing gradually increase
  for (let i=0; i<bodyNum; i++){
    bodyEasing[i] = easing + 0.02 * i
    x[i] = 0;
    y[i] = 0;
  }
  
}

  

function draw() { 
  
  background(214,183,234);
  
  //eat leaf
  noStroke();
  fill("white");
  ellipse(mouseX, mouseY, 30, 30);
  
  
  x[0] += (mouseX - x[0]) * bodyEasing[0];
  y[0] += (mouseY - y[0]) * bodyEasing[0];

  for (let i=1; i< bodyNum; i++){
    x[i] += (x[i-1] - x[i]) * bodyEasing[i];
    y[i] += (y[i-1] - y[i]) * bodyEasing[i];
  }
  
  //body
  for (let i=bodyNum-1; i>=0; i--){
    noStroke();
    fill(1, gColor[i], 1);
    ellipse((x[i]-20)-20*i, y[i], 65, 80*randNumber[i])
  } 
  
  //caterpillar
  push();
  translate(mouseX, mouseY);
  
  //antenna-left
  noStroke();
  fill(129, 70, 149);

  beginShape();
  curveVertex(-10, -30);
  curveVertex(-10, -30);
  
  curveVertex(-15, -70);
  
  curveVertex(-5, -70);
  curveVertex(-5, -70);
  endShape();
  
  //antenna-right
  noStroke();
  fill(129, 70, 149);

  beginShape();
  curveVertex(10, -30);
  curveVertex(10, -30);
  
  curveVertex(15, -70);
  
  curveVertex(5, -70);
  curveVertex(5, -70);
  endShape();
  
  //face
  noStroke();
  fill(179,0,0);
  ellipse(0,0, 60, 75);
  
  //eyes
  stroke(255, 204, 0);
  strokeWeight(3);
  fill("green");
  ellipse(-10,-5, 13, 25);
  ellipse(10,-5, 13, 25);
  
  //mouth
  noStroke();
  fill("black");
  ellipse(0,17,8,8);
  
  pop();
}