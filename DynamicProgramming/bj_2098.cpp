/*
백준 2098 (골드1)
외판원 순회
dp
*/

#include <iostream>
#include <vector>
#define MAX 2100000000
using namespace std;

int n;
int w[17][17];
int dp[17][1 << 17];

// dp[i][j] = 
// 현재 도시가 i, 방문한 도시들 j (2진수) 일 때,
// 방문하지 않은 도시들을 모두 방문 후 출발 도시로 돌아올 때 드는 최소 비용

int tsp(int visit, int now) {

    // 현재 도시를 방문 했다고 체크
    visit |= (1 << now); // 1을 now 만큼 이동

    // 모든 도시를 방문한 경우
    if (visit == (1 << n) - 1) {
        // now -> 출발(0) 경로가 있어야 순환 생성
        if (w[now][0] > 0) {
            return w[now][0];
        }
        // 순환 생성 못할 경우
        return MAX;
    }

    int& ret = dp[now][visit];
    if (ret > 0) {
        return ret;
    }

    ret = MAX;
    for (int i = 0; i < n; i++) {
        // 다음 방문 노드
        if (i != now && ((visit & (1 << i)) == 0) && w[now][i] > 0) {
            // 있을 경우 최소 비용 갱신
            int temp = tsp(visit, i) + w[now][i];
            if (ret > temp)
                ret = temp;
        }
    }

    return ret;

}

int main() {

    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> w[i][j];
        }
    }

    int ans = tsp(0, 0);
    if (ans == MAX) cout << -1;
    else cout << ans;

    return 0;
}