#include<bits/stdc++.h>
using namespace std;

char str[100];

int is_digit(char ch){
    if(ch>='0' && ch<='9'){
        return 1;
    }
    return 0;
}
int is_char(char ch){
    if(ch>='A'&&ch<='Z'){
        return 1;
    }
    if(ch>='a'&&ch<='z'){
        return 1;
    }
    return 0;
}
int is_vowel(char ch){
    if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u'){
        return 1;
    }
    return 0;
}
void count(){
    int cnt=1,letter_cnt=0,digit_cnt=0,others=0;
    for(int i=0;str[i];i++){
        if(str[i]==' '&&is_char(str[i+1])&&is_digit(i+1)){
            cnt++;
        }
        if(is_char(str[i])){
            letter_cnt++;
        }
        if(is_digit(str[i])){
            digit_cnt++;
        }
        if(!is_digit(str[i])&&!is_char(str[i])){
            others++;
        }
    }
}
int main()
