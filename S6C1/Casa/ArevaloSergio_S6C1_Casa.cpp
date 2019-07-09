#include <fstream>
#include<iostream>
using namespace std;

int main()
    {
    double v=1.0;
    double a=0.0;
    double b=2.0;
    int N=80;
    double dx=(b-a)/N;
    double dt= (dx/v)*0.25;
    double arrt[N];
    arrt[0]=a;
    arrt[N]=b;
    for(int i=1;i<=N-1;i++)
        {
        arrt[i]=arrt[i-1]+dx;
        }
    double arrv[N];
    for(int i=0;i<=N;i++)
        {
        if(arrt[i]>0.75 && arrt[i]<1.25)
            {
            arrv[i]=2;
            }
        else
            {
            arrv[i]=1;
            }
        }
    ofstream outfile;
    outfile.open("datos.dat");
    for(int i=0;i<=N;i++)
        {
        outfile <<arrt[i]<<";"<<arrv[i]<<endl;
        }
    outfile.close();
    double arrp[N];
    for(int i=0; i<=N;i++)
        {arrp[i]=arrv[i];
        for(int q=1; q<=N-1;q++)
            {
            arrv[q]=arrp[i]-v*dt/dx*(arrp[i]-arrp[i-1]);
            }
        }
    ofstream outfile2;
    outfile2.open("datos2.dat");
    for(int i=0; i<=N;i++)
        {
        outfile2<< arrt[i]<<";"<<arrv[i]<<endl;
        }
    outfile2.close();
    
    return 0;
    }