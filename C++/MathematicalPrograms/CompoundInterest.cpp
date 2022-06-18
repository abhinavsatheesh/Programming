#include <iostream>
#include <string>
#include <math.h>
#include <stdio.h>
 
using namespace std;

int main() {
	double principal, rateofinterest, time, rate2, rate1, amount, ci;
	cout << "Enter the Principal Amount";
	cin >> principal;
	cout << "Enter the Rate of Interest in Numbers";
	cin >> rateofinterest;
	cout << "Enter the Time in Years";
    cin >> time;
	rate1 = 1+(rateofinterest/100);
	rate2 = pow(rate1, time);
	amount = principal*rate2;
	ci = amount-principal;
	cout << "Compound Interest is " << ci;
	cout << "\nFinal Amount is " << amount;
}