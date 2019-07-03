#include<iostream>
using namespace std;

int producto(int a[],int b[])
    {
    int C[5];
    for (int i=0; i<=4;i++)
        {
         C[i]=a[i]*b[i];
        cout<<C[i]<<endl;
        }
    return 0;
    }
int punto(int a[], int b[])
    {
    int C[5];
    int H=0;
    for (int i=0; i<=4;i++)
        {
         C[i]=a[i]*b[i];
         H+=C[i];
        }
    cout<<"El producto punto da: "<<H<<endl;
    return 0;
    }
int main()
    {
    int A[] = {1,2,3,4,5};
    int B[] = {10,20,30,40,50};
    producto(A,B);
    punto(A,B);
    return 0;
    }