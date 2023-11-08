#include <iostream>
#include <string>

using namespace std;

int main() {
	int side1, side2, side3, side4;
	int base_1, base_2, height;
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
	cout << "Perimeter of the Trapezium is " << perimeter << " cm";
	cout << "\nEnter the length of Base 1";
	cin >> base_1;
	cout << "Enter the length of Base 2";
	cin >> base_2;
	cout << "Enter the height of Trapezium";
	cin >> height;
	area = 0.5*height*(base_1+base_2);
	cout << "Area of the Trapezium is " << area << " sq.cm.";
}