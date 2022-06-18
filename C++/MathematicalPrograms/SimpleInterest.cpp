#include <iostream>
#include <string>

using namespace std;

int main() {
	int principal, time, rateofinterest;
	cout << "Enter the Principal Amount";
	cin >> principal;
	cout << "Enter the Time in Years";
	cin >> time;
	cout << "Enter the Rate of Interest";
	cin >> rateofinterest;
	int simpleinterest = principal*time*rateofinterest;
	int amount = simpleinterest+principal;
	cout << "Simple Interest is " << simpleinterest << " Rupees. Total Amount is " << amount << " Rupees";
}
	