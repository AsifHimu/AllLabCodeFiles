#include<bits/stdc++.h>
using namespace std;

string encrypt(string text,int shift){
    int l = text.size();
    string str = "";
    for(int i=0;i<l;i++){
        if(isupper(text[i])){
            char ch = (text[i] + shift - 'A') % 26 + 'A';
            str.push_back(ch);
        }
        if(islower(text[i])){
            char ch = (text[i] + shift - 'a') % 26 + 'a';
            str.push_back(ch);
        }
    }
    return str;
}
string decrypt(string text,int shift){
    int l = text.size();
    string str = "";
    for(int i=0;i<l;i++){
        if(isupper(text[i])){
            char ch = (text[i] + shift - 'A') % 26 + 'A';
            str.push_back(ch);
        }
        if(islower(text[i])){
            char ch = (text[i] + shift - 'a') % 26 + 'a';
            str.push_back(ch);
        }
    }
    return str;
}
int main(){
    string text;
    cout<<"Enter the original text: "<<endl;
    getline(cin,text);
    int shift;
    cout<<"How many shift to right?"<<endl;
    cin>>shift;
    string cipher;
    cipher = encrypt(text,shift);
    cout<<"Encrypted text: "<<endl;
    cout<<cipher<<endl;
    string original;
    original = decrypt(cipher,26-shift);
    cout<<"Decrypted text: "<<endl;
    cout<<original<<endl;
    return 0;
}
