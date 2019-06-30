#include <iostream>
#include <stack>
using namespace std;

int dfs(int v, int visited[])
{
    if (visited[v])
    {
        return;
    }
    visited[v] = true;
    // adjacent node u
    for (int u = 0; u < (sizeof(v) / sizeof(*v)); u++)
    {
        dfs(u, visited);
    }
}

int DepthFirstSearch(int V)
{
    int visited[V];
    for (int v = 0; v < V; v++)
    {
        visited[v] = false;
    }
    for (int w = 0; w < V; w++)
    {
        dfs(w, visited);
    }
}

int main()
{
}