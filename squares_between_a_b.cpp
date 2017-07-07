#include <cmath>
#include <cstdio>
#include <iostream>
using namespace std;
/*
HackerRank Challenge
Given two numbers, find the numbers between that range that are perfect squares.
Tried with python but it was too slow to actually complete cases where the numbers were really big and far apart.
c++ has the power and speed for something like this.
completed 7/7/17
*/

int main() {
    int t;// the number of tests we will b performing 
    cin >> t;
    for(int i = 0; i < t; i++){
        int a;
        int b;
        cin >> a >> b;// the range of the numbers
        int count = 0;
        for(int range = a; range <= b; range++){
            int temp = sqrt(range);
            if(temp * temp == range){
                range += temp * 2; //For speed purposes and because the next perfect square is sqrt(x)*2+1
                count ++;
            }
        }
        cout << count << "\n";
    }
    return 0;
}
