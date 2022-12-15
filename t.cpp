#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

void solve();
void permute();


/*
void solve(vector<int> *list) {

  int exponent;

  for (int i = 1; i <= exponent; ++i) {
    int z = 0;
    z = pow(n, i); 
    list->push_back(z);
  }
  //list->push_back()

  for (auto i : list) {
    cout << i << " ";
  }

  for (auto it = list->begin(); it != list->end(); ++it){
    cout << *it << endl;
  }

}
*/


int main() {

  vector<int> *list = new vector<int>();
  vector<int> *exponent = new vector<int>();

  int n = 2, cases; 

  cin >> cases;

  for (int i = 0; i < cases; ++i) {
    int e = 0;
    cin >> e; 
    exponent->push_back(e);
  }

  //for (auto it = exponent->begin(); it != exponent->end(); ++it){
    //cout << *it << endl;
  //}

  //push 1 element from vector at a time



  for (auto it = exponent->begin(); it != exponent->end(); ++it){
    for (int i = 1; i <= *it; ++i) {
      int z = 0;
      z = pow(n, i); 
      list->push_back(z);
    }
  }

  /*for (int i = 1; i <= exponent; ++i) {
    int z = 0;
    z = pow(n, i); 
    list->push_back(z);
    }
    */
  //list->push_back()

  for (auto it = list->begin(); it != list->end(); ++it){
      cout << *it << endl;
  }

  if (vector.size() % 2 == 0) {

  }

  //permute();
}


void permute() {
  int a[] = {3,4,6,2,1};
  int size = sizeof(a)/sizeof(a[0]);
  std::sort(a, a+size);
  do {
    for (int i = 0; i < size; ++i) {
      cout << a[i] << endl;
    }
    cout << "\n";
  } while(std::next_permutation(a, a+size));
}
