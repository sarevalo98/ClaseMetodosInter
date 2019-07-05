#include <fstream>
#include<iostream>
using namespace std;

int m=2;
int k=300;

double fun(double x0)
    {
    double a= -(k*x0)/m;
    return a;
    }
double fun2(double v0)
    {
    return v0;
    }

double runge(double dx, float x0[], int num)
    {
    double k_1;
    double k_2;
    double k_3;
    double k_4;
    double prom;
    float arrx[num];
    arrx[0]=0.1;
    double e=arrx[0];
    double k_5;
    double k_6;
    double k_7;
    double k_8;
    double prom_2;
    float arrv[num];
    arrv[0]=0;
    double d=arrv[0];
    for(int i=1;i<=num;i++)
        {
        k_1= dx* fun2(arrx[i-1]);
        k_2= dx* fun2(arrx[i-1]+0.5*k_1);
        k_3= dx* fun2(arrx[i-1]+0.5*k_2);
        k_4= dx* fun2(arrx[i-1]+k_3);
        prom=(1.0/6.0)*(k_1+(2.0*k_2)+(2.0*k_3)+k_4);
        e=e+prom;
        arrx[i]=e;
        k_5= dx* fun(arrv[i-1]);
        k_6= dx* fun(arrv[i-1]+0.5*k_5);
        k_7= dx* fun(arrv[i-1]+0.5*k_6);
        k_8= dx* fun(arrv[i-1]+k_7);
        prom_2=(1.0/6.0)*(k_5+(2.0*k_6)+(2.0*k_7)+k_8);
        d=d+prom_2;
        arrv[i]=d;
        }
    ofstream outfile2;
    outfile2.open("runge.dat");
    for(int i=0;i<=num;i++)
        {
        outfile2 <<x0[i]<<";"<<arrx[i]<<";"<<arrv[i]<< endl;
        }
    outfile2.close();
    }

int main()
    {
    int a=0;
    int b=5;
    double h=0.01;
    int puntos=(b-a)/h;
    float arrt[puntos];
    arrt[0]=a;
    arrt[puntos]=b;
    double c=arrt[0];
    for(int i=1;i<=puntos-1;i++)
        {
        c=c+h;
        arrt[i]= c;
        }
    runge(h,arrt,puntos);
    return 0;
    }