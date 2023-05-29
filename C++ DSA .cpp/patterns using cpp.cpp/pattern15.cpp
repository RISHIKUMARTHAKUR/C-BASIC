#include<iostream>
using namespace std;

int main(){

    int n;
    cin>>n;

    int row = 1;
    while(row<=n){

        int column = 1;
        while(column<=n-row+1){
            cout<<column<<" ";
            column = column + 1;
        }
        column = 1;
        while(column<=(row - 1)*2){
            cout<<" * ";
            column = column + 1;
        }
        column = n - column + 1;
        while(column >= 1){
            cout<<column<<" ";
            column = column -1;
        }
        row = row +1;
        cout<<endl;
    }
}