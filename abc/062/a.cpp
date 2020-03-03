#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


int main(int argc, char const* argv[])
{
  vector<int> a{1, 3, 5, 7, 8, 10, 12};
  vector<int> b{4, 6, 9, 2};
  int x, y;
  cin >> x >> y;
  if (x==2 or y==2) {
    cout << "No" << endl; 
  } else {
    if ((a.find(a.begin(), a.end(), x) and a.find(a.begin(), a.end(), y)) or (b.find(a.begin(), a.end(), y) and b.findy))) {
      cout << "Yes" << endl;
    } else {
      cout << "No" << endl;
    }
  }
  return 0;
}
