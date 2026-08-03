#include<iostream>
#include<cstring>
using namespace std;

int main() {
	char line[100];
	cout << "문자열 입력 :";
	cin.getline(line, 100, '\n');

	int count = 0;
	int i = 0;
	while (line[i] != '\0') {
		if (line[i] == 'e') {
			count++;
		}
		i++;
	}
	cout << "총 글자 수 = " << i << ", 문자 e의 개수 = " << count << "개" << endl;
	return 0;
}