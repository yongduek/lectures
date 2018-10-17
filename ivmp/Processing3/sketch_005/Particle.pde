class Particle {
  public float x, y, vx, vy;
  float g = 9.8/15;
  public color c;
  public float diam;
  public Boolean bye = false;
  public int countdown = 10 + int(random(10));
  
  Particle (int xx, int yy, color cc) { x = xx; y = yy; c = cc; }
  Particle (float xx, float yy) {
    x = xx; y = yy;
    vx = vy = 0;
    c = color(random(255), random(25), random(25));
    diam = random (5, 10);
  }

  Particle (float xx, float yy, float vvx, float vvy) {
    x = xx; y = yy;
    vx = vvx; vy = vvy;
    c = color(random(255), random(25), random(25));
    diam = random (5, 10);
  }
 
  void draw() {
    noStroke();
    fill (c);
    ellipseMode (CENTER);
    ellipse (x,y, diam, diam);
  }
  
  void move() {
    x = x + vx;
    y = y + vy + 0.5*g;
    vy = vy + g;
    
    countdown = countdown - 1;
  }
  
  Boolean move(float ww, float wh) {
    move();
    if (y - diam/2 > wh) { bye = true; }
    return bye;
  }
  
  Boolean bye() { return bye; }
  int countdown() { return countdown; }
  void setColor(color cc) { c=cc; }
  void setDiam(float d) { diam=d; }
}
