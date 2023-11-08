#include <iostream>
#include <string>
#include <typeinfo>

using namespace std;

int main() {
	int f1 = 0;
	cout << "Your number " << f1 << " is of type " << typeid(f1).name();
	int f2 = 1;
	cout << "\nYour number " << f2 << " is of type " << typeid(f2).name();
	int f3 = 2;
	cout << "\nYour number " << f3 << " is of type " << typeid(f3).name();
	int f4 = 3;
	cout << "\nYour number " << f4 << " is of type " << typeid(f4).name();
}