#include<bits/stdc++.h>
using namespace std;

map<string,string>encry_dict;
map<string,string>decry_dict;

void solve(){
    string input = "STWXYZMNO";
    string encrypted,decrypted;
    ifstream dict("dictionary.txt");
    ofstream output;

    //making dictionary
    string line,key,value;
    while(getline(dict,line)){
        key = line.substr(0,3);
        value = line.substr(4,line.size());
        encry_dict[key] = value;
        decry_dict[value] = key;
    }
    //Encryption
    for(int i=0;i<input.size();i+=3){
        encrypted += encry_dict[input.substr(i,3)];
    }
    //Decryption
    for(int i=0;i<input.size();i+=3){
        decrypted += decry_dict[encrypted.substr(i,3)];
    }
    cout<<"Input message: "<<input<<endl;
    cout<<"Encrypted message: "<<encrypted<<endl;
    cout<<"Decrypted message: "<<decrypted<<endl;
}

int main(){
    solve();
    return 0;
}
