#include <iostream>
#include <string>
#include <math.h>

using namespace std;

int main() {
	int radius, height;
	double tsa, lsa, c, a;
	double PI = atan(1)*4;
	cout << "Enter the Radius";
	cin >> radius;
	cout << "Enter the Height";
	cin >> height;
	c = 2*PI*radius;
	a = PI*pow(radius, 2);
	tsa = 2*PI*radius*(radius+height);
	lsa = 2*PI*radius*height;
	cout << "Perimeter of the Bottom Circle is " << c << " cm";
	cout << "\nArea of the Bottom Circle is " << a << " sq.cm.";
	cout << "\nTotal Surface Area of the Cylinder is " << tsa;
	cout << "\nLateral Surface Area of the Cylinder is " << lsa;
}