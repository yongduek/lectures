float r = 0;
float theta = 0;
float t = 0.0;

void setup() {
  size(500, 500);
  background(255);
}

void draw() {
  float noisevalue = noise(t);
  float x = noisevalue*(r * cos(theta));
  float y = noisevalue*(r * sin(theta));

  noStroke();
  fill(0);
  ellipse(x+width/2, y+height/2, 3, 3); 

  theta += 0.035;

  r += 0.15;
  
  t += 0.01;

  println(noisevalue);
}
