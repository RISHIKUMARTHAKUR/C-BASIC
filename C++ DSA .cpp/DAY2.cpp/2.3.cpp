#include<iostream>
using namespace std;

int main(){
    
    char a;
    cout<<"Enter the character"<<endl;
    cin>>a;
    
    if (a>='A' && a<='Z') {
        cout<<"The given character is in UPPERCASE"<<endl;
    }
    else if (a>='a' && a<='z') {
        cout<<"The given character is in LOWERCASE"<<endl;
    }
    else if(a>='0' && a<='9') {
        cout<<"The given character is NUMERIC CHARACTER"<<endl;
    }
}