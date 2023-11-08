#include <iostream>
#include <string>

using namespace std;

int main() {
	int heightincm;
	double heightininches;
	double heightinfoot;
	cout << "Enter your height";
	cin >> heightincm;
	heightininches = heightincm/2.54;
	heightinfoot = heightincm/30.48;	
	cout << "Height in inches = " << heightininches << ". Height in feet = " << heightinfoot;
}	