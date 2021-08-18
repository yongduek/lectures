// Using Java LinkedList

import java.util.* ;

LinkedList<Bar> ll = new LinkedList<Bar>();

void setup() {
  size (600, 400);
  ll.add (new Bar(10, 50));
  ll.add (new Bar(40, 20));
}

void draw() {  
  for (int i = 0; i < ll.size(); i++) {
    ll.get(i).h += random(-10, 10);
    if (ll.get(i).h < 1) ll.get(i).h = 7;
  }

  for (Bar bar : ll) {
    bar.w += random(-5, 5);
    if (bar.w < 1) bar.w = 10;
  }


  for (Bar bar : ll) {
    translate (random(width), random(height));
    bar.draw();
  }

  if (random(1) < 0.5)
    ll.addLast (new Bar(random(20), random(20)));

  if (random(1) < 0.5 && ll.size() > 0)
    ll.removeFirst();

  println (ll.size());
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
