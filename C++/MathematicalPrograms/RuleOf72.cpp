#include <iostream>
#include <string>

using namespace std;

int main() {
	int principal, rate, doublerate, doubleprincipal;
	cout << "Enter the Principal Amount";
	cin >> principal;
	cout << "Enter the Rate of Interest";
	cin >> rate;
	doublerate = 72/rate;
	doubleprincipal = 2*principal;
	cout << "Your Principal Amount ₹ " << principal << " will become ₹ " << doubleprincipal << " in "  << doublerate << " years";
}