/*
    겹치는 코드 재활용 하는 게 낫지 않나...? 잘 생각해봐!
    string은 switch하려니 복잡하구만
*/
#include <iostream>
#include <queue>
#include <string>

using namespace std;

queue<int> q;

void push() {
    int x;
    cin >> x;

    q.push(x);
}

void front() {
    if (q.empty()) {
        cout << -1 << '\n';
    }
    else {
        cout << q.front() << '\n';
    }
}

void back() {
    if (q.empty()) {
        cout << -1 << '\n';
    }
    else {
        cout << q.back() << '\n';
    }
}

void pop() {
    front();

    if (!q.empty()) {
        q.pop();
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        string command;
        cin >> command;

        if (command == "push") {
            push();
        }
        else if (command == "pop") {
            pop();
        }
        else if (command == "size") {
            cout << q.size() << '\n';
        }
        else if (command == "empty") {
            cout << q.empty() << '\n';
        }
        else if (command == "front") {
            front();
        }
        else if (command == "back") {
            back();
        }
    }
    return 0;
}