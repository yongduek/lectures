#include<iostream>
#include<bits/stdc++.h>
using namespace std;


int main()
{
    unsigned long N, x, ub, lb;
    cin >> N;
    cout << "N:" << N << endl;
    
    ub = INT_MAX;
    lb = 0;
    x = INT_MAX >> 1; // half of max
    while (x < N) {
        if (x >= N) {
            x >>=1;
            continue;
        }
        unsigned long y = x*x;
        if (y == N) {
            break;
        } else if (y < N) {
            lb = x; // increase lb
            x = int( (ub+lb)/2 );  // increase x
            if (lb == ub) break;
        } else if (y > N) {
            ub = x; 
            x = int( (ub+lb) / 2);
        }
    }
    cout << x ;
    return 0;
}