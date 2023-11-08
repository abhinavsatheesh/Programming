//Program to find Area and Perimeter of Rectangle
#include <iostream>
#include <string>

using namespace std;

int main() {
	int Length, Breadth;
	double area, perimeter;
	cout << "Enter a Length measure";
	cin >> Length;
	cout << "Enter a Breadth measure";
	cin >> Breadth;
	area = Length*Breadth;
	perimeter = 2*(Length+Breadth);
	cout << "Perimter = " << perimeter << " cm";
	cout << "\nArea = " << area << " sq.cm.";
}