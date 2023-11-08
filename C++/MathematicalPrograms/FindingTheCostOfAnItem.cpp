//Finding the total cost of the item if quantity and price is given
#include <iostream>
#include <string>

using namespace std;

int main() {
	string itemname;
	int weight;
	int baseprice;
	int finalprice;
	cout << "Enter the name of the Item";
	getline(cin, itemname);
	cout << "Enter the quantity of the Item. Enter in Kilograms";
	cin >> weight;
	cout << "Enter the base price of the Item";
	cin >> baseprice;
	finalprice = baseprice*weight;
	cout << "Total Price for the item " << itemname << " is Rs. " << finalprice;
}