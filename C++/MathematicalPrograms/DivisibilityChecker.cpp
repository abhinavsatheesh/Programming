//Program to check whether a number is divisible by a number or not
#include <iostream>
#include <string>

using namespace std;

int main() {
	int num1;
	int num2;
	cout << "Enter a number";
	cin >> num1;
	cout << "Enter a number by which we should check if " << num1 << " is divisible";
	cin >> num2;
	if (num1 % num2 == 0) {
		 cout << "Your number " << num1 << " is divisible by " << num2;
	}
	else {
		cout << "Your number " << num1 << " is not divisible by " << num2;
	}
}
	