#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    char risada[52];
    char vogal []= {'a','e','i','o','u'};
    int i,j=0,c=0;
    char letrasrisada[52];
    char inverso[52];
    gets(risada);
    for(i=0; i<strlen(risada); i++)
    {
        for(j=0; j<5; j++)
        {
            if(risada[i]==vogal[j])
            {
                letrasrisada[c]=risada[i];
                c++;
            }
        }
    }
    letrasrisada[c]='\0';


    j=0;
    for(i=strlen(letrasrisada)-1; i>=0; i--)
    {
        inverso[j]=letrasrisada[i];
        j++;
    }
    inverso[j]='\0';

    int cont=0;
    for(i=0; i<strlen(letrasrisada); i++)
    {
        if(inverso[i]!=letrasrisada[i])
        {
            cont++;
        }
    }
    if(cont==0)
    {
        printf("S\n");
    }
    else
    {
        printf("N\n");
    }
    return 0;
}