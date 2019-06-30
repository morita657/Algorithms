#include <stdio.h>
#include <iostream>
using namespace std;

int partition(int A[], int N, int p, int r)
{
    int x = A[r];
    int i = p - 1, j;
    for (j = p; j < r; j++)
    {
        if (A[j] < x)
        {
            i = i + 1;
            swap(A[i], A[j]);
        }
    }
    swap(A[i + 1], A[j]);
    return i + 1;
}

int main()
{
    int A[] = {13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11};
    int N = sizeof(A) / sizeof(*A);
    int q = partition(A, N, 0, N - 1);
    for (int i = 0; i < N; i++)
    {
        if (i)
        {
            printf(" ");
        }
        if (i == q)
        {
            printf("[");
        }
        printf("%d", A[i]);
        if (i == q)
        {
            printf("]");
        }

        // cout << A[i] << endl;
    }
    return 0;
}