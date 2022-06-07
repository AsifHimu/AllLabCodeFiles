#include<bits/stdc++.h>
using namespace std;

class newtonRaphson{
public:
    double func(double x){
        return x*x*x-3*x+1;
    }
    double derivfunc(double x){
        return 3*x*x-3;
    }
    void calculate(double x1){
        for(int i=1;i<=100;i++){
           x1=x1-(func(x1)/derivfunc(x1));
        }
        cout<<"The value of the root is "<<x1<<endl;
    }
};

int main(){
    newtonRaphson ob;
    ob.calculate(0.9);
    return 0;
}
