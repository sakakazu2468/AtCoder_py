#include <iostream>
using namespace std;

int main(int argc, char const* argv[])
{
  int a, b, c;
  cin >> a >> b >> c;
  if (c >= a and c <= b) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
  return 0;
}
