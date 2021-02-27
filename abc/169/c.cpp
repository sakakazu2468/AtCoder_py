#include <iostream>
using namespace std;

int main() {
  long long int a;
  float b;
  long long int b_100;

  cin >> a >> b;
  b_100 = b*100;
  a *= b_100;
  cout << a/100 << endl;
   
  return 0;
}
