#include <stdio.h>
#include <math.h>
#include <limits.h>
int main(int argc, char const *argv[])
{
	int resultados[3];
	int x,y,tst;
	scanf("%d",&tst);
	while(tst>0){
		scanf("%d",&x);
		scanf("%d",&y);
		resultados[0] = (pow(3*x,2))+(pow(y,2));
		resultados[1] = 2*(pow(x,2))+pow(5*y,2);
		resultados[2] = (-100*x) + pow(y,3);
		int i;
		int maior = INT_MIN;
		for (i = 0; i <=2; i++)
		{
			if (resultados[i]>maior)
			{
				maior = resultados[i];
				
			}
		}
		if(resultados[0]==maior){
			printf("Rafael ganhou\n");
		}
		if(resultados[1]==maior){
			printf("Beto ganhou\n");
		}
		if(resultados[2]==maior){
			printf("Carlos ganhou\n");
		}
		tst--;
	}
	return 0;
}