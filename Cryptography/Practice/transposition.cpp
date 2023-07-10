#include<bits/stdc++.h>
using namespace std;

char mat[200][200];

string encryption(string text,int width){
    int l = text.size();
    int row = 0,col = 0;
    string encrypted;

    for(int i=0;i<l;i++){
        mat[row][col++] = text[i];
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

string decryption(string text,int width){
    string decrypted;
    int len = text.size();
    int row = (len/width) + (len%width > 0);
    int k = 0;

    for(int i=0;i<width;i++){
        for(int j=0;j<row;j++){
            if(mat[j][i] == 0){
                continue;
            }
            mat[j][i] = text[k++]; 
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
    string text;
    getline(cin,text);

    memset(mat,0,sizeof(mat));
    int width = 10;
    int iteration = 1;
    string encrypted,decrypted;
    cout<<"Input message:"<<text<<endl;
    for(int i=0;i<iteration;i++){
        encrypted = encryption(text, width);
        //text = encrypted;
    }
    cout<<"Encrypted message :"<<encrypted<<endl;

    for(int i=0;i<iteration;i++){
        decrypted = decryption(encrypted,width);
    }
    cout<<"Decrypted message :"<<decrypted<<endl;
    return 0;
}