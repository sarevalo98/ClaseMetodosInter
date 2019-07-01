#include<iostream>
using namespace std;

int primos(int a,int b)
    {
     for(int i=a; i<=b;i++)
        {int c=0;
        for(int h=1; h<=b;h++)
            {if(i%h==0)
                {c++;
                }
            }
         if(c==2)
                {cout<< i << " es un numero primo" <<endl;
                }
        }
    return 0;
    }
int main()
    {
    int a;
    int b;
    cout<<"Ingrese el valor de a:";cin>>a;
    cout<<"Ingrese el valor de b:";cin>>b;
    primos(a,b);
    return 0;
    }
