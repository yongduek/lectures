Ball ball;

void setup() {
  size (200,400);
  ball = new Ball(100, 20, color(100, 120, 250));
}

void draw() {
  ball.draw();
  ball.move();
}
