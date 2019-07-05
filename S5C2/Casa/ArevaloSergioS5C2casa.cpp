#include <fstream>
#include<iostream>
using namespace std;

//int derivada(float x0[], int valor, double dx)
    //{
    //float *p;
    //float arr3[valor];
    //p=arr3;
    //for(int i=0; i<=valor;i++)
        //{
            //arr3[i]= (x0[i+1]-x0[i-1])/(2*dx);
        //cout<< x0[i]<<";"<<arr3[i]<<endl;
        //}
    //cout<<"La direccion del arreglo calculado es: "<< p<<endl;
    //return 0;
    //}
double funcion(double x0)
    {
    double y= -x0;
    return y;
    }

int main()
    {
    int a=0;
    int b=2;
    double h=0.01;
    int puntos=(b-a)/h;
    float arrx[puntos];
    arrx[0]=a;
    arrx[puntos]=b;
    float arry[puntos];
    arry[0]=1;
    double c=arrx[0];
    double d=arry[0];
    //Euler
    for(int i=1;i<=puntos-1;i++)
        {
        c=c+h;
        arrx[i]= c;
        }
    for(int i=1;i<=puntos;i++)
        {
        d=d+h* funcion(arry[i-1]);
        arry[i]=d;
        }
    ofstream outfile;
    outfile.open("euler.dat");
    for(int i=0;i<=puntos;i++)
        {
        outfile <<arrx[i]<<";"<<arry[i]<< endl;
        }
    outfile.close();
    //Runge-Kutta
    double k_1;
    double k_2;
    double k_3;
    double k_4;
    double prom;
    float arry2[puntos];
    arry2[0]=1;
    double e=arry2[0];
    for(int i=1;i<=puntos;i++)
        {
        k_1= h* funcion(arry2[i-1]);
        k_2= h* funcion(arry2[i-1]+0.5*k_1);
        k_3= h* funcion(arry2[i-1]+0.5*k_2);
        k_4= h* funcion(arry2[i-1]+k_3);
        prom=(1.0/6.0)*(k_1+(2.0*k_2)+(2.0*k_3)+k_4);
        e=e+prom;
        arry2[i]=e;
        }
    ofstream outfile2;
    outfile2.open("runge.dat");
    for(int i=0;i<=puntos;i++)
        {
        outfile2 <<arrx[i]<<";"<<arry2[i]<< endl;
        }
    outfile2.close();
    return 0;
    }