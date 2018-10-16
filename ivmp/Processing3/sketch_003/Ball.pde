class Ball {
  float x, y;
  color c;
  float g=9.8; // meter / sec^2
  float vy;
  float diam;
  Ball(float xx, float yy, color cc) {
    x = xx; y = yy; c=cc;
    vy = 0;
    diam = 10;
  }
  void move() {
    y = y + vy + 0.5 * g;
  }
  void draw() {
    ellipseMode (CENTER);
    ellipse (x,y, diam, diam);
  }
}
