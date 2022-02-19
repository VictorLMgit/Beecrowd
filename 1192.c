#include <stdio.h>
#include <stdlib.h>
int main()
{
    char c;
    int a,b;
    
int resultado,n;
scanf("%d",&n);
int i;
for(i=0;i<n;i++){
    scanf("%d", &a);
    fflush(stdin);
    scanf("%c", &c);
    fflush(stdin);
    scanf("%d", &b);
    if(a==b){
        resultado=a*b;
    }
    else if(c>=65&&c<=90){
       resultado=b-a;
    }
    else if(c>=97&&c<=122){
        resultado=a+b;
    }
    printf("%d\n",resultado);
}
    return 0;
}