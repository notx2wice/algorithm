#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int T;
int answer;
int blue[4][6];
int green[6][4];

void add_block_blue(int form , int x, int y){
    if (form == 1)
    {

    }
    else if (form == 2)
    {

    }
    else
    {

    }
}
void add_block_green(int form , int x, int y)
{
    if (form == 1)
    {

    }
    else if (form == 2)
    {

    }
    else
    {

    }
}
void after_blue()
{

}
void after_green()
{

}

int main()
{
    answer = 0;
    cin >> T;
    for (int t = 0 ; t < T; t++)
    {
        int form, x, y;
        cin >> form >> x >> y;

        add_block_blue(form, x, y);
        add_block_green(form, x, y);

        after_blue();
        after_green();

    }
    cout << answer;
}