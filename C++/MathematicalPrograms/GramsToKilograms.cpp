// Convert grams to kilograms
#include <iostream>
#include <string>

using namespace std;

int main() {
	double grams;
	double kilograms;
	cout << "Enter the Measurement in Grams";
	cin >> grams;
	kilograms = grams/1000;
	cout << "Weight in kilograms = " << kilograms << " kg";
}