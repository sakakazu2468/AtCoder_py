#include <iostream>
#include <string>
using namespace std;


int main(int argc, char const* argv[])
{
  string s1, s2, s3;
  cin >> s1 >> s2 >> s3;
  cout << char((int)s1[0]-32) << char((int)s2[0]-32) << char((int)s3[0]-32) << endl;
  return 0;
}
