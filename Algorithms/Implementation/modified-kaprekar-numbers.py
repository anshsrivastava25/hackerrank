#include <bits/stdc++.h>
using namespace std;

bool isKaprekar(long long n) {
    long long square = n * n;

    // Count digits of n
    int d = to_string(n).length();

    // 10^d
    long long power = 1;
    for (int i = 0; i < d; i++) {
        power *= 10;
    }

    // Split square into left and right parts
    long long right = square % power;
    long long left = square / power;

    return (left + right == n);
}

int main() {
    long long p, q;
    cin >> p >> q;

    bool found = false;

    for (long long n = p; n <= q; n++) {
        if (isKaprekar(n)) {
            cout << n << " ";
            found = true;
        }
    }

    if (!found) {
        cout << "INVALID RANGE";
    }

    return 0;
}
