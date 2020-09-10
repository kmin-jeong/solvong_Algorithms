#include <iostream>

using namespace std;

bool check[10];
int ans[10];

void go(int index, int n, int m) {

	if (index == m) {
		for (int i = 0; i <m; i++) {
			cout << ans[i] << ' ';
		}
		cout << '\n';
		return;
	}
	for (int i = 1; i <= n; i++) {
		if (check[i] == true) continue;
		check[i] = true;
		ans[index] = i;
		go(index + 1, n, m);
		check[i] = false;
	}
}

int main()
{

	int n, m;
	cin >> n >> m;

	go(0, n, m);

	return 0;
}
 
