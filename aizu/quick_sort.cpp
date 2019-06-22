#include <stdio.h>
#include <iostream>
using namespace std;

int partition(int A[], int N, int l, int r)
{
    int i, j, t;
    int x = A[r];
    i = l - 1;
    for (j = l; j < r; j++)
    {
        if (A[j] <= x)
        {
            i++;
            t = A[i];
            A[i] = A[j];
            A[j] = t;
        }
    }
    t = A[i + 1];
    A[i + 1] = A[r];
    A[r] = t;
    return i + 1;
}

int quickSort(int A[], int N, int i, int j)
{
    int k;
    if (i >= j)
    {
        return false;
    }
    k = partition(A, N, i, j);
    quickSort(A, N, i, k - 1);
    quickSort(A, N, k, j);
}

int main()
{
    int A[] = {1, 6, 2, 7, 32, 876, 32, 1, 73};
    int N = sizeof(A) / sizeof(*A);
    int sw = quickSort(A, N, 0, N - 1);
    for (int i = 0; i < N; i++)
    {
        cout << A[i] << endl;
    }
    return 0;
}