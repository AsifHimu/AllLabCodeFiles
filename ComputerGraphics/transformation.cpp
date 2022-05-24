#include<bits/stdc++.h>
#include<graphics.h>
using namespace std;

int main(){
    int gd = DETECT,gm = DETECT,selection;
    initgraph(&gd,&gm,"");
    cout<<"1.Translation\n2.Scaling\n3.Rotation\n"<<endl;
    cout<<"selection for transformation\n";
    cin>>selection;
    switch(selection){
        case 1:{
            int x1=100,y1=100,x2=200,y2=200;
            int tx=50,ty=50;
            cout<<"Rectangle before translation\n";
            setcolor(RED);
            rectangle(x1,y1,x2,y2);
            cout<<"Rectangle after translation\n";
            setcolor(WHITE);
            rectangle(x1+tx,y1+ty,x2+tx,x2+ty);
            getch();
            break;
        }
        case 2:{
            int x1=30,y1=30,x2=70,y2=70;
            int x=2,y=2;
            cout<<"Rectangle before scaling\n";
            setcolor(RED);
            rectangle(x1,y1,x2,y2);
            cout<<"Rectangle after scaling\n";
            setcolor(WHITE);
            rectangle(x1*x,y1*y,x2*x,y2*y);
            getch();
            break;
        }
        case 3:{
            long x1=200,y1=200,x2=300,y2=300;
            double a;
            cout<<"line with rotation"<<endl;
            setcolor(RED);
            line(x1,y1,x2,y2);
            cout<<"Angle of rotation:";
            cin>>a;
            a=(a*3.14)/180;
            long xr=x1+((x2-x1)*cos(a)-(y2-y1)*sin(a));
            long yr=y1+((x2-x1)*sin(a)+(y2-y1)*cos(a));
            setcolor(WHITE);
            line(x1,y1,xr,yr);
            getch();
            break;
        }
        default:{
            cout<<"Invalid selection\n";
            break;
        }
    }
    closegraph();
    return 0;
}

