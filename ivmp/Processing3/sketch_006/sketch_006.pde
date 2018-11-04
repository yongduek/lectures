
PImage im; // Processing Image Class

void setup () {
  size (300, 300);
  im = loadImage ("data/Frog-Man2.jpg");
}

float radian = 0;
float rstep = PI / 100;

void draw () {
  // image at the center
  image (im, width/2 - im.width/10/2, 0, im.width/10, im.height/10);
  
  pushMatrix();
    translate (width/4, height*2/3.);
    rotate (radian);
    image (im, 0, 0, im.width/10, im.height/10);
  popMatrix();
  
  pushMatrix();
    translate (width*3/4., height*2/3.);
    rotate (radian);
    scale (0.2); // scale's pin point is the origin
    translate (-im.width/2, -im.height/2);
    image (im, 0, 0);
  popMatrix();
  
  radian += rstep;
}
