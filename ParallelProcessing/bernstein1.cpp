#include<bits/stdc++.h>
using namespace std;

int main(){
/*  P1: C:=D*E;
    P2: M:=G+C;
    P3: A:=B+C;
    P4: C:=L+M;
    P5: F:=G/E;
*/
    freopen("input.txt","r",stdin);
    vector<vector<char>>in;
    vector<char>out;
    string str;
    while(getline(cin,str)){
        bool flag = true;
        vector<char>temp;
        for(int i=1;i<str.size();i++){
            if(flag && isalpha(str[i])){
                out.push_back(str[i]);
                flag = false;
            }
            else if(!flag && isalpha(str[i])){
                temp.push_back(str[i]);
            }
        }
        in.push_back(temp);
    }
    for(int i=0;i<in.size();i++){
        for(int j=i+1;j<in.size();j++){
            if(find(in[i].begin(),in[i].end(),out[j]) != in[i].end()){
                cout<<"p"<<i+1<<" and "<<"p"<<j+1<<" are "<<"Anti dependent\n";
                continue;
            }
            if(find(in[j].begin(),in[j].end(),out[i]) != in[j].end()){
                cout<<"p"<<i+1<<" and "<<"p"<<j+1<<" are "<<"Flow dependent\n";
                continue;
            }
            if(out[i] == out[j]){
                cout<<"p"<<i+1<<" and "<<"p"<<j+1<<" are "<<"Output dependent\n";
                continue;
            }
            cout<<"p"<<i+1<<" and "<<"p"<<j+1<<" are "<<"Parallel\n";
        }
    }
}
