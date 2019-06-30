#include <iostream>
using namespace std;
<<<<<<< HEAD
static const int MAX = 100;
=======
>>>>>>> 4600b1ff8059f999868990b48e25517fde96d37a

int bubbleSort(int A[], int N)
{
    int sw = 0;

    bool flag = 1;
    for (int i = 0; flag; i++)
    {
        flag = 0;
        for (int j = N - 1; j >= i + 1; j--)
        {
            if (A[j] < A[j - 1])
            {
                swap(A[j], A[j - 1]);
                flag = 1;
                sw++;
            }
        }
    }
    return sw;
};

int main()
{
<<<<<<< HEAD
    int A[MAX], j, N, sw;
    cin >> N;
    for (int k = 0; k < N; k++)
    {
        cin >> j;
        A[k] = j;
    }
=======
    int A[10] = {1, 6, 3, 7, 9, 423, 76, 432, 0, 64}, N = 10, sw;
>>>>>>> 4600b1ff8059f999868990b48e25517fde96d37a
    sw = bubbleSort(A, N);
    for (int i = 0; i < N; i++)
    {
        if (i)
        {
            cout << " ";
        }
        cout << A[i];
    }
    cout << endl;
    cout << sw << endl;
    return 0;
}