#include<cstdio>
#include<algorithm>

using namespace std;

const int max_n = 100, max_k = 450, max_w = max_n/2 *max_k;

int main(){
    
    int N, K[max_n], i , j , k, t = 0, a = 2000000000, b, diff = 2000000000;
    bool dp[51][max_w + 1] = {};
    
    scanf("%d", &N);
    
    for (i = 0; i < N; i ++)
    {
        scanf("%d", &K[i]);
        t+=K[i];
    }
    dp[0][0] = 1;
    
    for(i = 0; i < N; i++) 
        for (j= N/2; j; j--)
            for(k = max_w; k >= K[i]; k--)
                dp[j][k] |= dp[j-1][k - K[i]];
    
    for (k = 0; k <max_w; k++) 
        if (dp[N/2][k])
            if (diff > abs(t-2*k))
            {
                diff = abs(t-2*k);
                a = k;
            }
    b = t - a;
    if (a> b) swap(a, b);
    printf("%d %d", a, b);
    return 0;
}