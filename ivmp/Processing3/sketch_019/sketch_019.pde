// A rotating Bar with scale change at the center of window

float angle = 0;
float scale;

Bar bar = new Bar(180, 25);

void setup() {
  size (600, 400);
}

void draw() {  
  scale = 2 + cos (radians(angle)); // scale = [1, 3]
 
  fill (0,120,200);
  pushMatrix();
  translate (width/2, height/2);
  rotate (radians(angle));
  scale (scale);
  translate (-bar.w/2, -bar.h/2);
  bar.draw();
  popMatrix();

  fill (55,0,0);
  ellipseMode (CENTER);
  ellipse (width/2, height/2, 10,10);

  angle += 10;
}


class Bar {
  float w, h;

  Bar (float ww, float hh) { 
    w = ww; 
    h = hh;
  }

  void draw() {
    beginShape();
    vertex (0, 0);
    vertex (w, 0);
    vertex (w, h);
    vertex (0, h);
    endShape(CLOSE);
  }
}
