
color c = color(255, 255, 0);

void setup() {
  size(800, 800);
  background(255);
  frameRate (5);
}

float ll = 600;
float angle = 0;
float dangle = PI / 8;

void draw() {
  if (ll <= 2) return;
  translate(width/2, height/2);
  rotate (angle);
  rectDraw(0, 0, ll);
  ll = ll*0.99;
  angle += dangle;
}

void rectDraw(float x, float y, float l) {
  fill (c);
  beginShape();
  vertex(x, y);
  vertex(x, y+l);
  vertex(x+l, y+l);
  vertex(x+l, y);
  endShape(CLOSE);
}
