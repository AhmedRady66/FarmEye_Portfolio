#include <vector>
#include <iostream>
#include <math.h>
#include <vector>
#include <string>
#include <array>

using namespace std;

int findDifference(array<int, 3> a, array<int, 3> b) {
    int result = 0, c1 = 1, c2 = 1;
    for (int i = 0; i < 3; i++)
    {
        c1 *= a[i];
        c2 *= b[i];
        result = c1 - c2;
    }

    return abs(result);
}

int main()
{

    cout << findDifference({ 3, 2, 5 }, { 1, 4, 4 }) << "\n";
    cout << findDifference({ 9, 7, 2 }, { 5, 2, 2 }) << "\n";
    cout << findDifference({ 11, 2, 5 }, { 1, 10, 8 }) << "\n";

    return 0;
}