#include<bits/stdc++.h>
using namespace std;

class secant{
public:
    double value(double x){
        return x*x*x-x-1;
    }
    void calculate(double x0,double x1){
        if(value(x0)*value(x1) >= 0){
            cout<<"Incorrect input"<<endl;
            return;
        }
        double x2;
        while(abs(x1-x0) >= 0.0001){
            x2 = (x0*value(x1)-x1*value(x0))/(value(x1)-value(x0));
            x0=x1;
            x1=x2;
        }
        cout<<"The value of the root is "<<x2<<endl;
    }
};
int main(){
    secant ob;
    ob.calculate(1.3,1.4);
    return 0;
}
