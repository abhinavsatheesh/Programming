#include <iostream>
#include <string>

using namespace std;

int main() {
	string answer;
	int ba, height;
	double length3D, breadth3D, height3D;
	int volume;
	cout << "Do you wish to find the Volume of Cuboid by 2D Method or via 3D Method? Please enter either 2D or 3D";
	getline(cin, answer);
	if (answer == "2D") {
		cout << "OK.";
		cout << "\nEnter the Base Area of the Cube";
		cin >> ba;
		cout << "Enter a Height measure";
		cin >> height;
		volume = ba*height;
		cout << "Volume of the Cuboid is " << volume;
	}
	else if (answer == "3D") {
		cout << "OK.";
	    cout << "\nEnter a Length measure";
		cin >> length3D;
		cout << "Enter a Breadth measure";
		cin >> breadth3D;
		cout << "Enter a Height measure";
		cin >> height3D;
		volume = length3D*breadth3D*height3D;
		cout << "Volume of the Cuboid is " << volume;
	}
	else {
		exit(0);
	}
}