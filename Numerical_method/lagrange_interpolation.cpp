#include<bits/stdc++.h>
using namespace std;

class lagrange{
    double x[500],y[500];
    int n;
public:
    lagrange(int n,double ar[],double br[]){
        this->n = n;
        for(int i=0;i<n;i++){
            x[i] = ar[i];
            y[i] = br[i];
        }
    }
    double calculate(double val){
        double ans = 0;
        for(int i=0;i<n;i++){
            double p=1;
            for(int j=0;j<n;j++){
                if(i==j){
                    continue;
                }
                p=p*((val-x[j])/(x[i]-x[j]));
            }
            ans=ans+p*y[i];
        }
        return ans;
    }
};
int main(){
    int i,j,n;
    cin>>n;
    double x[n+10],y[n+10],val;
    for(i=0;i<n;i++){
        cin>>x[i]>>y[i];
    }
    cin>>val;
    lagrange lr = lagrange(n,x,y);
    cout<<lr.calculate(val)<<endl;
}
