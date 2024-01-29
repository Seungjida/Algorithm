#include <iostream>
#include <queue>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // 중요도와 넣은 순서가 들어가 있는 큐
    queue<pair<int, int>> q;
    // 중요도에 따라 정렬되어 있는 큐
    priority_queue<int> pq;

    int test_case;
    cin >> test_case;

    for (int t = 0; t < test_case; t++) {
        int n, m;
        cin >> n >> m;

        int priority;

        for (int i = 0; i < n; i++) {
            cin >> priority;

            q.push({ priority, i });
            pq.push(priority);
        }

        int nth_print = 0;
        int index;

        while (!q.empty()) {
            priority = q.front().first;
            index = q.front().second;
            q.pop();

            if (pq.top() == priority) {
                pq.pop();
                nth_print++;
                if (m == index) {
                    cout << nth_print << '\n';
                    break;
                }
            }
            else {
                q.push({ priority, index });
            }
        }

        while(!q.empty()) {
            q.pop();
        }
        while(!pq.empty()) {
            pq.pop();
        }
    }
    return 0;
}