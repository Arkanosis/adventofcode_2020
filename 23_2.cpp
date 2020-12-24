#include <iostream>
#include <vector>

int cups_count = 1000000;
int moves_count = 10000000;

struct Cup {
  int label;
  int next;
};

int offset(int label) {
  static const int offsets[] = {
    // example
    // 3,
    // 4,
    // 0,
    // 6,
    // 5,
    // 7,
    // 8,
    // 1,
    // 2,
    // actual
    0,
    8,
    4,
    6,
    1,
    7,
    5,
    2,
    3,
  };
  if (label > 9) {
    return label - 1;
  }
  return offsets[label - 1];
}

int main() {
  std::vector<Cup> cups = {
    // example
    // {3, 1},
    // {8, 2},
    // {9, 3},
    // {1, 4},
    // {2, 5},
    // {5, 6},
    // {4, 7},
    // {6, 8},
    // {7, 9},
    // actual
    {1, 1},
    {5, 2},
    {8, 3},
    {9, 4},
    {3, 5},
    {7, 6},
    {4, 7},
    {6, 8},
    {2, 9},
  };
  cups.reserve(cups_count);
  for (int label = 10;
       label <= cups_count;
       ++label) {
    cups.emplace_back(Cup{label, label});
  }
  cups.back().next = 0;
  int current = 0;
  for (int move = 1;
       move <= moves_count;
       ++move) {
    // std::cout << "-- move " << move << " --" << std::endl;
    // std::cout << "cups: (" << cups[current].label << ")";
    // int next = current;
    // for (int cup = 1;
    // 	 cup < cups_count;
    // 	 ++cup) {
    //   next = cups[next].next;
    //   std::cout << " " << cups[next].label;
    // }
    // std::cout << std::endl;
    int first = cups[current].next;
    int second = cups[first].next;
    int third = cups[second].next;
    cups[current].next = cups[third].next;
    int destination = cups[current].label - 1;
    if (!destination) {
      destination = cups_count;
    }
    while (destination == cups[first].label ||
	   destination == cups[second].label ||
	   destination == cups[third].label) {
      --destination;
      if (!destination) {
	destination = cups_count;
      }
    }
    // std::cout << "destination: " << destination << std::endl;
    auto& before = cups[offset(destination)];
    cups[third].next = before.next;
    before.next = first;
    current = cups[current].next;
  }

  // current = offset(1);
  // for (int cup = 1;
  //      cup < 9;
  //      ++cup) {
  //   current = cups[current].next;
  //   std::cout << cups[current].label << std::endl;
  // }

  int first = cups[offset(1)].next;
  int second = cups[first].next;
  std::cout << long(cups[first].label) * long(cups[second].label) << std::endl;
}
