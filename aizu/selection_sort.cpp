#include <stdio.h>
#include <iostream>
using namespace std;
static const int MAX = 100;
int main()
{
    int N, A[MAX], elem, mini, sw = 0;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> elem;
        A[i] = elem;
    }

    for (int k = 0; k < N; k++)
    {
        mini = k;
        for (int j = k; j < N; j++)
        {
            if (A[j] < A[mini])
            {
                mini = j;
            }
        }
        if (k != mini)
        {
            swap(A[k], A[mini]);
            sw++;
        }
    }
    for (int j = 0; j < N; j++)
    {
        if (j)
        {
            cout << " ";
        }
        cout << A[j];
    }
    cout << endl;

    cout << sw << endl;
    return 0;
}