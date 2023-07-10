#include<bits/stdc++.h>
using namespace std;

string encrypt(string msg){
    int l = msg.size();
    string encrypted = "",pad;
    ifstream input("random_string.txt");
    input>>pad;
    for(int i=0;i<l;i++){
        if(isupper(msg[i])){
            char ch = ((msg[i] - 'A') + (pad[i] - 'A')) % 26 + 'A';
            encrypted.push_back(ch);
        }
        else if(islower(msg[i])){
            char ch = ((msg[i] - 'a') + (pad[i] - 'A')) % 26 + 'a';
            encrypted.push_back(ch);
        }
        else{
            encrypted.push_back(msg[i]);
        }
    }
    input.close();
    return encrypted;
}

string decrypt(string cipher){
    int l = cipher.size();
    string decrypted = "",pad;
    ifstream input("random_string.txt");
    input>>pad;
    for(int i=0;i<l;i++){
        if(isupper(cipher[i])){
            char ch = ((cipher[i] - 'A') - (pad[i] - 'A') + 26) % 26 + 'A';
            decrypted.push_back(ch);
        }
        else if(islower(cipher[i])){
            char ch = ((cipher[i] - 'a') - (pad[i] - 'A') + 26) % 26 + 'a';
            decrypted.push_back(ch);
        }
        else{
            decrypted.push_back(cipher[i]);
        }
    }
    input.close();
    return decrypted;
}

int main(){
    freopen("input.txt","r",stdin);
    string text,cipher,decrypted;
    getline(cin,text);
    cipher = encrypt(text);
    cout<<"Input text: "<<text<<endl;
    cout<<"Encrypted text: "<<cipher<<endl;
    decrypted = decrypt(cipher);
    cout<<"Decrypted text: "<<decrypted<<endl;
    return 0;
}