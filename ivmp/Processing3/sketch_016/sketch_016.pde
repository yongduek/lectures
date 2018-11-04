float theta;
float t;
float ratio = 0.7;

void setup() {
  size(600,400);
  theta = PI/1.8;
  t = height/2;
}

void draw(){
  background(255);
  stroke(0);
  translate(width/2,height);
  line(0,0,0,-t);
  translate(0,-t);
  branch(t);
}

void branch(float h) {
  h = h * ratio;
  if(h > 2) {
      pushMatrix();
      rotate(theta);
      line(0,0,0,-h);
      translate(0,-h);
      branch(h);
      popMatrix();
      
      pushMatrix();
      rotate(-theta);
      line(0,0,0,-h);
      translate(0,-h);
      branch(h);
      popMatrix();
  }
}
