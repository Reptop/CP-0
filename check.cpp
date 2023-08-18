#include <iostream>
using namespace std;

int main() {
  int cases;
  string check = "codeforces";

  cin >> cases;
  string letters[cases];

  for (int i = 0; i < cases; ++i) {
    cin >> letters[i]; 
  }

  for (int i = 0; i < cases; ++i) {
    if (check.find(letters[i]) != std::string::npos) {
      cout << "YES" << endl;
    }
    else {
      cout << "NO" << endl; 
    }
  }
  return 0;
}
