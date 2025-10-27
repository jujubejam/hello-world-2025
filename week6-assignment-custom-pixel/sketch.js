let capture;

function setup() {
  createCanvas(640, 480);
  capture = createCapture(VIDEO);
  capture.hide();
  pixelDensity(1);
  rectMode(CENTER);
  noStroke;
}

function draw() {
  background("white");
  fill(255);

  translate(width, 0);
  scale(-1, 1);

  capture.loadPixels();

  let pixelSize = 30;
  for(let i = 0; i < capture.height; i += pixelSize){
    for(let j = 0; j < capture.width; j += pixelSize){
      let offset = (i * capture.width + j) * 4;
      let xpos = (j / capture.width) * width;
      let ypos = (i / capture.height) * height;
      let c = color(
        capture.pixels[offset],
        capture.pixels[offset + 1],
        capture.pixels[offset + 2],
        capture.pixels[offset + 3]
      );
      fill(c);
      textSize(28);
      // strokeWeight(0.5);

      push();
      translate(xpos, ypos);
      scale(-1, 1);
      text('칸', 0, 0);
      pop();
    }
  }
}
