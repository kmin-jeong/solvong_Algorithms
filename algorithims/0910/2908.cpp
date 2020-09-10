#include <iostream>
using namespace std;

int ReverseNumber(int num);
int main(){
    int a,b;
    cin >> a >> b;
    
    if(ReverseNumber(a) > ReverseNumber(b)){
        cout << ReverseNumber(a);
    }else{
        cout <<ReverseNumber(b);
    }
}

int ReverseNumber(int num){
    int a,b,c,result;
    a = num%10;
    b = (num/10)%10;
    c = (num/100)%10;
    
    result = a*100 + b*10 + c;
    return result;    
}
