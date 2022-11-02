/*
백준 1182 (실버2)
부분수열의 합
백트래킹
*/

#include <iostream>
#include <vector>

using namespace std;

int n, s;
int answer;
vector<int> v;
bool isOk = false;

void dfs(int idx, int sum) {
    if (isOk && sum == s) {
        answer += 1;
    }

    isOk = true;
    for (int i = idx; i < n; i++) {
        dfs(i + 1, sum + v[i]);
    }
}

int main() {

    cin >> n >> s;
    int tmp;
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        v.push_back(tmp); 
    }

    dfs(0, 0);

    cout << answer;

    return 0;
}