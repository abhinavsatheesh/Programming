#include <iostream>
#include <string>
using namespace std;

int main() {
  string nameper;
  string classdiv;
  string school;
  cout << "Enter your name";
  getline (cin, nameper);
  cout << "Enter your class and division";
  getline (cin, classdiv);
  cout << "Enter your school";
  getline (cin, school);
  cout << "Your name is " << nameper << ". Your class and division is " << classdiv << ". Your school is " << school;
  return 0;
}
