// Bar object here has a unit shape.
// The purpose of this code is 
//   1. to learn geometric transformations
//   2. millis()
//   3. control of period of sin/cos in the unit of millis.

Bar bar = new Bar(1,1); // basic shape
PVector b1 = new PVector(80, 100); // size of first bar
PVector b2 = new PVector(30, 170); // size of second bar
PVector b3 = new PVector(15, 220);

float joint1 = 0, joint2 = 0;

void setup() {
  size (800, 800);
  frameRate (120);
}

void draw() {
  background (128);
  
  // draw axes
  drawAxes (width, height);

  translate (width/2, height*.8);
  rotate (PI);
  
  pushMatrix(); // robot arm
    // first bar at the bottom
    pushMatrix();
      translate (-b1.x/2, 0);
      scale (b1.x, b1.y);
      bar.draw(255,255,0);
    popMatrix();
    // draw base axes, appear at the top of the bar
    drawAxes (400,height);
    
    translate (0, b1.y);
    rotate (radians(joint1)); // first joint
    
    // second bar
    pushMatrix();
      translate (-b2.x/2, 0);
      scale (b2.x, b2.y);
      bar.draw(120, 180, 255);
    popMatrix();
    drawAxes (200,400);
    
    translate (0, b2.y);
    rotate (radians(joint2)); // second joint
    
    // third bar
    pushMatrix();
      translate (-b3.x/2, 0);
      scale (b3.x, b3.y);
      bar.draw(155, 180, 120);
    popMatrix();
    drawAxes(200,400);

  popMatrix();
  
  // angle update in degrees
  joint1 = sin (millis()*PI*2/10000) * 30;
  joint2 = cos (millis()*PI*2/20000) * 60;
}


class Bar {
  float w, h;
  
  Bar (float ww, float hh) { 
    w = ww; 
    h = hh;
  }

  void draw(float r, float g, float b) {
    noStroke();
    fill (r,g,b);
    beginShape();
    vertex (0, 0);
    vertex (0, h);
    vertex (w, h);
    vertex (w, 0);
    endShape(CLOSE);
  }
}

void drawAxes (float w, float h) {
  pushMatrix();
      stroke (255, 0, 0);
      line (-w/2, 0, w/2, 0); // x-axis
      stroke (0, 255, 0); // y-axis
      line (0, -h/2, 0, h/2);
      ellipseMode (CENTER);
      ellipse (w/3, 0, 5, 5);
      ellipse (0, h/3, 5, 5);
  popMatrix();
}
