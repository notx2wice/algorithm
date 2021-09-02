#include <iostream>
#include <algorithm> // fill, fill_n 
#include <vector>
#include <string.h> // memcpy
#include <deque>
#include <queue> // priority queue
#include <list>
#include <set>
#include <map>

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

    //set , multiset
    //set -> 키(o) 밸류(x)
    //초기화 
    set <int> s; multiset< int> ms;
    s.insert(1);
    s.insert(2);
    s.insert(5);
    s.insert(-1);
    s.insert(42);
    s.erase(-1); // 그냥도 지워짐 왜냐 값자체가 iter이기 때문이다 이진 트리 구조에서는 
    s.erase(s.find(42));
    ms.insert(1);
    ms.insert(1);
    ms.insert(1);
    set<int>:: iterator setit;
    multiset<int> :: iterator mulset;
    for (setit = s.begin() ; setit != s.end(); setit++)
        cout << *setit << " ";
    cout << endl;
    //ms.erase(1); // 1을 모두 지워 버린다.
    ms.erase(ms.find(1)); // 이거는 값을 한개만 지운다.
    for (mulset = ms.begin(); mulset != ms.end(); mulset++)
        cout << *mulset << " ";

        
    //map , multimap -> key(o) , value(o) 멀티맵은 []연산자로 value 수정 불가능
    map<int, string> m;
    //  key  value
    m.insert(pair<int, string>(40, "me"));
    m.insert(pair<int, string>(35, "Show"));
    m.insert(pair<int, string>(10, "Dok2"));
    m.insert(pair<int, string>(90, "6"));
    m.insert(pair<int, string>(65, "money"));
    m.insert(pair<int, string>(20, "ZICO"));
    m.insert(pair<int, string>(50, "the"));
 
    map<int, string>::iterator iter;
    
    //접근방법 1 
    for(iter = m.begin(); iter != m.end(); iter++){
        cout << "[" << iter->first << ", " << iter->second << "]" << " " ;
    }
    cout << endl;
    
    //접근방법 2 
    for(iter = m.begin(); iter != m.end(); iter++){
        cout << "[" << (*iter).first << ", " << (*iter).second << "]" << " " ;
    }
    // 객체나 구조체를 키로 삼고 싶으면  < 오퍼레이션 오버라이딩이 필요함 
    // map은 키값을 기준으로 오름 차순 정렬되어 있음
    // value로 정렬을 하고 싶다면 .. 벡터로 옴기고 정렬하는수 밖에...

    //queue priority queue 
    queue<int> q;
 
    cout << endl << "=== empty ===" << endl;
    cout << "size : " << q.size() << endl;
    cout << "empty : " << q.empty() << endl;
 
    q.push(10);
    q.push(20);
    q.push(30);
    q.push(40);
    q.push(50);
    q.push(60);
    
    cout << endl << "=== push ===" << endl;
    cout << "size : " << q.size() << endl;
    cout << "empty : " << q.empty() << endl;    
    cout << "front : " << q.front() << endl;
    cout << "back : " << q.back() << endl << endl;
    
    
    cout << endl << "=== front & pop ===" << endl;
    while(!q.empty()){
        cout << q.front() << endl;
        q.pop();
    }

    // pq!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    priority_queue<int> pq;
    
    cout << "empty : " << pq.empty() << endl;
    pq.push(20);
 
    cout << "empty : " << pq.empty() << endl;
    cout << "top : " << pq.top() << endl;
 
    pq.push(10);
    cout << "top : " << pq.top() << endl;
 
    pq.push(30);
    cout << "top : " << pq.top() << endl;
 
    pq.push(50);
    pq.push(40);
    cout << "top : " << pq.top() << endl;
    cout << "size : " << pq.size() << endl;
 
    pq.pop();
    cout << "top : " << pq.top() << endl;
 
    while(!pq.empty()){
        cout << pq.top() << endl;
        pq.pop();        
    }

    //연산자 오버라이딩 !!! sort에 적용시켜 보자.
}