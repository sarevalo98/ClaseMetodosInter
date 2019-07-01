#include<iostream>
using namespace std;
int main()
    {
    int n;
    int a=1;
    cout<<"Ingrese el valor de n:";cin>>n;
    for(int i=1;i<=n;i++)
        {a*=i;
        }
    cout<<"el factorial del valor dado es: "<<a<<endl;
    return 0;
    }