#include <fstream>
#include<iostream>
using namespace std;



double fun2(double x0)
    {
    double m=2.0;
    double k=300.0;
    double j= -(k*x0)/m;
    return j;
    }
double fun(double v0)
    {
    return v0;
    }

double runge(double h0, float x0[], int num)
    {
    float arrx[num];
    arrx[0]=0.1;
    double k1;
    double k2;
    double k3;
    double k4;
    double prom;
    for(int i=1;i<=num;i++)
        {
        k1=h0*fun(arrx[i-1]);
        k2=h0*fun(arrx[i-1]+0.5*k1);
        k3=h0*fun(arrx[i-1]+0.5*k2);
        k4=h0*fun(arrx[i-1]+k3);
        prom=(1.0/6.0)*(k1+(2.0*k2)+(2.0*k3)+k4);
        arrx[i]=arrx[i-1]+prom;
        }
     ofstream outfile2;
     outfile2.open("runge.dat");
     for(int i=0;i<=num;i++)
         {
         outfile2 <<x0[i]<<";"<<arrx[i]<< endl;
         }
    outfile2.close();
    return 0;
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
    for(int i=1;i<=puntos-1;i++)
        {
        arrt[i]= arrt[i-1]+h;
        }
    runge(h,arrt,puntos);
    return 0;
    }