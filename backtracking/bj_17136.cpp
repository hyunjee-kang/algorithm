/*
백준 2023 (골드2)
색종이 붙이기
백트래킹
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int> > v(10, vector<int> (10, 0));
vector<int> paper(5, 5);
int answer = 2100000000;

bool can_attach(int x, int y, int size) {
    for (int i = 0; i <= size; i++) {
        for (int j = 0; j <= size; j++) {
            if (v[y + i][x + j] == 0) return false; 
        }
    }
    return true;
}

void update(int x, int y, int size, int is_attach) {
    for (int i = 0; i <= size; i++) {
        for (int j = 0; j <= size; j++) {
            v[y + i][x + j] = is_attach;
        }
    }
}

void dfs(int x, int y, int attached_cnt) {
    while (v[y][x] == 0) {
        if (10 <= ++x) {
            if (10 <= ++y) {
                answer = min(answer, attached_cnt);
                return;
            }
            x = 0;
        }
    }

    if (answer <= attached_cnt) return;

    for (int i = 4; i >= 0; i--) {
        if (10 <= y + i || 10 <= x + i || paper[i] == 0) continue;
        if (can_attach(x, y, i)) {
            update(x, y, i, 0);
            paper[i] -= 1;

            dfs(x, y, attached_cnt + 1);

            update(x, y, i, 1);
            paper[i] += 1;
        } 
    }
}

int main() {

    int total = 0;
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            cin >> v[i][j];
            if (v[i][j] == 1) total +=1; 
        }
    }

    if (total == 100) cout << 4;
    else if (total == 0) cout << 0;
    else {
        dfs(0, 0, 0);
        if (answer == 2100000000) cout << -1;
        else cout << answer;
    }

    return 0;
}