/*
문제: 백준 1486 등산
유형: Floyd Warshall
노트: -
*/
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <queue>
#include <utility>

using namespace std;

int n, m, t, d;
char board[25][25];
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

bool isOutOfIndex(int x, int y) {
    if (x < 0 || y < 0 || y >= n || x >= m) return true;
    return false;
}

int getValue(char ch) {
    if ('A' <= ch && ch <= 'Z')
        return ch - 'A';
    
    if ('a' <= ch && ch <= 'z') 
        return ch - 'a' + 26;
    
    return -1;
}

vector<vector<int> > up() {
    vector<vector<int> > v(n, vector<int> (m, 2100000000));
    v[0][0] = 0;

    queue<pair<int, int> > q;
    q.push(make_pair(0, 0));


    while (!q.empty()) {
        pair<int, int> cur = q.front();
        q.pop();

        for (int i = 0; i < 4; i++) {
            int x = cur.second + dx[i];
            int y = cur.first + dy[i];
            if (isOutOfIndex(x, y)) continue;
            
            int next_val = getValue(board[y][x]);
            int cur_val = getValue(board[cur.first][cur.second]);
            if (abs(next_val - cur_val) > t) continue;
            
            int w;
            if (cur_val < next_val)  w = (next_val - cur_val) * (next_val - cur_val);
            else  w = 1;

            if (v[y][x] > v[cur.first][cur.second] + w) {
                q.push(make_pair(y, x));
                v[y][x] = v[cur.first][cur.second] + w;
            }


        }
    }

    return v;
}

vector<vector<int> > down() {
    vector<vector<int> > v(n, vector<int> (m, 2100000000));
    v[0][0] = 0;

    queue<pair<int, int> > q;
    q.push(make_pair(0, 0));


    while (!q.empty()) {
        pair<int, int> cur = q.front();
        q.pop();

        for (int i = 0; i < 4; i++) {
            int x = cur.second + dx[i];
            int y = cur.first + dy[i];
            if (isOutOfIndex(x, y)) continue;
            
            int next_val = getValue(board[y][x]);
            int cur_val = getValue(board[cur.first][cur.second]);
            if (abs(next_val - cur_val) > t) continue;
            
            int w;
            if (cur_val > next_val)  w = (next_val - cur_val) * (next_val - cur_val);
            else  w = 1;

            if (v[y][x] > v[cur.first][cur.second] + w) {
                q.push(make_pair(y, x));
                v[y][x] = v[cur.first][cur.second] + w;
            }


        }
    }

    return v;
}

int main() {
    cin >> n >> m >> t >> d;
    for (int i = 0; i < n; i++) {
        cin >> board[i];
    }

    vector<vector<int> > uu = up();
    vector<vector<int> > dd = down();
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (uu[i][j] == 2100000000 || dd[i][j] == 2100000000) continue;
            uu[i][j] += dd[i][j];
        }
    }

    int max_val = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (uu[i][j] <= d) {
                max_val = max(max_val, getValue(board[i][j]));
            }
        }
    }
    
    cout << max_val;

    return 0;
}