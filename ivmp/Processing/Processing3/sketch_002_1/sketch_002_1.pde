Car car;

void setup() {
  size (200, 200);
  background (128);
  
  car = new Car();
}

void draw() {
  car.draw(100, 100);
}


class Car {
  Car() {}
  
  void draw (float x0, float y0) {
    //float x0 = 100, y0 = 100; // center of the car
    float cw = 50, ch = 100; // w,h of the car

    // car body
    fill (255, 100, 100);
    rectMode (CENTER); // the rect() is w.r.t center
    rect(x0, y0, cw, ch);

    // now 4 wheels
    float ch4 = ch / 4; 
    float yfront = y0 - ch4; // front wheel
    float xfrontRight = x0 + cw/2;
    fill (0);
    rect (xfrontRight, yfront, 10, 20);

    float xfrontLeft = x0 - cw/2;
    rect (xfrontLeft, yfront, 10, 20);

    float yback = y0 + ch4;
    rect (xfrontRight, yback, 10, 20);
    rect (xfrontLeft, yback, 10, 20);

    return;
  }
}
