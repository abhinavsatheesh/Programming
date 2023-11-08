#include <iostream>
#include <string>
#include <math.h>

using namespace std;

int main() {
	int radius, height;
	double volume;
	double PI = atan(1)*4;
	cout << "Enter the Radius";
	cin >> radius;
	cout << "Enter the Height";
	cin >> height;
	volume = PI*pow(radius, 2)*height;
	cout << "Volume of the Cylinder is " << volume;
}