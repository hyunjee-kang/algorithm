/*
백준 22352 (골드5)
항체 인식
dfs, bfs
*/

#include <iostream>
using namespace std;

int N, M;
int map_old[31][31];
int map_new[31][31];
int visit[31][31];
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
int err = 0;

bool isOutOfIndex(int c, int r) {
    if (0 <= c && c < N && 0 <= r && r < M) 
        return false;
    return true;
}

void dfs(int c, int r, int check) {
    visit[c][r] = check;

    for (int i = 0; i < 4; i++) {
        if (isOutOfIndex(c + dy[i], r + dx[i]))
            continue;
        if (visit[c + dy[i]][r + dx[i]] != 0)
            continue;
        if (map_old[c][r] == map_old[c + dy[i]][r + dx[i]] && map_new[c][r] == map_new[c + dy[i]][r + dx[i]])  
            dfs(c + dy[i], r + dx[i], check);
        if (map_old[c][r] == map_old[c + dy[i]][r + dx[i]] && map_new[c][r] != map_new[c + dy[i]][r + dx[i]]) {
            err = -1;
            return;
        }
    }
}

int main() {

    cin >> N >> M;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> map_old[i][j]; 
        }
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> map_new[i][j]; 
        }
    }

    int val = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (map_old[i][j] != map_new[i][j] && visit[i][j] == 0) {
                dfs(i, j, ++val);
            }
            if (err == -1) {
               cout << "NO\n";
               return 0;
            }
        }
    }

    if (val <= 1) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }

    return 0;
}