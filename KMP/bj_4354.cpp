/*
백준 4354 문자열 제곱
KMP
*/

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<int> makeTable(string s) {
    vector<int> table(s.size(), 0);
    
    int j = 0;
    for (int i = 1; i < s.size(); i++) {
        while (j > 0 && s[i] != s[j])
            j = table[j - 1];
        if (s[i] == s[j])
            table[i] = ++j;
    }
    return table;
}

int main() {

    while (true) {
        string s;
        cin >> s;
        if (s == ".") break;
        
        vector<int> table = makeTable(s);

        int tmp = s.size() - table[s.size() - 1];
        if (s.size() % tmp == 0) cout << s.size() / tmp << endl;
        else cout << 1 << endl;
    }

    return 0;
}