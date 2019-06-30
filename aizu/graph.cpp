#include <iostream>
using namespace std;
static const int N = 100;

int main()
{
    int M[N][N];
    int n, u, k, v;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            M[i][j] = 0;
        }
    }

    for (int i = 0; i < n; i++)
    {
        cin >> u >> k;
        for (int j = 0; j < k; j++)
        {
            cin >> v;
            M[u - 1][v - 1] = 1;
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (j)
            {
                cout << " ";
            }
            cout << M[i][j];
        }
        cout << endl;
    }
    return 0;
}