#include <iostream>
#include <string>
#include <math.h>

using namespace std;

int main() {
	string answer;
	int side;
	int ba, height;
	int volume;
	cout << "Do you wish to find the Volume of Cube by 2D Method or via Side Method? Please enter either 2D or Side";
	getline(cin, answer);
	if (answer == "2D") {
		cout << "OK.";
		cout << "\nEnter the Base Area of the Cube";
		cin >> ba;
		cout << "Enter a Height measure";
		cin >> height;
		volume = ba*height;
		cout << "Volume of the Cube is " << volume;
	}
	else if (answer == "Side") {
		cout << "OK.";
		cout << "\nEnter the measure of the Side";
		cin >> side;
		volume = pow(side, 3);
		cout << "Volume of the Cube is " << volume;
	}
	else {
		exit(0);
	}
}