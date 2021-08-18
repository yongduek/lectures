
class Firework {
  float wwidth, wheight;
  Particle s;
  Boolean flagS = true; // s is drawn when this is true
  ArrayList<Particle> plist = new ArrayList<Particle>();

  Firework(int ww, int wh) {
    wwidth = ww; 
    wheight = wh;
    s = new Particle(ww/2, wh, 0, -25);
    s.setColor (color(255, 255, 255));
    s.setDiam (5);
  }

  void draw() {
    if (flagS) { s.draw(); }

    for (Particle p : plist) { p.draw(); }
  } // draw

  void move () {
      if (flagS) { s.move(wwidth, wheight); }
  
      for (Particle p : plist) { p.move(wwidth, wheight); }
  
      if (s.vy > -1 && flagS == true) {
          flagS = false;
          // generate firework
          make_fire_particles();
      }
  } // move

  void make_fire_particles () {
    int N = 200;
    float vmag = 20 + random (10);
    float dt = PI/10;
    for (int k = 0; k < N; k++) {
      float vx = vmag * cos (TWO_PI / N * k + random(-dt, dt));
      float vy = vmag * sin (TWO_PI / N * k + random(-dt, dt));
      Particle p = new Particle (s.x, s.y, vx, vy);
      p.diam = random (10, 20);
      plist.add (p);
    }
  }
} // end class
