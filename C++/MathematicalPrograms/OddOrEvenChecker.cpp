#include <iostream>
#include <string>

using namespace std;

int main() {
	int num;
	cout << "Enter a number";
	cin >> num;
	if (num%2 == 0) {
		cout << "Your number " << num << " is even";
	}
	else {
		cout << "Your number " << num << " is odd";
	}
}