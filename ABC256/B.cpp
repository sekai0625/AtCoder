#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<int> A(N);
    for (auto &x : A)
        cin >> x;

    vector<bool> field(4, 0);
    int point = 0;

    for (auto x : A)
    {
        vector<bool> next_field(4, 0);
        field[0] = 1;
        for (int i = 0; i < 4; i++)
        {
            if (field[i])
            {
                if (i + x >= 4)
                    point++;
                else
                    next_field[i + x] = 1;
            }
        }
        field = next_field;
    }

    cout << point << endl;
    return 0;
}