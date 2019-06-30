#include <iostream>
using namespace std;

int main()
{
    int time, hrs, mins, secs, rems;
    cin >> time;
    hrs = time / 3600;
    rems = time - hrs * 3600;
    mins = rems / 60;
    rems = rems - (mins * 60);
    secs = rems;
    cout << hrs << ":" << mins << ":" << secs << endl;
}