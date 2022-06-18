#include <iostream>
#include <string>

using namespace std;
int main() {
	string nameper;
	int ageper;
	cout << "Enter your name";
	getline(cin, nameper);
	cout << "Enter your age";
	cin >> ageper;
	cout << "Hello " << nameper << ". Your age is " << ageper;
}
