// Change & observe
//   strokeWeight
//   step size (from 10 to e.g. 20)
//   stroke 
float strokeN = 0;
void setup(){
  size(400,400);
  strokeWeight(2);
}

void draw(){
  background(255);
  Line1(0, 0, 10, height, strokeN);
  Line2(0, height, width, height-10, strokeN);
  Line3(width, height, width-10, 0, strokeN);
  Line4(width, 0, 0, 10, strokeN);
}

void Line1(float x1, float y1, 
            float x2, float y2, float S){
  stroke(S);
  line(x1, y1, x2, y2); 
  if(x2 < width){
    Line1(x1, y1+10, x2+10, y2,S+10);
  }
}

void Line2(float x1, float y1, 
            float x2, float y2, float S){
  stroke(S);
  line(x1, y1, x2, y2); 
  if(x1 < width){
    Line2(x1+10, y1, x2, y2 - 10,S+10);
  }
}

void Line3(float x1, float y1, 
            float x2, float y2, float S){
  stroke(S);
  line(x1, y1, x2, y2); 
  if(x2 > 0){
    Line3(x1, y1-10, x2-10, y2,S+10);
  }
}

void Line4(float x1, float y1, 
            float x2, float y2, float S){
  stroke(S);
  line(x1, y1, x2, y2);
  if(y2 < height){
    Line4(x1-10, y1, x2, y2+10,S+10);
  }
}
