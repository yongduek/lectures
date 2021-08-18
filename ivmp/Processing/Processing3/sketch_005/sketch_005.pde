Firework f; // declare an instance name f
Boolean stop = false;

void setup() {
  size (1300, 700);
  f = new Firework(width, height); // allocate & init
}

void draw() {
    background (1);
    if (!stop) { f.draw(); }
}


void keyPressed() {
  stop = !stop;
}
