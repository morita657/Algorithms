#include <iostream>
using namespace std;
int main()
{
    int m, n;
    cin >> m >> n;
    int r;
    if (m == n)
    {
        cout << n << endl;
        return 0;
    }
    while (m != n && m > 0 && n > 0)
    {
        r = m % n;
        if (r == 0)
        {
            cout << n << endl;
        }
        m = n;
        n = r;
    }

    return 0;
}