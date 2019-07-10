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
    int N= 200;
    double cond= c*dt/dx;
    double arrt[N];
    arrt[0]=a;
    arrt[N]=b;
    double arrAi[N];
    double arrAf[N];
    arrAi[N/2]=0.01;
    double arrx[N];
    arrx[0]=0.0;
    for(int i=1; i<=N;i++)
        {
        arrx[i]=arrx[i-1]+dx;
        }
    for(int i=1;i<=N-1;i++)
        {
        arrt[i]=arrt[i-1]+dt;
        }
    for(int i=0;i<=N;i++)
        {
        arrAf[i]=0;
        }
    for(int i=0;i<N/2;i++)
        {
        arrAi[i]=(2*0.01/L)*(i*dx);
        }
    for(int i=N/2;i<=N;i++)
        {
        arrAi[i]= (-2*0.01/L)*i*dx+(2*0.01);
        }
    ofstream outfile;
    outfile.open("datos.dat");
    for(int i=0; i<=N;i++)
        {
        outfile<<arrx[i]<<";"<<arrAi[i]<<endl;
        }
    outfile.close();
    for(int i=0;i<=N;i++)
        {
         arrAf[i]=(1/2)*(((c*c)*(dt*dt))/(dx*dx))*(arrAi[i+1]+arrAi[i-1]-(2*arrAi[i]))+(2*arrAi[i]);
        }
    ofstream outfile2;
    outfile2.open("datos2.dat");
    for(int i=0; i<=N;i++)
        {
        outfile2<<arrx[i]<<";"<<arrAf[i]<<endl;
        }
    outfile2.close();
    double arrf[N];
    for(int i=0;i<=N;i++)
        {
        for(int j=0;j<=N;j++)
            {
            arrf[j]= (2.0*(1.0-(cond*cond)))*arrAf[i] - arrAi[i] + (cond*cond)*(arrAf[i+1] +  arrAf[i-1]);
            }
        }
    ofstream outfile3;
    outfile3.open("datos3.dat");
    for(int i=0; i<=N;i++)
        {
        outfile3<<arrx[i]<<";"<<arrf[i]<<endl;
        }
    outfile3.close();
    return 0;
    }