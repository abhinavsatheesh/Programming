#include <iostream>
#include <string>

using namespace std;

int main() {
	string nameper;
	int ageper;
	string professionper;
	int retiringage;
	int yearsleft;
	cout << "Enter your name";
	getline(cin, nameper);
	cout << "Enter your age";
	cin >> ageper;
	cin.clear();
	cin.sync();
	cout << "Enter your profession";
	getline(cin, professionper);
	cout << "Enter your retiring age";
	cin >> retiringage;
	yearsleft = retiringage - ageper;
	cout << "Hello " << nameper << ". Your age is " << ageper << ". Your profession is " << professionper << ". You will have to retire from " << professionper << " in " << yearsleft << " years";
}