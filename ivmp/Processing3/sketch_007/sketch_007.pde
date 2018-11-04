

color c = color(255, 255, 0);

void setup() {
  size(800, 800);
}

void draw() {
  translate(width/2, height/2);
  background(255);
  rectDraw(0, 0, 600);
}

void rectDraw(float x, float y, float l) {
  beginShape();
  vertex(x, y);
  vertex(x, y+l);
  vertex(x+l, y+l);
  vertex(x+l, y);
  endShape(CLOSE);
    
  if ( l>2) {
    rotate(PI/8);
    fill(c);
    rectDraw(x, y, l*0.99);
  }
}
