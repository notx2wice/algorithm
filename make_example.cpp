#include <iostream>
#include <algorithm> // fill, fill_n 
#include <vector>
#include <string.h> // memcpy
#include <deque>
#include <queue> // priority queue
#include <list>

using namespace std;

typedef struct s_test
{
    int a, b;
    s_test(int a, int b) : a(a), b(b) {}
}               t_test;

int arr[10];
int arr_copy[10];

int main(){
    fill(&arr[0], &arr[9] , 42);
    for (int x = 0; x < 10; x++)
        cout << arr[x] << " ";
    cout << "\n";  
    // 0  1  2  3  4  5  6  7  8  9
    // 42 42 42 42 42 42 42 42 42 0 출력 결과 
    fill(&arr[0], &arr[10] , 42); // 2번째 인자 전 까지 채워줌
    for (int x = 0; x < 10; x++)
        cout << arr[x] << " ";
    cout << "\n";  
    fill_n(arr, 10 , 4242); // 갯수 만큼 채워준다.
    for (int x = 0; x < 10; x++)
        cout << arr[x] << " ";
    cout << "\n";  

    memcpy(arr_copy, arr, sizeof(int) * 10); // 3번째 인자 바이트임
    for (int x = 0; x < 10; x++)
        cout << arr_copy[x] << " ";
    cout << "\n";  
    s_test s_maked = s_test(1, 2);
    cout << s_maked.a + s_maked.b << "\n";

    //vector 선언 , deque 이하 동일
    vector <int> data0;
    deque <int> dq;
    vector <int> data1(5); // 0으로 초기화 되면서 들어가는 구나.
    data0.assign(5, 1); // 1로 5개 크기 할당;
    data1.push_back(2);
    data1.insert(data1.begin(), 1);
    data1.insert(data1.begin() + 1,3);
    // data0.end() : 마지막 + 1  data0.back() : 마지막
    //      .begin()                .front()
    for (int x = 0; x < data1.size(); x++)
        cout << data1[x]<< " ";
    cout << endl;
    data1.erase(data1.begin()); // 삽입 삭제 모두 이터레이터로 동작
    //deque 차이점
    dq.push_back(1);
    dq.push_front(2);
    cout << dq[0] << " " << dq[1] <<endl; //이렇게 접근 가능
    cout << dq.front() <<endl;
    dq.pop_front();
    dq.pop_back(); // push_front , pop_front 가 있다.

    // list 생성
    list <int> lst;
    list <int> lst1(3, 42);
    lst.push_back(1); lst.push_back(2); lst.push_front(0);
    //lst.assign(3, 42); // 갈아 없고 새로 할당
    list<int> ::iterator it;
    it = lst.begin(); // 리스트는 이터레이터 + 연산 당연히 안되겠지 증신차려
    it++;
    it++;
    lst.insert(it, 3 ,42);
    it = lst.begin();
    lst.erase(it); // 흠 탐색 하면서 삭제하지 않으면 계산 이득이 없을듯
    for (it = lst.begin() ; it != lst.end() ; it++)
        cout << *it <<" "; //iterator *를 붙여야 합니다. 
    cout << endl;
    lst.remove(42); // 찾아서 다 삭제
    for (it = lst.begin() ; it != lst.end() ; it++)
        cout << *it <<" "; //iterator *를 붙여야 합니다. 
    cout << endl;
}