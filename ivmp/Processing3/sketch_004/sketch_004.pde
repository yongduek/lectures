
ArrayList<Particle> plist = new ArrayList<Particle> ();
ArrayList<Particle> flist = new ArrayList<Particle> ();
Boolean flag_move = false;

void setup() {
  size(640, 480);
   
  println ("plist size = ", plist.size());
  for (int i = 0; i < 50; i++)
    plist.add (new Particle (random(width), random(height)));
  println ("plist size = ", plist.size());
}

void draw() {
  background (1);
  for (Particle pi : plist) { pi.draw(); }
  
  if (flag_move == true) {
    for (int i = 0; i < plist.size(); i++) {
      Particle pi = plist.get(i);
      pi.move(width, height);
      if (pi.bye()) 
        plist.remove(i);
    }
  }
  
  for (int i = flist.size() - 1; i >= 0; i--) {
    Particle f = flist.get(i);
    f.draw();
    f.move();
    if (f.bye() || f.countdown() < 0) flist.remove (i);
  }
} // end draw()

void mousePressed() {
  if (mouseButton == LEFT) {
    make_fire_particles ();
  } else if (mouseButton == RIGHT) {
    flag_move = !flag_move;
  }
}

void make_fire_particles () {
  int N = 13;
  float vmag = 20 + random (10);
  for (int k = 0; k < N; k++) {
    float vx = vmag * cos (TWO_PI / N * k);
    float vy = vmag * sin (TWO_PI / N * k);
    Particle p = new Particle (mouseX, mouseY, vx, vy);
    flist.add (p);
  }
}

// EOF
