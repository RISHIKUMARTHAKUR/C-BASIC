#include <iostream>
using namespace std;

int main(){

    int a;
    
    cout<<"Enter the value of a  : "<< endl;
    cin>>a;
    
    
   if (a>0) {
       cout<<"The given number is positive"<<endl;
   }
   else if(a<0) {
       cout<<"The given number is negative"<<endl;
       }
       else {
           cout<<"The given number is 0"<<endl;
       }
       
    return 0;
}