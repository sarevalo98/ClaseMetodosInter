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
    
    
    return 0;
    }