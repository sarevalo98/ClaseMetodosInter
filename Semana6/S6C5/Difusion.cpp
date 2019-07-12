#include <fstream>
#include<iostream>
#include <cmath>
using namespace std;

int main()
    {
    double L=1.0;
    double v= pow(10,-4);
    double dx=0.01;
    double dy=0.01;
    double dt=(0.05*(dx*dx))/v;
    int N=100;
    double inicial[N][N];
    for(int i=0;i<=N-1;i++)
        {
        for(int k=0;k<=N-1;k++)
            {
            if(i<60&&i>40&&k<40&&k>20)
                {
                inicial[i][k]=100.0;
                }
            else
                {
                inicial[i][k]=50.0;
                }
            }
        }
    ofstream outfile;
    outfile.open("placa.txt");
    for(int i=0;i<=N-1;i++)
        {
        for(int k=0;k<=N-1;k++)
            {
            outfile<<inicial[i][k]<<" ";
            }
        outfile<<"\n";
        }
    outfile.close();
    double pasito[N][N];
    for(float t=0;t<100;t+=dt)
        {
        for(int i=1;i<N-1;i++)
            {
            for(int k=1;k<N-1;k++)
                {
                pasito[i][k]=((v*dt)/(dx*dx))*(inicial[i+1][k]+inicial[i-1][k]-(2*inicial[i][k]))+((v*dt)/(dy*dy))*(inicial[i][k+1]+inicial[i][k-1]-(2*inicial[i][k]))+inicial[i][k];
                inicial[i][k]=pasito[i][k];
                }
            }
        }
    ofstream outfile2;
    outfile2.open("placa2.txt");
    for(int i=0;i<=N-1;i++)
        {
        for(int k=0;k<=N-1;k++)
            {
            outfile2<<inicial[i][k]<<" ";
            }
        outfile2<<"\n";
        }
    outfile2.close();
    //Paso2500
    for(float t=0;t<2400;t+=dt)
        {
        for(int i=1;i<N-1;i++)
            {
            for(int k=1;k<N-1;k++)
                {
                pasito[i][k]=((v*dt)/(dx*dx))*(inicial[i+1][k]+inicial[i-1][k]-(2*inicial[i][k]))+((v*dt)/(dy*dy))*(inicial[i][k+1]+inicial[i][k-1]-(2*inicial[i][k]))+inicial[i][k];
                inicial[i][k]=pasito[i][k];
                }
            }
        }
    ofstream outfile3;
    outfile3.open("placa3.txt");
    for(int i=0;i<=N-1;i++)
        {
        for(int k=0;k<=N-1;k++)
            {
            outfile3<<inicial[i][k]<<" ";
            }
        outfile3<<"\n";
        }
    outfile3.close();
    return 0;
    }