/*
백준 2023 (골드5)
신기한 소수
백트래킹, 소수 찾기
*/

#include <iostream>
#include <vector>
using namespace std;

int N;
vector<int> v;

bool isPrime(int num) {
    // 숫자의 루트까지만 확인
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) return false;
    }
    return true;
}

void getSpecial(int number, int depth) {
    if (depth > N) return;
    if (!isPrime(number)) return;

    if (depth == N) {
        v.push_back(number);
    }

    for (int i = 1; i <= 9; i++) {
        getSpecial(number * 10 + i, depth + 1);
    } 
}

int main() {
    cin >> N;

    for(int i = 2; i <= 7; i++) {
        getSpecial(i, 1);
    }
    
    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << endl;
    }

    return 0;
}