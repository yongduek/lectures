PImage im;

void setup() {
  size (800, 500);
  smooth();
  im = loadImage ("data/mountain.jpg");
  println (im.width);
}

void draw() {
  background (250);
  
  pushMatrix(); // scaled image
      scale (0.9 * width/float(im.width));
      image (im, 0, 0);
  popMatrix();
  
  pushMatrix(); // rotate a scaled image at the ceter of the canvas
      translate(width/2, height/2);
      scale (0.2);
      rotate (TWO_PI/15000 * millis());
      translate (-im.width/2, -im.height/2);
      image (im, 0, 0);
  popMatrix();

  translate(width/2, height/2); // put a mark at the canvas center
  ellipseMode(CENTER);
  ellipse(0,0, 30, 10);
}
