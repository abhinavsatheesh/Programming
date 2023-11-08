#include <iostream>
#include <math.h>
#include <string>

using namespace std;

int main() {
	double PI = atan(1)*4;
	double radius;
	cout << "Enter the Radius";
	cin >> radius;
	double area = PI*radius*radius;
	double perimeter = 2*PI*radius;
	cout << "Area = " << area;
	cout << "\nPerimeter = " << perimeter;
}