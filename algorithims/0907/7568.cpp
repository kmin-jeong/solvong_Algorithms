#include <iostream>
 
using namespace std;
 
int main() {
 
    int N;
 
    cin >> N;
 
    int* height = new int[N];
    int* weight = new int[N];
    int* bulk = new int[N];
 
    for (int i = 0; i < N; i++) {
        cin >> weight[i] >> height[i];
        bulk[i] = N;
    }
 
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            if (weight[i]>weight[j] && height[i]>height[j]) { 
                bulk[i]--;
            }
            else if (weight[i] < weight[j] && height[i] < height[j]) { 
                bulk[j]--;
            }
            else { 
                bulk[i]--;
                bulk[j]--;
            }
        }
    }
 
    for (int i = 0; i < N; i++) {
        cout << bulk[i] << " ";
    }
 
    return 0;
}
