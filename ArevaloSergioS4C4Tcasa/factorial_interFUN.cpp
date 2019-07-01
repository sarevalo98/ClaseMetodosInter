#include<iostream>
using namespace std;
int factorial(int n, int a=1)
    {
    for(int i=1;i<=n;i++)
        {a*=i;
        }
    cout<<"el factorial del valor dado es: "<<a<<endl;
    return 0;
    }
int main()
    {
    int n;
    cout<<"Ingrese el valor de n:";cin>>n;
    factorial(n);
    return 0;
    }