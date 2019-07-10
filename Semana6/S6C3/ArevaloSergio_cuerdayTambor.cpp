#include <fstream>
#include<iostream>
using namespace std;

int main()
    {
    double a=0.0;
    double b=0.1;
    double L=1.0;
    double dx=0.005;
    double c=300.0;
    double dt= (dx*0.5)/c;
    int N=L/dx;
    double cond= c*dt/dx;
    double arrt[N];
    arrt[0]=a;
    arrt[N]=b;
    double arrAi[N];
    double arrAf[N];
    arrAi[N/2]=0.01;
    double arrx[N];
    arrx[0]=0.0;
    //Arreglo de X
    for(int i=1; i<=N;i++)
        {
        arrx[i]=arrx[i-1]+dx;
        }
    //Arreglo de tiempo
    for(int i=1;i<=N-1;i++)
        {
        arrt[i]=arrt[i-1]+dt;
        }
    //hago un arreglo para el primer paso
    for(int i=0;i<=N;i++)
        {
        arrAf[i]=0;
        }
    //Calculo posicion inicial
    for(int i=0;i<N/2;i++)
        {
        arrAi[i]=(2*0.01/L)*(i*dx);
        }
    for(int i=N/2;i<=N;i++)
        {
        arrAi[i]= (-2*0.01/L)*i*dx+(2*0.01);
        }
    //Agrego a un archivo .dat las posiciones X y las condiciones iniciales.
    ofstream outfile;
    outfile.open("datos.dat");
    for(int i=0; i<=N;i++)
        {
        outfile<<arrx[i]<<";"<<arrAi[i]<<endl;
        }
    outfile.close();
    //Primer paso...
    for(int i=0;i<=N;i++)
        {
         arrAf[i]=(((c*c)*(dt*dt))/(2*dx*dx))*(arrAi[i+1]+arrAi[i-1]-(2*arrAi[i]))+arrAi[i];
        }
    double arrf[N];
    int conta=0;
    ofstream outfile3;
    outfile3.open("datos3.dat");
    for(int k=0;k<=N+200;k++)
        {
        conta = conta+1;
        for(int i=1;i<=N-1;i++)
            {
             arrf[i]=(((c*c)*(dt*dt))/(dx*dx))*(arrAf[i+1]+arrAf[i-1]-(2*arrAf[i]))-arrAi[i]+(2*arrAf[i]);
            if(conta%10==0)
            {
            outfile3<<arrx[i]<<";"<<arrf[i]<<endl;
            }
            }
        for(int i=1;i<=N-1;i++)
            {
            arrAi[i]=arrAf[i];
            arrAf[i]=arrf[i];
            }
     }
    outfile3.close();
    return 0;
    }