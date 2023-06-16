#include<iostream>
using namespace std;
int main(){
    for(int i=0 , j=10 , k=20 ;(i+j+k)<100 ; j++ , k--, i+=k){
        cout<<i<<" "<<j<<" "<<k<<endl;
    }
    return 0;
}   