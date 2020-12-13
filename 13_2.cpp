#include <iostream>

struct Line {
  int id;
  int delta;
};

int main() {
  Line lines[] = {
    { 383, -31 },
    { 41, 10 },
    { 37, -37 },
    { 29, -2 },
    { 23, -23 },
    { 19, -50 },
    { 17, 17 },
    { 13, -18 }
  };

  for (long t = 0;
       ;
       t += 457) {
    for (Line line: lines) {
      if ((t + line.delta) % line.id) {
	goto bad;
      }
    }
    std::cout << t - 50 << std::endl;
    return 0;
  bad:;
  }
}
