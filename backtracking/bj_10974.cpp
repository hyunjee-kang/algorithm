/*
백준 10974 (실버3)
모든 순열
실버3
*/

#include <iostream>
#include <vector>

using namespace std;

int n;
vector<vector<int> > answer;
int visit[10];


void dfs(vector<int> v) {
    if (v.size() == n) {
        answer.push_back(v);
        return;
    }

    for (int i = 1; i <= n; i++) {
        if (visit[i] == 1) continue;
        v.push_back(i);
        visit[i] = 1;
        dfs(v);
        v.pop_back();
        visit[i] = 0;
    }
}

int main() {


    cin >> n;

    
    for (int i = 1; i <= n; i++) {
        vector<int> v;
        v.push_back(i);
        visit[i] = 1;
        dfs(v);
        visit[i] = 0;
    }

    for (int i = 0; i < answer.size(); i++) {
        for (int j = 0; j < n; j++) {
            cout << answer[i][j] << " ";
        }
        cout << "\n";
    }

    return 0;
}