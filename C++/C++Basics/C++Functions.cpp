#include <iostream>
#include <string>

using namespace std;

void completereturn(string name, string job) {
	cout << "Hello " << name << ". Your job is " << job;
}

int main() {
	string Name, Job;
	cout << "May I know your name?";
	getline(cin, Name);
	cout << "May I know your job?";
	getline(cin, Job);
	completereturn(Name, Job);
}