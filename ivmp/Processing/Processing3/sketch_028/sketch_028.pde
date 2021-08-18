PImage img;

void setup() {
  size(600, 600);
  img = loadImage("../data/sunflower.png");
  imgProc();
}

void draw() {
  image (img, 0, 0);
  step();
}

void imgProc () {
  img.loadPixels();
  for (int y = img.height/2; y < img.height; y++) {
    for (int x = 0; x < img.width; x++) {
      int loc = x + y*img.width;
      // Image Processing Algorithm would go here
      float r = red (img.pixels [loc]);
      float g = green(img.pixels[loc]);
      float b = blue (img.pixels[loc]);
      // Image Processing would go here
      // Set the display pixel to the image pixel
      img.pixels[loc] = color(255-r, 255-g, 255-b);
    }
  }
  img.updatePixels();
}

int pos = 0;
void step () {
  img.loadPixels();
  for (int x = 0; x < img.width; x++) {
    int loc = x + pos * img.width;
    img.pixels[loc] = 0xFF000000 + (0xFFFFFFFF - img.pixels[loc]);
  }
  img.updatePixels();
  pos++;
  if (pos >= img.height) pos = 0;
}
