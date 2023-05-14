#incclude<iostream>
using namespace std;

int main(){

     
    int n;
    cin>>n;
    
     int i=2;
     
     while (i<n){
         if(n%i!=0){
             cout<<"The given number is  not a prime number"<<i<<endl;
         }
         else{
             cout<<"The given number is a prime number"<<i<<endl;
         }
         i=i+1;
     }

}