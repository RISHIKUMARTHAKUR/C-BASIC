#include<iostream>
using namespace std;
int main(){

    int n;
    cin>>n;

    int row = 1;
    while(row<=n){

        int column = 1;
        char ch = 'A' + row + column -2;
        while (column <=n){
            cout<<ch<<" ";
            column = column +1;
            ch = ch + 1;
        }
        cout<<endl;
        row = row + 1;
    }

}