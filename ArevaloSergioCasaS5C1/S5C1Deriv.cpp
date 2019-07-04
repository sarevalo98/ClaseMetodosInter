#include<iostream>
#include <cmath>
using namespace std;

int derivada(float x0[], int valor, double dx)
    {
    float *p;
    float arr3[valor];
    p=arr3;
    for(int i=0; i<=valor;i++)
        {
            arr3[i]= (x0[i+1]-x0[i-1])/(2*dx);
        cout<< x0[i]<<";"<<arr3[i]<<endl;
        }
    cout<<"La direccion del arreglo calculado es: "<< p<<endl;
    return 0;
    }
 
int main()
    {
    int puntos;
    int a;
    int b;
    cout<<"Puntos: ";cin>>puntos;
    cout<<"a: ";cin>>a;
    cout<<"b: ";cin>>b;
    float * arr;
    arr=new float [puntos];
    arr[0]=a;
    arr[puntos]=b;
    double h=(b-a)/puntos;
    double c=a;
    for(int i=1;i<=puntos-1;i++)
        {
        c=c+h;
        arr[i]= c; 
        }
    float * arr2;
    arr2=new float [puntos];
    for(int i=0;i<=puntos;i++)
        {
        arr2[i]= cos(arr[i]);
        //cout<<arr2[i]<<endl;
        }
    derivada(arr2,puntos,h);
    return 0;
    }