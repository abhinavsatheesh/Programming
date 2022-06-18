#include <iostream>
#include <string>
#include <math.h>

using namespace std;

int main() {
	int side;
	double area, perimeter;
	cout << "Enter the Side measure";
	cin >> side;
	area = pow(side, 2);
	perimeter = 4*side;
	cout << "Area = " << area << " sq.cm.";
	cout << "\nPerimeter = " << perimeter << " cm";
}