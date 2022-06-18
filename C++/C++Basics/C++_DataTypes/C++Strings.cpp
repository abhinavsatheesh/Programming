#include <iostream>
#include <string>

using namespace std;

int main() {
	string Name, Place, Date;
	cout << "Enter your name";
	getline(cin, Name);
	cout << "Enter the place where you were born";
	getline(cin, Place);
	cout << "Enter the date when you were born";
	getline(cin, Date);
	cout << "Hello, " << Name << ". You were born in " << Place << " on " << Date;
}
	