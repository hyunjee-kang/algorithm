/*
백준 1707 (골드4)
이분 그래프
dfs, bfs
*** 이분 그래프 판별은 bfs, dfs로 한다는 것을 기억하자! ***
*/

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int K;
int V, E;

bool bfs(vector<vector<int> > &graph, int* color, int start) {
    queue <int> q;
    q.push(start);
    color[start] = 1;

    while (!q.empty()) {
        int cur = q.front();
        q.pop();

        for (vector<int>::iterator i = graph[cur].begin(); i != graph[cur].end(); i++) {
            if (color[*i] == 0) {
                q.push(*i);
                color[*i] = color[cur] * (-1);

            } else if (color[*i] * (-1) == color[cur]) {
                continue;
                
            } else {
                return false;
            }
        }
    }

    return true;
}

int main() {

    cin >> K;
    while (K--) {
        cin >> V >> E;

        int a = 1, b = 1;
        vector<vector<int> > graph(V + 1);
        int color[20001] = {0};

        for (int i = 0; i < E; i++) {
            cin >> a >> b;
            graph[a].push_back(b);
            graph[b].push_back(a);
        }
        
        bool isBipartite = true;
        for (int i = 1; i <= V; i++) {
            if (graph[i].size() > 0 && color[i] == 0) {
                isBipartite = bfs(graph, color, i);
                if (!isBipartite) break;
            }
        }

        if (isBipartite) 
            cout << "YES\n";
        else 
            cout << "NO\n";
    }

    return 0;
}