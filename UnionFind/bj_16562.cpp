/*
백준 16562 (골드4)
친구비
union-find
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, m, k;
int answer;
vector<int> price(1, 0);
vector<int> parent(1, 0);

int find(int x) {
    if (parent[x] == x)
        return x;
    return parent[x] = find(parent[x]);
}

void merge(int a, int b) {
    a = find(a);
    b = find(b);
    if (price[a] > price[b]) {
        price[a] = price[b];
        parent[a] = b;
    } else {
        price[b] = price[a];
        parent[b] = a;
    }
}

void make_friends() {
    for (int i = 1; i <= n; i++) {
        if (k < 0) return;
        if (parent[i] == i) {
            k -= price[i];
            answer += price[i];
        }
    }
}

int main() {

    cin >> n >> m >> k;
    int tmp;
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        price.push_back(tmp);
        parent.push_back(i + 1);
    }

    int a, b;
    for (int i = 0; i < m; i++) {
        cin >> a >> b; 
        merge(a, b);
    }

    for (int i = 1; i <= n; i++) {
        cout << parent[i] << " ";
    }
    cout << "\n";
    for (int i = 1; i <= n; i++) {
        cout << price[i] << " ";
    }
    cout << "\n";

    make_friends();
    if (k < 0) {
        cout << "Oh no";
    } else {
        cout << answer;
    }

    return 0;
}