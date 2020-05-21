#include<bits/stdc++.h>
using namespace std;
vector<int> vec;
int main()
{
    int q;
    cin>>q;
    for(int i=1;i<q;i++)
    {
        char ch;
        cin>>ch;
        if(ch=='+')
        {
            int x;
            cin>>x;
            vec.push_back(x);
            sort(vec.begin(),vec.end());
        }
        else
        {
            int l,r;
            cin>>l>>r;
            cout<<upper_bound(vec.begin(),vec.end(),r)-lower_bound(vec.begin(),vec.end(),l)<<endl;
        }
 
    }
}
 
 
