#include <iostream>
#include <string>

using namespace std;

int main() {
	int diagonal1, diagonal2;
	int side;
	double area, perimeter;
	cout << "Enter the length of Diagonal 1";
	cin >> diagonal1;
	cout << "Enter the length of Diagonal 2";
	cin >> diagonal2;
	area = 0.5*diagonal1*diagonal2;
	cout << "Area of Rhombus is " << area << " sq.cm.";
	cout << "\nEnter the side of the Rhombus";
	cin >> side;
	perimeter = 4*side;
	cout << "Perimeter of the Rhombus is " << perimeter << " cm";
}