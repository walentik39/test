#include <iostream>
using namespace :: std;

bool isEven(int n)
{
	return (n % 2 == 0);
}
int main()
{
	int n;
	cin >> n;
	isEven(n) ? cout << "Even": cout << "Odd" << '\n';

	return 0;
}
