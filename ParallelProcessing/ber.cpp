#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    vector<vector<char>>in;
    vector<char>out;
    string s;

    while(getline(cin,s))
    {
        bool flag =true;
        vector<char>temp;
        for(int i=1; i<s.size(); i++){
            if(flag && isalpha(s[i])){
                out.push_back(s[i]);
                flag =false;
            }
            else if (!flag&& isalpha(s[i])){
                temp.push_back(s[i]);
            }
        }
        in.push_back(temp);
    }

    for(int i=0; i<in.size();i++){
        for(int j=i+1; j<in.size();j++){
            if(find (in[i].begin(), in[i].end(), out[j]) != in[i].end()){
                    cout<<"p"<<i+1<<"p"<<j+1<<"are anti-dependent.\n";
                    continue;

            }
            if(find (in[j].begin(), in[j].end(), out[i]) != in[j].end()){
                    cout<<"p"<<i+1<<"p"<<j+1<<"are follow-dependent.\n";
                    continue;
            }
            if(out[i]==out[j]){
                cout<<"p"<<i+1<<"p"<<j+1<<"are output-dependent.\n";
                continue;
            }
            cout<<"p"<<i+1<<"p"<<j+1<<"are parallel.\n";
        }
    }
    return 0;
}
