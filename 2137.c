#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	int qtd;
	while(scanf("%d",&qtd)!=EOF){

	int i;
	int *vet;
	vet = (int*)malloc(sizeof(int)*qtd);
	for ( i = 0; i < qtd; i++)
	{
		scanf("%d",&vet[i]);
	}
	int j,aux;
	for(i = 0 ; i < qtd ; i++){
		for(j = 0 ;j < qtd-1 ; j++){
			if (vet[j]>vet[j+1])
			{
				aux = vet[j];
				vet[j] = vet[j+1];
				vet[j+1] = aux;
			}
		}
	}
	for ( i = 0; i < qtd; i++)
	{
		if (vet[i]<10)
		{
			printf("000%d\n",vet[i]);
		}
		else if (vet[i] >= 10 && vet[i]<100)
		{
			printf("00%d\n",vet[i]);
		}
		else if (vet[i]>=100&&vet[i]<1000)
		{
			printf("0%d\n",vet[i]);
		}
		else{
			printf("%d\n",vet[i]);
		}
		
	}
}
	return 0;
}