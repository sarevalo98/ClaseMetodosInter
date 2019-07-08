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
    double dt= 
    double arrt[N];
    arrt[0]=a;
    arrt[N]=b;
    for(int i=1;i<=N-1;i++)
        {
        arrt[i]=arrt[i-1]+h;
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
    
    return 0;
    }