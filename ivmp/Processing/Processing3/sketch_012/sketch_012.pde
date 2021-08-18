void setup() {   
  size(400, 400);
  frameRate (1);
  strokeWeight(2);
}   

void draw() {   
  background(255);  
  branch1(width/2, height, 100);
  branch2(width/2, 0, 100);
}

void branch1(float x, float y, float h) {
  stroke (random(255), random(255), 0);
  line(x, y, x-h, y-h);
  line(x, y, x+h, y-h);
  if (h > 1) {
    branch1(x-h, y-h, h/2);
    branch1(x+h, y-h, h/2);
  }
}

void branch2(float x, float y, float h) {
  stroke (0, random(255), random(255));
  line(x, y, x-h, y+h);
  line(x, y, x+h, y+h);
  if (h > 1) {
    branch2(x-h, y+h, h/2);
    branch2(x+h, y+h, h/2);
  }
}
