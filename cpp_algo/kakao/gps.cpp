#include <vector>
#include <iostream>
#include <iomanip>
using namespace std;

int di_dp[202][202];  //node
int ans_dp[202][202]; //index
int map[202][202]; //node

void dikstra(int n)
{
    for (int x = 0 ; x <= 200; x++)
        for(int y = 0; y <= 200 ; y++)
        {
            if (map[x][y] == 1)
                di_dp[x][y] = 1;
            if (x == y)
                di_dp[x][y] = 0;
        }
    for (int nod = 1; nod <= n ; nod++)
        for (int x = 1; x <= n; x++)
            for(int y = 1; y <= n; y++)
                if (di_dp[x][nod] + di_dp[nod][y] < di_dp[x][y])
                    di_dp[x][y] = di_dp[x][nod] + di_dp[nod][y];
}

void make_ans(int n,int k, vector<int> gps)
{
    for (int t = 1; t <= k; t++)
    {
        for (int s = 1 ; s + t <= k ; s++)
        {
            int e = s + t;
            if (t == 1)
            {
                if (map[gps[s]][gps[e]] == 1)
                    ans_dp[s][e] = 0;
                continue;
            }
            for (int mid = s + 1 ; mid < e; mid++)
                if (ans_dp[s][mid] + ans_dp[mid][e] < ans_dp[s][e])
                    ans_dp[s][e] = ans_dp[s][mid] + ans_dp[mid][e];
            if (ans_dp[s][e] > di_dp[gps[s]][gps[e]] - 1 && e - s >= di_dp[gps[s]][gps[e]] && di_dp[gps[s]][gps[e]] < 1000000000)
                if ( e- s -1 < ans_dp[s][e])
                    ans_dp[s][e] = e - s - 1;
        }
    }
}

int solution(int n, int m, vector<vector<int> > edge_list, int k, vector<int> gps_log) {
    gps_log.insert(gps_log.begin(),0);
    for (int x = 0 ; x <= 200; x++)
        for(int y = 0; y <= 200 ; y++)
        {
            di_dp[x][y] = 1000000000;
            ans_dp[x][y] = 1000000000;
            map[x][y] = 1000000000;
            if (x == y)
            {
                map[x][y] = 1;
                ans_dp[x][y] = 0;
                di_dp[x][y] = 0;
            }
        }
    
    for (int x = 0; x < m; x++)
    {
        map[ edge_list[x][0] ][ edge_list[x][1] ] = 1;
        map[ edge_list[x][1] ][ edge_list[x][0] ] = 1;
    }   
    dikstra(n);
    make_ans(n, k, gps_log);
    if (ans_dp[1][k] >= 1000000000)
        return -1;
    return ans_dp[1][k];
}

int main()
{
    int n , m , k;
    n = 7;
    m = 10;
    k = 6;
    vector< vector<int> > edge_list;
    vector< int > gps_log ;
    vector<int> t;
    t.push_back(1);
    t.push_back(2);
    edge_list.push_back(t);
    t.clear();
    t.push_back(1);
    t.push_back(3);
    edge_list.push_back(t);
    t.clear();
    t.push_back(2);
    t.push_back(3);
    edge_list.push_back(t);
    t.clear();
    t.push_back(2);
    t.push_back(4);
    edge_list.push_back(t);
    t.clear();
    t.push_back(3);
    t.push_back(4);
    edge_list.push_back(t);
    t.clear();
    t.push_back(3);
    t.push_back(5);
    edge_list.push_back(t);
    t.clear();
    t.push_back(4);
    t.push_back(6);
    edge_list.push_back(t);
    t.clear();
    t.push_back(5);
    t.push_back(6);
    edge_list.push_back(t);
    t.clear();
    t.push_back(5);
    t.push_back(7);
    edge_list.push_back(t);
    t.clear();
    t.push_back(6);
    t.push_back(7);
    edge_list.push_back(t);
    gps_log.push_back(20);
    gps_log.push_back(20);
    gps_log.push_back(1);
    gps_log.push_back(1);
    gps_log.push_back(1);
    gps_log.push_back(7);

    cout << solution(n, m, edge_list, k, gps_log);
}