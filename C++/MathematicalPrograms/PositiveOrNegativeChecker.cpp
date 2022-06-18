//Program to check whether a number is Postitive or Negative
#include <iostream>
#include <string>

using namespace std;

int main() {
	int num;
	cout << "Enter a number";
	cin >> num;
	if (num > 0) {
		cout << "Your number " << num << " is positive";
	}
	else {
		cout << "Your number " << num << " is negative";
	}
}