#include<bits/stdc++.h>
#define sz 10005
using namespace std;

char stck[sz];
int top=0;

void push(char ch){
    if(top>=sz){
        cout<<"stack overflow"<<endl;
    }
    else{
        top++;
        stck[top]=ch;
    }
}
char pop(){
    if(top<=0){
        cout<<"stack underflow"<<endl;
    }
    else{
        char ch=stck[top];
        top--;
        return ch;
    }
}
bool Operator(char x){
    if(x=='+'||x=='-'||x=='*'||x=='/'||x=='^'){
        return true;
    }
    else{
        return false;
    }
}
int precedence(char ch){
    if(ch=='^'){
        return 3;
    }
    else if(ch=='*'||ch=='/'){
        return 2;
    }
    else{
        return 1;
    }
}
int main(){
    int i,j,cnt=0,len;
    string a,res;
    //char ch;
    getline(cin,a);
    a.insert(0,"(");
    a.append(")");
    len=a.size();
    cout<<a<<endl;
    for(i=0;i<len;i++){
        if(a[i]=='('){
            push(a[i]);
        }
        else if(Operator(a[i])){
            while(precedence(a[i]) <= precedence(stck[top]) && Operator(stck[top])){
                res+=pop();
            }
            push(a[i]);
        }
        else if(a[i]==')'){
            while(stck[top]!='('){
                res+=pop();
            }
            pop();
        }
        else{
            res+=a[i];
        }
    }
    cout<<res<<endl;
    return 0;
}
