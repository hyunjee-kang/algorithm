/*
문제: 백준 1956 운동
유형: Floyd Warshall
노트: 기본 유형
*/
#include <iostream>
#include <vector>

using namespace std;

int v, e;
int MAX = 2100000000;

int main() {
    ios::sync_with_stdio(false); cin.tie(0);

    cin >> v >> e;
    vector<vector<int> > board(v+1, vector<int> (v+1, MAX));
    for (int i = 0; i <= v; i++) {
        board[i][i] = 0;
    }

    int a, b, c;
    for (int i = 0; i < e; i++) {
        cin >> a >> b >> c;
        board[a][b] = c;
    }

    for (int k = 1; k <= v; k++) {
        for (int i = 1; i <= v; i++) {
            for (int j = 1; j <= v; j++) {
                if (board[i][k] == MAX || board[k][j] == MAX) continue;
                board[i][j] = min(board[i][j], board[i][k] + board[k][j]);
            }
        }   
    }
    
    int min_val = MAX;
    for(int i = 1; i <= v ; i++) {
        for (int j = 1; j <= v; j++) {
            if (board[i][j] == MAX || board[j][i] == MAX || i == j) continue;
            min_val = min(board[i][j] + board[j][i], min_val);
        }
    }

    if (min_val == MAX) cout << -1;
    else cout << min_val;

    return 0;
}