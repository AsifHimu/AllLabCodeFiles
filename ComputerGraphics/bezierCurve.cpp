#include<bits/stdc++.h>
#include<conio.h>
#include<graphics.h>
using namespace std;

int getPt( int n1 , int n2 , float perc){
        return n1 + (n2 - n1)*perc;
}

int main(){
    ///10 10 100 150 150 300 400 100
   int xa, ya, xb, yb, xc, yc, x1, y1, x2, y2, x3, y3, x4, y4, x, y, a, b, c, d;
   cout<<"Enter 4 Points (x1,y1,x2,y2,x3,y3, x4, y4): ";
   cin>>x1>>y1>>x2>>y2>>x3>>y3>>x4>>y4;
	int gd = DETECT, gm;
   initgraph(&gd, &gm, "");
    setfillstyle(SOLID_FILL, RED);
   circle(x1,y1, 5);
    floodfill(x1,y1, WHITE);
   circle(x2,y2, 5);
    floodfill(x2,y2, WHITE);
   circle(x3,y3, 5);
    floodfill(x3,y3, WHITE);
   circle(x4,y4, 5);
    floodfill(x4,y4, WHITE);
    setcolor(WHITE);
    line(x1,y1,x2,y2);
    line(x2,y2,x3,y3);
    line(x3,y3,x4,y4);
    for( float i=0; i<1; i=i+0.00001 ){
        xa = getPt( x1 , x2 , i );
        ya = getPt( y1 , y2 , i );
        xb = getPt( x2 , x3 , i );
        yb = getPt( y2 , y3 , i );
        xc = getPt( x3 , x4 , i );
        yc = getPt( y3, y4 , i );

        a = getPt( xa , xb , i );
        b = getPt( ya , yb , i );
        c = getPt( xb , xc , i );
        d = getPt( yb , yc , i );

        x = getPt( a , c , i );
        y = getPt( b , d , i );

        putpixel( x , y , RED );
    }
    getch();
	closegraph();
    return 0;
}
