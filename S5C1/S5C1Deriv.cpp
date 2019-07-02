#include<iostream>
using namespace std; 
//#include <cmath>

//int *¨derivada(int x0[])
//    {
    //for(int i=0; i<=x0.size();i++)
        //{
            //valor[i]= (x0[i+1]-funcion[i-1])/(2*h)
        //}
//    }
 
int main()
    {
    int puntos;
    int a;
    int b;
    cout<<"Ingrese el numero de puntos: ";cin>>puntos;
    cout<<"Ingrese el primer valor del intervalo: ";cin>>a;
    cout<<"Ingrese el ultimo valor del intervalo: ";cin>>b;
    float * arr;
    arr=new float [puntos];
    arr[0]=a;
    arr[puntos-1]=b;
    float h=(b-a)/puntos;
    int c=a;
    cout<<"me lleva "<<h<<endl;
    for(int i=1;i<=puntos-2;i++)
        {
        c=c+h;
        arr[i]= c; 
        }
    for(int i=0;i<=puntos;i++)
        {
        cout<<arr[i]<<endl;
        }
    return 0;
    }