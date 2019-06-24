#include <iostream>
#include <algorithm>
using namespace std;

static const int N = 100;

int main()
{
    int n, p[N + 1], m[N + 1][N + 1];
    cin >> n;
    for (int i = 0; i <= n; i++)
    {
        cin >> p[i - 1] >> p[i];
    }

    for (int i = 1; i <= n; i++)
    {
        m[i][i] = 0;
    }
    for (int i = 2; i <= n; i++)
    {
        for (int l = 1; l <= n - l; l++)
        {
            int j = i + l - 1;
            m[i][j] = (1 << 21);
            for (int k = 1; k <= j - 1; k++)
            {
                m[i][j] = min(m[i][j], m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]);
            }
        }
    }
    cout << m[1][n] << endl;

    return 0;
}