#include <iostream>
#include <stack>
#include<utility>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    stack<pair<int, int>> stk;
    int n;
    cin >> n;

    for (int i = 1; i <= n; i++) {
        int height;
        cin >> height;

        while (!stk.empty()) {
            if (stk.top().first > height) {
                cout << stk.top().second;
                if (i < n) {
                    cout << ' ';
                }
                break;
            }
            else {
                stk.pop();
            }
        }
        if (stk.empty()) {
            cout << 0;
            if (i < n) {
                cout << ' ';
            }
        }

        pair<int, int> element = make_pair(height, i);
        stk.push(element);
    }
    cout << '\n';
    return 0;
}