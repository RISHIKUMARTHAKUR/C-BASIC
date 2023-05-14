#include<iostream>
using namespace std;

int main(){

 
    int a = 123;
    cout<<a<<endl;

    char b ='v';
    cout<< b <<endl;

    bool bl = true;
    cout<< bl <<endl;

    float f= 1.02355466;
    cout<< f <<endl;

    double d= 1.02563;
    cout<< d << endl;

    int size= sizeof(a);
    cout<< "The size of integer is :"<< size << endl;

    int size1 = sizeof(b);
    cout<<"The size of char is    :"<< size1 << endl;

    int size2= sizeof(bl);
    cout<<"The size of boolean is :"<< size2 << endl;

    int size3 = sizeof(f);
    cout<< "The size of float is   :"<< size3 <<endl;

    int size4 = sizeof(d);
    cout<< "The size of double is  :"<< size4 <<endl;





}