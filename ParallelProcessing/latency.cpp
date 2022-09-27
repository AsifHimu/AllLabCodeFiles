#include<bits/stdc++.h>
using namespace std;

// function for calculating forbidden latency
vector <int> forbiddenLatency(vector <vector<int>> &arr) {
    set <int> s;
    int row = arr.size();
    int col = arr[0].size();

    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col-1; j++) {
            for (int k = j+1; k < col; k++) {
                if (arr[i][j] && arr[i][k]) {
                    s.insert(k-j);
                }
            }
        }
    }
    vector <int> res(s.begin(), s.end());
    return res;
}

// function for calculating permissible latency
vector <int> permissibleLatency(vector <int> &fl, int col) {
    vector <int> res;
    for (int i = 0, j = 0; i < col; i++) {
        if (i == fl[j]-1) {
            j++;
        } 
        else {
            res.push_back(i+1);
        }
    }
    return res;
}

// function for calculating collision vector
vector <int> collisionVector(vector<int> &fl) {
    int maxFLVal = fl[fl.size()-1];
    vector <int> res(maxFLVal);
    for (int i = 0, j = 0; i < maxFLVal; i++) {
        if (i == fl[j]-1) {
            res[i] = 1;
            j++;
        }
        else {
            res[i] = 0; 
        }
    }
    return res;
}
