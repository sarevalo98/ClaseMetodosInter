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
    double dt=(0.5*dx*dx)/v;
    double L=1.0;
    int N=(L-0)/dx;
    double plac[N][N];
    for(int i=0;i<N;i++)
        {
        for(int k=0;k<N-1;k++)
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
    double placf[N][N];
 
    for(double t=0.0;t<2501.0;t+=dt)
        {
        for (int i=1;i<N-1;i++)
            {
            for(int k=1;k<N-1;k++)
                {
                placf[i][k]=((v*dt)/(dx*dx))*(plac[i+1][k]+plac[i-1][k]-(2*plac[i][k]))+((v*dt)/(dy*dy))*(plac[i][k+1]+plac[i][k-1]-(2*plac[i][k]))+plac[i][k];
                plac[i][k]=placf[i][k];
                }
            }
        if(t==100)
            {
            ofstream outfile2;
            outfile2.open("placa2.txt");
            for(int w=0;w<N;w++)
                {
                for(int h=0;h<N;h++)
                    {
                     outfile2<<placf[w][h]<<" ";
                     }
                 outfile2<<"\n";
                 }
                 outfile2.close();
                 }
             if(t==2500)
                 {ofstream outfile3;
                  outfile3.open("placa3.txt");
                  for(int w=0;w<N;w++)
                      {
                      for(int h=0;h<N;h++)
                          {
                           outfile3<<placf[w][h]<<" ";
                          }
                      outfile3<<"\n";
                      }
                   outfile3.close();
                  }
        }
    return 0;
    }