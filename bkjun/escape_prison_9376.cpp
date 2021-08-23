#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < n; ++i)
#define REP(i, n) for (int i = 1; i <= n; ++i)
using namespace std;
 
template<typename A, typename T, size_t N>
void Fill(A (&array)[N], const T& val) {
    fill((T*)array, (T*)(array + N), val);
}
 
const int dy[4] = { 1, -1, 0, 0 };
const int dx[4] = { 0, 0, 1, -1 };
typedef pair<int, int> pii;
 
int tc, N, M;
int board[100 + 5][100 + 5];
int dist[3][100 + 5][100 + 5];
 
bool inr(int y, int x) {
    return 0 <= y && y <= N + 1 && 0 <= x && x <= M + 1;
}
 
void bfs01(int r, int c, int person) {
    dist[person][r][c] = 0;
    deque<pii> dq;
    dq.emplace_back(r, c);
 
    while (!dq.empty()) {
        auto [R, C] = dq.front();
        dq.pop_front();
        rep(i, 4) {
            int NR = R + dx[i];
            int NC = C + dy[i];
            if (!inr(NR, NC) || board[NR][NC] == -1 || dist[person][NR][NC] != INT_MAX / 3)
                continue;
 
            dist[person][NR][NC] = dist[person][R][C] + board[NR][NC];
            if (board[NR][NC] == 1) {
                dq.emplace_back(NR, NC);
            } else if (board[NR][NC] == 0) {
                dq.emplace_front(NR, NC);
            }
        }
    }
}
 
int main() {
#ifndef ONLINE_JUDGE
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
#endif
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);
 
    cin >> tc;
    while (tc--) {
        vector<pii> prisoner;
        memset(board, 0, sizeof(board));
        Fill(dist, INT_MAX / 3);
        cin >> N >> M;
        REP(i, N) REP(j, M) {
            char x;
            int conv = 0;
            cin >> x;
 
            switch (x) {
            case '*': {
                conv = -1;
                break;
            }
            case '#': {
                conv = 1;
                break;
            }
            case '$': {
                prisoner.emplace_back(i, j);
                break;
            }
            }
            board[i][j] = conv;
        }
        prisoner.emplace_back(0, 0);
        rep(i, 3) {
            bfs01(prisoner[i].first, prisoner[i].second, i);
        }
 
        REP(k, 2) {
            for (int i = 0; i <= N + 1; ++i) {
                for (int j = 0; j <= M + 1; ++j) {
                    dist[0][i][j] += dist[k][i][j];
                }
            }
        }
        int ans = INT_MAX;
        for (int i = 0; i <= N + 1; ++i) {
            for (int j = 0; j <= M + 1; ++j) {
                if (board[i][j] == 1)
                    dist[0][i][j] -= 2;
                ans = min(ans, dist[0][i][j]);
            }
        }
        cout << ans << '\n';
    }
    return 0;
}