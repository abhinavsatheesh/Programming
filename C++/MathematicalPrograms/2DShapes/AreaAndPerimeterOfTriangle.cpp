//Program to find Area of Triangle
#include <iostream>
#include <string>

using namespace std;

int main() {
	int side1, side2, side3;
	int breadth, height;
	double area, perimeter;
	cout << "Enter the length of 1st Side";
	cin >> side1;
	cout << "Enter the length of 2nd Side";
	cin >> side2;
	cout << "Enter the length of 3rd Side";
	cin >> side3;
	perimeter = side1+side2+side3;
	cout << "Perimeter of the Triangle is " << perimeter << " cm";
	cout << "\nEnter the breadth";
	cin >> breadth;
	cout << "Enter the height";
	cin >> height;
	area = 0.5*breadth*height;
	cout << "Area of the Triangle is " << area;
}