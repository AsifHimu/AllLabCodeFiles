#include<bits/stdc++.h>
using namespace std;

class bisection{
public:
    double value(double x){
        return 3*x-cos(x)-1;
    }
    void calculate(double a,double b){
       /*while(true){
            a-=.5;
            b+=.5;
            if(value(a)*value(b)<0.0) break;
        }
        */
        if(value(a)*value(b) >= 0){
            cout<<"Incorrect input"<<endl;
            return;
        }
        double c;
        while((b-a)>=0.001){
            c=(a+b)/2;
            if(value(c) == 0.0){
                break;
            }
            else if(value(a)*value(c)<0){
                b=c;
            }
            else{
                a=c;
            }
        }
        cout<<"The value of the root is "<<c<<endl;
        //cout<<"values"<<a<<" "<<b<<endl;
    }
};

int main(){
    bisection ob;
    double a=-1,b=1;
    ob.calculate(a,b);
    return 0;
}
