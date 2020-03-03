#include <iostream>
#include <string>
using namespace std;


int main(int argc, char const* argv[])
{
  string a, b, c;
  cin >> a >> b >> c;
  if (a.at(a.size()-1) == b[0] and b.at(b.size()-1) == c[0]) {
    cout << "YES" << endl;
  } else {
    cout << "NO" << endl;
  }
  return 0;
}
