#include <iostream>

int main() {
	int v, t, s, d;
	std::cin >> v >> t >> s >> d;

	const int dis_t = t * v;
	const int dis_s = s * v;

	if (dis_t <= d && d <= dis_s) {
		std::cout << "No\n";
	} else {
		std::cout << "Yes\n";
	}
	return 0;
}