#include<bits/stdc++.h>
using namespace std;

int main(){
    map<string,string>encry_dict;
    map<string,string>decry_dict;

    string input = "STWXYZMNO";
    ifstream dict("dictionary.txt");

    string line,key,value,encrypted,decrypted;
    while(getline(dict,line)){
        key = line.substr(0,3);
        value = line.substr(4,line.size());
        encry_dict[key] = value;
        decry_dict[value] = key;
    }
    for(int i=0;i<input.size();i+=3){
        encrypted += encry_dict[input.substr(i,3)];
    }
    for(int i=0;i<input.size();i+=3){
        decrypted += decry_dict[encrypted.substr(i,3)];
    }
    cout<<"Input message :"<<input<<endl;
    cout<<"Encrypted message:"<<encrypted<<endl;
    cout<<"Decrypted message:"<<decrypted<<endl;

    return 0;
}