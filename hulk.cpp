#include <iostream>
#include <vector>
#include <cstring>
using namespace std; 

int main() {
    int n; 
    cin >> n; 
 
    if (n == 1) {
        cout << "I hate it";
    }
    else if (n == 2) {
        cout << "I hate that I love it";  
    }

    else {

        for (int i = 1; i < n; ++i) {
            if (i % 2 != 0) {
                cout << "I hate that ";
            }
            else {
                cout << "I love that ";
            } 
        }

        if (n % 2 == 0)
            cout << "I love it";
        else
            cout << "I hate it";
    }
}
