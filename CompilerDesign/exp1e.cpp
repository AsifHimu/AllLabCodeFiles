#include <bits/stdc++.h>
using namespace std;

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
    if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u'||ch=='A'||ch=='E'||ch=='I'||ch=='O'||ch=='U'){
        return 1;
    }
    return 0;
}
void separate_vowel_and_consonant_word(char str[]){
    char str1[100],str2[100];
    int l1=0,l2=0;
    int sz=strlen(str);
    for(int i=0;i<sz;i++){
        if(is_vowel(str[i])){
            while(str[i]!=' ' && str[i]!='\0'){
                str1[l1++]=str[i++];
            }
            str1[l1++]=' ';
            i--;
        }
        else if(is_char(str[i])){
            while(str[i]!=' ' && str[i]!='\0'){
                str2[l2++]=str[i++];
            }
            str2[l2++]=' ';
            i--;
        }
    }
    str1[l1]='\0';
    str2[l2]='\0';
    cout<<"Words started with vowel :"<<str1<<endl;
    cout<<"Words started with consonant :"<<str2<<endl;
}
int main(){
    char p[500];
    cin.getline(p,500);
    separate_vowel_and_consonant_word(p);
    return 0;
}

