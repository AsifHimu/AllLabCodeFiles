#include<bits/stdc++.h>
using namespace std;

string encryption(string text,int shift){
    int l = text.size();
    string encrypted = "";
    for(int i=0;i<l;i++){
        if(isupper(text[i])){
            char ch = (text[i] + shift - 'A') % 26 + 'A';
            encrypted.push_back(ch);
        }
        if(islower(text[i])){
            char ch = (text[i] + shift - 'a') % 26 + 'a';
            encrypted.push_back(ch);
        }
    }
    return encrypted;
}

string decryption(string text,int shift){
    int l = text.size();
    string decrypted = "";
    for(int i=0;i<l;i++){
        if(isupper(text[i])){
            char ch = (text[i] + shift - 'A') % 26 + 'A';
            decrypted.push_back(ch);
        }
        if(islower(text[i])){
            char ch = (text[i] + shift - 'a') % 26 + 'a';
            decrypted.push_back(ch);
        }
    }
    return decrypted;
}

int main(){
    cout<<"Enter the original text :"<<endl;
    string text;
    getline(cin,text);
    int shift;
    cout<<"How many shift to right?"<<endl;
    cin>>shift;
    string cipher = encryption(text,shift);
    cout<<"Encrypted message: "<<cipher<<endl;
    string decrypt = decryption(cipher,26-shift);
    cout << "Decrypted message: " << decrypt << endl;
}