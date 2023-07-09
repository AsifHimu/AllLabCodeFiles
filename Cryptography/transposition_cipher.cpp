#include<bits/stdc++.h>
using namespace std;

char mat[200][200];

string encryption(string s,int width){
    string encrypted;
    int len = s.size();
    int row = 0,col = 0;
    for(int i=0;i<len;i++){
        mat[row][col++] = s[i];
        if(col >= width){
            row++;
            col = 0;
        }
    }
    for(int i=0;i<width;i++){
        for(int j=0;j<=row;j++){
            if(mat[j][i] == 0){
                continue;
            }
            encrypted += mat[j][i];
        }
    }
    return encrypted;
}

string decryption(string s,int width){
    string decrypted;
    int len =s.size();
    int row = (len/width)+(len%width > 0);
    int k = 0;
    for(int i=0;i<width;i++){
        for(int j=0;j<row;j++){
            if(mat[j][i] == 0){
                continue;
            }
            mat[j][i] = s[k++];
        }
    }
    for(int i=0;i<row;i++){
        for(int j=0;j<width;j++){
            decrypted += mat[i][j];
        }
    }
    return decrypted;
}

int main(){
    freopen("input.txt","r",stdin);
    string s;
    getline(cin,s);
    string encrypted,decrypted;
    int width = 10;
    int iteration = 1;
    memset(mat,0,sizeof(mat));

    //Encryption
    for(int i=0;i<iteration;i++){
        encrypted = encryption(s,width);
        //s = encrypted;
    }
    cout<<"Encrypted text :"<<endl;
    cout<<encrypted<<endl;

    //Decryption
    decrypted = encrypted;
    for(int i=0;i<iteration;i++){
        decrypted = decryption(decrypted,width);
    }
    cout<<"Decrypted text :"<<endl;
    cout<<decrypted<<endl;
    return 0;
}
