#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    int n, target, count = 0, j, sw = false;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> target;
        if (target == 2)
        {
            count += 1;
        }
        if (target > 2)
        {
            for (j = 2; j < sqrt(target) + 1; j++)
            {
                if (target % j == 0)
                {
                    sw = true;
                    break;
                }
            }
            if (!sw)
            {
                count += 1;
            }
            sw = false;
        }
    }
    cout << count << endl;
    return 0;
}