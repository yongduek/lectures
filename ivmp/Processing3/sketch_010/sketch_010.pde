
float time =0;
float theta = 0;
float increment = 0.01;

void setup() {
  size(500, 500);
  background(255);
  smooth();
}

void draw() {

  //원이 움직일 크기 r을 Perlin Noise 함수로 지정  
  float r = noise(time);  

  //r이 보다 큰 크기로 자연스레 움직이기 위한 Map 함수 지정
  float s = map(r, 0, 1, 0, 200);


  //원을 그릴 벡터 X, 벡터 Y 설정
  float x = s * cos(theta);
  float y = s * sin(theta);

  noFill();
  ellipse(x + width/2, y + height/2, 3, 3);
  theta += 0.01;
  time += increment;
}
