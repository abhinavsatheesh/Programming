#include <iostream>
#include <string>

using namespace std;

int main() {
	int side1, side2, side3, side4;
	int d, h1, h2, dss, hss;
	double area, perimeter;
	cout << "Enter the length of 1st Side";
	cin >> side1;
	cout << "Enter the length of 2nd Side";
	cin >> side2;
	cout << "Enter the length of 3rd Side";
	cin >> side3;
	cout << "Enter the length of 4th Side";
	cin >> side4;
	perimeter = side1+side2+side3+side4;
	cout << "Perimeter of the Quadrilateral is " << perimeter;
	cout << "\nEnter the length of Diagonal";
	cin >> d;
	cout << "Enter the 1st Altitude";
	cin >> h1;
	cout << "Enter the 2nd Altitude";
	cin >> h2;
	dss = d/2;
	hss = h1+h2;
	area = dss*hss;
	cout << "Area of the Quadrilateral is " << area;
}