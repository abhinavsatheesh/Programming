//Program to find out the total marks recieved in a subject and its Percentage
#include <iostream>
#include <string>

using namespace std;

int main() {
	double sciencemarks, socialmarks, mathsmarks, englishmarks, hindimarks, sanskritmarks, totalmarks, TOTAL, PERCENTAGE;
	cout << "Enter the marks recieved for Science";
	cin >> sciencemarks;
	cout << "Enter the marks recieved for Social";
	cin >> socialmarks;
	cout << "Enter the marks recieved for Maths";
	cin >> mathsmarks;
	cout << "Enter the marks recieved for English";
	cin >> englishmarks;
	cout << "Enter the marks recieved for Hindi";
	cin >> hindimarks;
	cout << "Enter the marks recieved for Sanskrit";
	cin >> sanskritmarks;
	cout << "Enter the total marks for an exam";
	cin >> totalmarks;
	TOTAL = sciencemarks + socialmarks + mathsmarks + englishmarks + hindimarks + sanskritmarks;
	PERCENTAGE = (TOTAL/totalmarks)*100;
	cout << "Your total marks in exams is " << TOTAL;
	cout << "\nYour mark percentage in exams is " << PERCENTAGE << " % ";
}
