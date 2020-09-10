#include <stdio.h>
 
void fibonacci(int N)
{
    int past, current, result;
    current=1, past = result = 0;
    int i;
    for (i = 0; i <=N; i++)
    {
        past = current;
        current = result;
        result = past + current;
    }
    printf("%d %d\n", past, current);
}
int main()
{
    int N,M;
    int i;
    scanf("%d", &N);
    for (i = 0; i < N; i++)
    {
        scanf("%d", &M);
        fibonacci(M);
    }
}
