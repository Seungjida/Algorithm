#include <iostream>
#include <stack>
#include <string>

using namespace std;

char OPEN = '(';
char CLOSE = ')';

int main(int argc, char* argv[]){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        stack<int> stk;
        string parenthesis;
        cin >> parenthesis;

        bool isVps = true;

        for (int j = 0; j < parenthesis.length(); j++) {
            if (parenthesis[j] == OPEN) {
                stk.push(parenthesis[j]);
            }
            else if (parenthesis[j] == CLOSE) {
                if (stk.empty()) {
                    isVps = false;
                    break;
                }
                else {
                    stk.pop();
                }
            }
        }
        if (stk.empty() && isVps) {
            cout << "YES" << '\n';
        }
        else {
            cout << "NO" << '\n';
            int size = stk.size();
            for (int k = 0; k < size; k++) {
                stk.pop();
            }
        }
    }
    return 0;
}