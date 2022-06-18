#include <iostream>
#include <string>

using namespace std;

int main() {
	int number;
	cout << "Enter a number between 2 and 10";
	cin >> number;
	if (number>10 || number<2) {
		cout << "This is a number off limits. Retry again.";
	}
	else {
		if (number%2 == 0 && number>2) {
			cout << number << " is not a Prime Number";
		}
		else if (number%3 == 0 && number!=3) {
			cout << number << " is a Prime Number";
		}
		else {
			cout << number << " is a Prime Number";
		}
	}
}
			
		