/*
백준 16991 (골드1)
외판원 순회3
dp
*/

#include <iostream>
#include <cmath>
using namespace std;

int n;
int w[17][2];
double dp[17][1 << 17];

double getDistance(int a, int b) {
    return abs( sqrt( pow((w[a][0] - w[b][0]), 2) + pow((w[a][1] - w[b][1]), 2) ) ); 
}

double tsp(int visit, int now) {
    visit |= (1 << now);

    if (visit == (1 << n) - 1) {
        return getDistance(now, 0);
    }

    double& ret = dp[now][visit];
    if (ret > 0) {
        return ret;
    }

    ret = 2100000000;
    for (int i = 0; i < n; i++) {
        if (i != now && (visit & (1 << i)) == 0) {
            double tmp = tsp(visit, i) + getDistance(i, now);
            if (ret > tmp) {
                ret = tmp;
            }
        }
    }

    return ret;
}

int main() {

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> w[i][0] >> w[i][1]; 
    }

    double ans = tsp(0, 0);
    cout << ans;

    return 0;
}