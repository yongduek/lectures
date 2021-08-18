size(200, 200);

// Before we deal with pixels
loadPixels();

// Loop through every pixel
for (int i = 0; i < pixels.length; i++) {
  // Pick a random number, 0 to 255
  float rand = random(0xFF);
  // We can get the length of the pixels array just like with any array.
  // Create a grayscale color based on random number
  color c = color(rand, random(255), random(255));
  // Set pixel at that location to random color
  pixels[i] = c;
}

// a red box at (30,40) of size (50, 60);
for (int y = 40; y < 40 + 60; y++) {
  for (int x = 30; x < 30+50; x++) {
    int loc = (x + y * width);
    pixels[loc] = #FF0000;
  }
}

// When we are finished dealing with pixels
updatePixels();
// EOF //
