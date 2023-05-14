/* program to swap two numbers with the help of a third variable */

#include <iostream>
using namespace std;

int main(){

    cout<<"SWAP TWO NUMBERS"<<endl;
    int n1=5, n2=6, n3;

    cout<<"BEFORE SWAPPING , THE FIRST NUMBER IS :"<<n1<<endl;
    cout<<"BEFORE SWAPPING THE SECOND NUMBER IS :"<<n2<<endl;


    n3=n2;
    n2=n1;
    n1=n3;

    cout<<"AFTER SWAPPING THE FIRST NUMBER IS :"<<n1<<endl;
    cout<<"AFTER SWAPPING THE SECOND NUMBER IS :"<<n2<<endl;

    return 0;
}