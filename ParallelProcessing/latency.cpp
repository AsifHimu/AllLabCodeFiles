#include<bits/stdc++.h>
using namespace std;

vector<int> forbiddenlatency(vector<vector<int>>arr){
    set<int>s;
    int row = arr.size();
    int col = arr[0].size();
    for(int i=0;i<row;i++){
        for(int j=0;j<col-1;j++){
            for(int k=j+1;k<col;k++){
                if(arr[i][j] && arr[i][k]){
                    s.insert(k-j);
                }
            }
        }
    }
    vector<int>res(s.begin(),s.end());
    return res;
}
vector<int> permissablelatency(vector<int>fl,int col){
    vector<int>res;
    int j=0;
    for(int i=1;i<=col;i++){
        if(i == fl[j]){
            j++;
        }
        else{
            res.push_back(i);
        }
    }
    return res;
}
vector<int> collisionvector(vector<int>fl){
    int mxfl = fl[fl.size()-1];
    vector<int>res;
    int j=0;
    for(int i=1;i<=mxfl;i++){
        if(i == fl[j]){
            res.push_back(1);
            j++;
        }
        else{
            res.push_back(0);
        }
    }
    return res;
}
int main(){
    freopen("reservation-table.txt","r",stdin);
    int row,col,value;
    cin>>row>>col;
    vector<vector<int>>vec;
    for(int i=0;i<row;i++){
        vector<int>v1;
        for(int j=0;j<col;j++){
            cin>>value;
            v1.push_back(value);
        }
        vec.push_back(v1);
    }
    //ForbiddenLatency
    vector<int>fl = forbiddenlatency(vec);
    cout<<"ForbiddenLatency : ";
    for(int i=0;i<fl.size();i++){
        cout<<fl[i]<<" ";
    }
    cout<<endl;
    //PermissableLatency
    vector<int>pl = permissablelatency(fl,col);
    cout<<"PermissableLatency : ";
    for(int i=0;i<pl.size();i++){
        cout<<pl[i]<<" ";
    }
    cout<<endl;
    //Collsiionvector
    vector<int>cv = collisionvector(fl);
    reverse(cv.begin(),cv.end());
    cout<<"CollisionVector : ";
    for(int i=0;i<cv.size();i++){
        cout<<cv[i]<<" ";
    }
    cout<<endl;
}
