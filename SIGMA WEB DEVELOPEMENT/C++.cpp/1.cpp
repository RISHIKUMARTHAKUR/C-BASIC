#include<bits/stdc++.h>
using namespace std;

//Grade system for student

int main(){

   int marks;
   cin>>marks;
   if(marks<25){
    cout<<"F";
   }
   else if(marks<44 && marks>25){
    cout<<"E";

   }
   else if(marks<49 && marks>45){
    cout<<"D";
   }
   else if(marks<59 && marks>50){
    cout<<"C";
   }
   else if(marks<79 && marks>60){
    cout<<"B";

   }
   else if(marks<100 && marks>80){
    cout<<"A";
   }

    return 0;
}

