#include<bits/stdc++.h>
using namespace std;

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
    if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u'||ch=='A'||ch=='E'||ch=='I'||ch=='O'||ch=='U'){
        return 1;
    }
    return 0;
}
void is_count(string str){
    int cnt=1,letter_cnt=0,digit_cnt=0,others=0;
    for(int i=0;i<str.size();i++){
        if(str[i]==' '&&(is_char(str[i+1])||is_digit(str[i+1]))){
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
    cout<<"Number of words: "<<cnt<<endl;
    cout<<"Number of letters: "<<letter_cnt<<endl;
    cout<<"Number of digits: "<<digit_cnt<<endl;
    cout<<"Others: "<<others<<endl;
    cout<<endl;
}
void separate(string str){
    string sep_letter,sep_digit,sep_other;
    for(int i=0;i<str.size();i++){
        if(is_char(str[i])){
            sep_letter+=str[i];
        }
        if(is_digit(str[i])){
            sep_digit+=str[i];
        }
        if(!is_digit(str[i])&&!is_char(str[i])){
            sep_other+=str[i];
        }
    }
    cout<<"All letter :"<<sep_letter<<endl;
    cout<<"All Digit :"<<sep_digit<<endl;
    cout<<"ALL Other :"<<sep_other<<endl;
    cout<<endl;
}
void vowel_and_consonant_count(string str){
    int vowel_cnt=0,consonant_cnt=0;
    for(int i=0;i<str.size();i++){
        if(is_vowel(str[i])){
            vowel_cnt++;
        }
        if(is_char(str[i])&&!is_vowel(str[i])){
            consonant_cnt++;
        }
    }
    cout<<"Vowel count :"<<vowel_cnt<<endl;
    cout<<"Consonant count :"<<consonant_cnt<<endl;
    cout<<endl;
}
void vowel_and_consonant(string str){
    string vowels,consonants;
    for(int i=0;i<str.size();i++){
        if(is_vowel(str[i])){
            vowels+=str[i];
        }
        if(is_char(str[i])&&!is_vowel(str[i])){
            consonants+=str[i];
        }
    }
    cout<<"Vowels :"<<vowels<<endl;
    cout<<"Consonants :"<<consonants<<endl;
    cout<<endl;
}
int main(){
    string s;
    getline(cin,s);
    is_count(s);
    separate(s);
    vowel_and_consonant_count(s);
    vowel_and_consonant(s);

    return 0;
}
