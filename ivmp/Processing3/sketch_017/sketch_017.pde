float r = 75;
float theta = 0;

void setup() {
  size(600, 600);
  background(255);
  frameRate(120);
  smooth();
}
void draw() {
  // Polar to Cartesian conversion
  float t = noise(theta);

  float x = r * cos(t * PI / 2);
  float y = r * sin(t * PI / 2);
  // Draw an ellipse at x,y
  noStroke();
  fill(0);
  ellipse(x, y, 3, 3); // Adjust for center of window
  // Increment the angle
  theta += 0.01;
  r += 0.11;
}
