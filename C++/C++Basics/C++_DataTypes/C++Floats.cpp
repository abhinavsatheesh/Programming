#include <iostream>
#include <string>
#include <typeinfo>

using namespace std;

int main() {
	float f1 = 0.5;
	cout << "Your number " << f1 << " is of type " << typeid(f1).name();
	float f2 = 1.5;
	cout << "\nYour number " << f2 << " is of type " << typeid(f2).name();
	float f3 = 2.5;
	cout << "\nYour number " << f3 << " is of type " << typeid(f3).name();
	float f4 = 3.5;
	cout << "\nYour number " << f4 << " is of type " << typeid(f4).name();
}