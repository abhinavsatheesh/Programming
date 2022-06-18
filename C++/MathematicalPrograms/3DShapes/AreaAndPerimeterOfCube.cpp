#include <iostream>
#include <string>
#include <math.h>

using namespace std;

int main() {
	int side;
	double tsa, lsa;
	cout << "Enter the side of the cube";
	cin >> side;
	tsa = 6*pow(side, 2);
	lsa = 4*pow(side, 2);
	cout << "Total Surface Area of Cube is " << tsa;
	cout << "\nLateral Surface Area of Cube is " << lsa;
}