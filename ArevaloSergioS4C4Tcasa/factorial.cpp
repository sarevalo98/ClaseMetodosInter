#include<iostream>
using namespace std;
int main()
    {
    int n=7;
    int a=1;
    for(double i=1;i<=n;i++)
        {a*=i;
        }
    cout<<"el factorial de 7 es: "<<a<<endl;
    int h=77;
    int q=1;
    for(int k=1;k<=h;k++)
        {q*=k;
        }
    cout<<"el factorial de 77 es: "<<q<<endl;
    cout<<"Si el contador es un entero el valor usando 77 es 0. Si el contador es un double el resultado es un numero negativo."<<endl;
    return 0;
    }