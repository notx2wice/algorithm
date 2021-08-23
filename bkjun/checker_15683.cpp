#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>

using namespace std;
typedef struct t_cctv
{
	int x;
	int y;
	int type;

	t_cctv(int xx, int yy, int tt) : x(xx), y(yy), type(tt) {}
}              cctv;

int idx[4] =  {-1,0,1,0}; // 상 우 하 좌
int idy[4] =  {0,1,0,-1};

int W,H, cctv_count, answer;

int map[10][10];
int paper[10][10];

vector <cctv> cctvv;

int cctv_ewsn[8];

void draw_line(int x, int y, int dir)
{
	int tx = x + idx[dir];
	int ty = y + idy[dir];

	while (paper[tx][ty] != 6)
	{
		paper[tx][ty] = 7;
		tx += idx[dir];
		ty += idy[dir];
	}
}

void draw_one(int x, int y,int dir)
{
	draw_line(x,y,dir);
}
void draw_two(int x, int y, int dir)
{
	draw_line(x,y, dir);
	draw_line(x,y, (dir + 2) % 4);
}
void draw_three(int x, int y,int dir)
{
	draw_line(x,y, dir);
	draw_line(x,y, (dir + 1) % 4);
}
void draw_four(int x, int y, int dir)
{
	draw_line(x,y, dir);
	draw_line(x,y, (dir + 1) % 4);
	draw_line(x,y, (dir + 2) % 4);
}
void draw_five(int x, int y)
{
	draw_line(x,y, 0);
	draw_line(x,y, 1);
	draw_line(x,y, 2);
	draw_line(x,y, 3);
}
void draw(int cc_num)
{
	t_cctv *temp;

	temp = &cctvv[cc_num];
	if(cctvv[cc_num].type == 1)
		draw_one(temp->x, temp->y, cctv_ewsn[cc_num]);
	else if(cctvv[cc_num].type == 2)
		draw_two(temp->x, temp->y, cctv_ewsn[cc_num]);
	else if(cctvv[cc_num].type == 3)
		draw_three(temp->x, temp->y, cctv_ewsn[cc_num]);
	else if(cctvv[cc_num].type == 4)
		draw_four(temp->x, temp->y, cctv_ewsn[cc_num]);
	else if(cctvv[cc_num].type == 5)
		draw_five(temp->x, temp->y);
}

int count_seven()
{
	int count = 0;
	for (int h = 1; h <= H; h++)
	{
		for(int w = 1; w <= W; w++)
		{
			if (paper[h][w] == 0)
				count++;
		}
	}
	return count;
}

int make_map()
{
	int count = 0;
	memcpy(&paper[0][0], &map[0][0], 100 * sizeof(int));
	for (int x = 0; x <cctv_count; x++)
		draw(x);
	count = count_seven();
	return count;
}

void dfs(int level)
{
	if (level == cctv_count)
	{
		int t_answer;
		t_answer = make_map();
		if (t_answer < answer)
			answer = t_answer;
		return ;
	}
	else
	{
		for(int x=0; x< 4; x++)
		{
			cctv_ewsn[level] = x;
			dfs(level + 1);
			cctv_ewsn[level] = 0;
		}
	}
}

int main()
{
	cctv_count = 0;
	answer = 1000;
	cin >> H >> W;
	fill_n(&map[0][0], 100, 6);
	for (int h=1;h<=H;h++){
		for(int w=1; w<=W; w++){
			int temp;
			cin >> temp;
			if ( temp >=1 && temp <=5 )
			{
				map[h][w] = 7;
				cctvv.push_back(t_cctv(h, w, temp));
				cctv_count++;
			}
			else if (temp == 0)
				map[h][w] = 0;
		}
	}
	dfs(0);
	cout << answer;
	return 0;
}