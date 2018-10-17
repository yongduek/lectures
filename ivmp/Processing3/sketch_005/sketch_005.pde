Firework f;
Boolean stop = false;

void setup() {
  size (300, 700);
  f = new Firework(width, height);
}

void draw() {
  if (!stop) {
      background (1);
      f.draw();
  }
}


void keyPressed() {
  stop = !stop;
}
