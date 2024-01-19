#include <iostream>
using namespace std;

void pattern(int x) {
	char currChar = 'a';
	
	for (int i=1 ; i <= x ; i *= 2) {
		for (int j=1 ; j<=i ; ++j) {
			cout << currChar << " ";
			currChar = currChar == 'z' ? 'a' : currChar + 1;
		}
		cout << "+" << endl;
	}
}

int main() {
	int x, y;
	
	cin >> x ;
	
	if (x <= 0 || (x & (x-1)) != 0) {
		cout << "gagal";
	} else {
		pattern(x);
	}
	return 0;
}


