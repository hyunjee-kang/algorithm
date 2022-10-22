/*
백준 11722 (실버2)
가장 긴 감소하는 부분 수열
dp
*/

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int n;
    vector <int> v;
    vector <int> dp;
    int ans = 1;

    cin >> n;
    int a;
    for (int i = 0; i < n; i++) {
        cin >> a;
        v.push_back(a);
        dp.push_back(1);
    }

    for (int i = 1; i < n; i++) {
        for (int j = i - 1; j >= 0; j--) {
            if (v[j] > v[i]) {
                dp[i] = max(dp[i], 1 + dp[j]);
                ans = max(dp[i], ans);
            } 
        }
    }

    cout << ans << "\n";

    return 0;
}