#include <iostream>
#include <vector>

using namespace std;


int main() {
    //a has to be divsible by b 
    int cases, counter = 0; 
    cin >> cases;
    int a[cases];

    for (int i = 0; i < cases; ++i) {
        cin >> a[i];  
    }
    for (int i = 0; i < cases; i+2) {
        if (a[i] % a[i+1] != 0) {
            ++a[i]; 
            ++counter; 
        }
    }

    cout << counter;
    
}

