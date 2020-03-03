#include <iostream>
using namespace std;

int main(){
  int a, b;
  cin >> a >> b;
  if (a==1 || b==1) {
    if (a==b) {
      cout << "Draw" << endl;
    } else if (a!=1) {
      cout << "Bob" << endl;
    } else {
      cout << "Alice" << endl;
    }
  } else {
    if (a==b) {
      cout << "Draw" << endl;
    } else if (a>b) {
      cout << "Alice" << endl;
    } else {
      cout << "Bob" << endl;
    }
  }
}
