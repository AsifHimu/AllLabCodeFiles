#include<bits/stdc++.h>
using namespace std;

string encrypt(string msg){
    string cipher = "",pad;

    ifstream input("random_string.txt");
    input>>pad;

    for(int i = 0; i < msg.size(); i++){
        if(isupper(msg[i])){
            cipher += (char)(((msg[i] - 'A') + (pad[i] - 'A')) % 26 + 'A');
        }
        else if(islower(msg[i])){
            cipher += (char)(((msg[i] - 'a') + (pad[i] - 'A')) % 26 + 'a');
        }
        else{
            cipher += msg[i];
        }
    }
    input.close();
    return cipher;
}

string decrypt(string cipher){
    string msg = "", pad;

    ifstream input("random_string.txt");
    input>>pad;

    for(int i = 0; i < cipher.size(); i++){
        if(isupper(cipher[i])){
            msg += (char)(((cipher[i] - 'A') - (pad[i] - 'A') + 26) % 26 + 'A');
        }
        else if(islower(cipher[i])){
            msg += (char)(((cipher[i] - 'a') - (pad[i] - 'A') + 26) % 26 + 'a');
        }
        else{
            msg += cipher[i];
        }
    }

    input.close();
    return msg;
}

int main(){
    freopen("in.txt","r",stdin);

    string msg;
    string cipher;

    getline(cin, msg);
    cout<<"Original message : "<<msg<<endl;

    cipher = encrypt(msg);
    msg = decrypt(cipher);

    cout<<"Encrypted message : "<<cipher<<endl;
    cout<<"Decrypted message : "<<msg<<endl;
    return 0;
}
