#include <fstream>
#include<iostream>
#include <cmath>
using namespace std;

int main()
    {
    double v=pow(10,-4);
    double T=50.0;
    double Tc=100.0;
    double dx=0.01;
    double dy=0.01;
    double dt=(0.5*dx)/v;
    double L=1.0;
    int N=(L-0)/dx;
    double plac[N][N];
    for(int i=0;i<N;i++)
        {
        for(int k=0;k<N;k++)
            {
            if(i<=60&&i>=40&&k<=40&&k>=20)
                {
                plac[i][k]=Tc;
                }
            else
                {
                plac[i][k]=T;
                }
            }
        }
    ofstream outfile;
    outfile.open("placa.txt");
    for(int i=0;i<N;i++)
        {
        for(int k=0;k<N;k++)
            {
            outfile<<plac[i][k]<<" ";
            }
        outfile<<"\n";
        }
    outfile.close();
    double placP[N][N];
    cout<<(v*dt)/(dx*dx)<<endl;
    for (int i=0;i<N;i++)
        for(int k=0;k<N;i++)
        {
        placP[i][k]=(v*dt)/(dx*dx);
        }
    return 0;
    }