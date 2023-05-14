#include<iostream>
using namespace std;


/*program to add all even number upto n*/
int main(){
    
    int n;
    cin>>n;
    int sum=0;
    int i  = 2;
    
    while(i<=n){
        if(i%2==0){
            sum=sum+i;
        }
        i=i+1;
    }
    cout<<"Sum from  "<< 1 <<"  to  "<<n<< "  =  " <<sum<<endl;
    return  0;
} 
