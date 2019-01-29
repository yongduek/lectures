float theta = 0;
float delta_i = 0.3; // try different values
float delta_j = 0.3; // try different values

void setup() {
  size(400, 400);
  smooth();
}
void draw() {
  background(100);
  stroke(255);
  // Translate to center of window
  translate(width/2, height/2);
  // Loop from 0 to 360 degrees (2*PI radians)
  for (float i=0; i < TWO_PI; i+=delta_i) {
    // Push, rotate and draw a line!
    pushMatrix();
    rotate(theta+i);
    line(0, 0, 100, 0);
    // Loop from 0 to 360 degrees (2*PI radians)
    for (float j=0; j < TWO_PI; j+=delta_j) {
      // Push, translate, rotate and draw a line!
      pushMatrix();
      translate(100, 0);
      rotate(-theta - j);
      line(0, 0, 50, 0);
      // We're done with the inside loop, pop!
      popMatrix();
    }
    // We're done with the outside loop, pop!
    popMatrix();
  }
  // Increment theta
  theta+=0.01;
}
