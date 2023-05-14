#include<iostream>


int main(){
    
    int n;
    std::cin>>n;
    
    int row = 1;
    while(row<=n){
        int column = 1;
        while(column<=row){
            std::cout<<"*";
            column =column + 1;
        }
        std::cout<<std::endl;
        row = row + 1;
    }
    
}