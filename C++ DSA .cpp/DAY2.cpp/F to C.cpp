#include<iostream>
using namespace std;


/*program to convert farenhite to celsius*/
int main(){
    
    float fahrenheit;
    cin>>fahrenheit;
    float celsius = (5.0/9)*(fahrenheit - 32);
    cout<<fahrenheit <<"F = "<< celsius << " C "<< endl;
    
    return 0;
} 