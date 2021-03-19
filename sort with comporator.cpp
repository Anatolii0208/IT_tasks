#include <iostream>
#include <queue>
#include <vector>

using namespace std;

typedef long long LL;

struct Para {
  int First;
  int Second;
};

#define ii pair<int, int>
#define S second
#define F first
#define iii pair<int, ii>
#define viii vector<iii>


//Para A[10];
//ii B[10];
//viii Q;

//priority_queue <int> Q;
//priority_queue < int, vector<int>, greater<int> > Q;

priority_queue< iii, viii, greater<iii> > Q;

int main()
{
    //pair <int, int> P;
    //cin >> P.first >> P.second;
    int n,a,b,c;
    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> a >> b >> c;
        Q.push({a,{b,c}});
    }

    for(int i = 0; i < n; i++){
        cout << Q.top().F << " " << Q.top().S.F << " " << Q.top().S.S << endl;
        Q.pop();
    }

    return 0;
}
