#include <stdio.h>
#include <iostream>
using namespace std;
static const int MAX = 100;
int main()
{
    // for i = 0 to A.length-1
    // 2     mini = i
    // 3     for j = i to A.length-1
    // 4         if A[j] < A[mini]
    // 5             mini = j
    // 6     swap A[i] and A[mini]
    int N, A[MAX], elem, mini, sw = 0;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> elem;
        A[i] = elem;
    }
    for (int i = 0; i < N; i++)
    {
        mini = i;
        for (int j = i; j < N; j++)
        {
            if (A[j] < A[mini])
            {
                mini = j;
            }
        }
        swap(A[i], A[mini]);
        sw++;
    }
    for (int i = 0; i < N; i++)
    {
        if (i)
        {

            cout << " ";
        }
        cout << A[i];
    }
    cout << endl;

    cout << sw;
    return 0;
}