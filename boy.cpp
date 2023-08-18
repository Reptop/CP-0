#include <iostream>
using namespace std;

void swap(char* xp, char* yp) {
    char temp = *xp;
    *xp = *yp;
    *yp = temp;
}

int main() {
  int a, b;
  string s; 

  cin >> a >> b;
  cin >> s;

  for (int i = 0; i < s.length() - 1; ++i) {
    if (s[i] == 'B' && s[i+1] == 'G') {
      swap(&s[i], &s[i+1]);
    }
    else {
      continue;
    }
  }

  cout << s << endl;
  return 0;
}
