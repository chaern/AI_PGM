#include <iostream>
using namespace std; 

int bigger(int a, int b) {
	if (a > b) return a;
	else return b;
}

bool dividedBy3(int n) {
	if (n % 3 == 0) return true;
	else return false;
}

int main() {
	int a, b, n;
	cout << "두개의 정수 입력>>";
	cin >> a >> b;
	n = bigger(a, b);
		cout << a << "중" << b << "중 큰 값은" << n << "입니다.\n";
	if (dividedBy3(n))
		cout << n << "은" << "3의 배수입니다.\n";
	else
		cout << n << "은" << "3의 배수가 아닙니다.\n";
}