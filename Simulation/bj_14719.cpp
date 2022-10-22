/*
백준 14719 (골드5)
빗물
simulation
*/

#include <iostream>
#include <queue>
using namespace std;

int h, w;
int block[501];

int getRain() {
    queue<int> q;
    int pole = block[0];
    int tall = 0;
    int rain = 0;
    for (int i = 1; i < w; i++) {
        if (pole > block[i]) {
            q.push(block[i]);
            if (tall < block[i]) 
                tall = block[i];

        } else if (pole <= block[i]) {
            while (!q.empty()) {
                rain += (pole - q.front());
                q.pop();
            }
            pole = block[i];

        } else if (block[i] > 0 && i == w - 1) {
            while (!q.empty()) {
                rain += (block[i] - q.front());
                cout << " ~~ ";
                cout << q.front() << " ";
                q.pop();
            }
        }

        cout << "\n";
    }

    return rain;
}

int main() {

    cin >> h >> w;
    for (int i = 0; i < w; i++) {
        cin >> block[i];
    }

    cout << getRain();

    return 0;
}