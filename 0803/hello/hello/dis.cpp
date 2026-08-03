#include<iostream>

using namespace std;

int main() {
	string name [3] = {"12345", "abcd", "qwer"};
	int stdNum[3] = { 0,1,2 };
	for (int i = 0; i < 3; i++)
	{
		cin >> name[i] >> stdNum[i];
	}
	for (int i = 0; i < 3; i++)
	{
		cout << "name = " << name[i] << ", stdNumber = " << stdNum[i] << endl;
	}
	
}

