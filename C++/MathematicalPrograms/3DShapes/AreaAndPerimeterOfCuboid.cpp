#include <iostream>
#include <string>

using namespace std;

int main() {
	int Length, Breadth, Height;
	double perimeter, tsa, lsa;
	cout << "Enter a Length measure";
	cin >> Length;
	cout << "Enter a Breadth measure";
	cin >> Breadth;
	cout << "Enter a Height measure";
	cin >> Height;
	perimeter = 4*(Length+Breadth+Height);
	tsa = 2*((Length*Breadth)+(Length*Breadth)+(Breadth*Height));
	lsa = 2*Height*(Length+Breadth);
	cout << "Perimeter of the Cuboid is " << perimeter << " cm";
	cout << "\nTotal Surface Area of the Cuboid is " << tsa << " sq.cm.";
	cout << "\nLateral Surface Area of the Cuboid is " << lsa << " sq.cm.";
}