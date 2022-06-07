#include<bits/stdc++.h>
using namespace std;

class falsePosition{
public:
    double value(double x){
        return x*x*x-4*x-9;
    }
    double x2,cnt;
    void calculate(double x0,double x1){
        if(value(x0)*value(x1) >= 0){
            cout<<"Incorrect input"<<endl;
            return;
        }
        for(int i=1;i<=100;i++){
            x2 = (x0*value(x1) - x1*value(x0))/(value(x1) - value(x0));
            if(value(x2)==0.0){
                break;
            }
            else if(value(x0)*value(x2)>0){
                x0=x2;
            }
            else{
                x1=x2;
            }
        }
        cout<<"The value of the root is "<<x2<<endl;
    }
};
int main(){
    falsePosition ob;
    ob.calculate(-9,6);
    return 0;
}

/*
        do{
            tmp=x2;
            x2 = (x0*value(x1) - x1*value(x0))/(value(x1) - value(x0));
            if(value(x2)==0.0){
                break;
            }
            else if(value(x0)*value(x2)>0){
                x0=x2;
            }
            else{
                x1=x2;
            }
        }while(tmp-x2 >= 0.0001);
*/
