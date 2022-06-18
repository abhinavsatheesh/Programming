#include <iostream>
#include <string>
#include <math.h>

using namespace std;

int main() {
	double num1, num2, num3, num4;
	double square1, squareroot2, cube3, cuberoot4;
	cout << "Enter a number";
	cin >> num1;
	cout << "Enter another number";
	cin >> num2;
	cout << "Enter another number";
	cin >> num3;
	cout << "Enter another number";
	cin >> num4;
	square1 = pow(num1, 2);
	squareroot2 = sqrt(num2);
	cube3 = pow(num3, 3);
	cuberoot4 = cbrt(num4);
	cout << "The square of number "<< num1 << " is " << square1 << ". The square root of " << num2 << " is " << squareroot2 << ". The cube of number " << num3 << " is " << cube3 << ". The cube root of " << num4 << " is " << cuberoot4;
}