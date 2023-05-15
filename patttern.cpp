#include<iostream>
using namespace std;
int main(){
    
    int n;
    cin>>n;
    
    int row=1;
    while(row<=n){
        
        int column =1;
        int value = row;
        while(column<=row){
            cout<<value;
            value = value + 1;
            column = column + 1; 
        }
        cout<<endl;
        row = row + 1; 
    }
    
}