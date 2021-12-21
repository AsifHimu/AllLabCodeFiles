#include<bits/stdc++.h>
using namespace std;

string str;

int is_alldigit(){
    for(int i=0;i<str.size();i++){
        if(str[i]>='0'&&str[i]<='9'){
            continue;
        }
        return 0;
    }
    return 1;
}
int is_valid(int start,int end){
    for(int i=start;i<=end;i++){
        if((str[i]>='a'&&str[i]<='z')||(str[i]>='A'&&str[i]<='Z')||(str[i]>='0'&&str[i]<='9')){
            continue;
        }
        return 0;
    }
    return 1;
}
int is_binary(){
    for(int i=0;i<str.size();i++){
        if(str[i]!='0'||str[i]!='1'){
            return 0;
        }
    }
    return 1;
}
int isFloat(){
    int cn=0,i;
    for(i=0;str[i]!='.';i++){
        if(str[i]=='.'){
            continue;
        }
        if(str[i]<'0'||str[i]>'9'){
            return 0;
        }
    }
    for(i++;str[i];i++){
        if(str[i]<'0'&&str[i]>'9'){
            return 0;
        }
        cn++;
    }
    return cn;
}
int main(){
    while(cin>>str){
        int len=str.size();
        if((str[0]>='i'&&str[0]<='n')||(str[0]>='I'&&str[0]<='N')){
            cout<<"Integar Variable"<<endl;
        }
        else if(len<=4 && (str[0]>='1'&&str[0]<='9') && is_alldigit()){
            cout<<"ShortInt Number"<<endl;
        }
        else if((str[0]>='1'&&str[0]<='9') && is_alldigit()){
            cout<<"LongInt Number"<<endl;
        }
        else if((str[0]>='a'&&str[0]<='h')||(str[0]>='A'&&str[0]<='H')||(str[0]>='o'&&str[0]<='z')||(str[0]>='O'&&str[0]<='Z')){
            cout<<"Float Variable"<<endl;
        }
        else if(str[0]=='c'&&str[1]=='h'&&str[2]=='_' && len>3 && is_valid(3,len-1)){
            cout<<"Character variable"<<endl;
        }
        else if(str[0]=='b'&&str[1]=='n'&&str[2]=='_'&&len>3 && is_valid(3,len-1)){
            cout<<"Binary Variable"<<endl;
        }
        else if(len>=2 && str[0]=='0' && is_binary()){
            cout<<"Binary Number"<<endl;
        }
        else if((isFloat()==2||isFloat()==1)&&((str[0]>='1'&&str[0]<='9')||str[0]=='.')){
            cout<<"Float Number"<<endl;
        }
        else if(isFloat()>2 && ((str[0]>='1'&&str[0]<='9')||str[0]=='.')){
            cout<<"Double Number"<<endl;
        }
        else if(!is_valid(0,len-1)){
            cout<<"Undefined"<<endl;
        }
        else{
            cout<<"Invalid Input"<<endl;
        }
    }
    return 0;
}
