#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	int quantidadeDeTeste;
	scanf("%d",&quantidadeDeTeste);
	int numero;
	int i;
	int j;
	int contador=0;
	int quantidade=0;
	while(quantidadeDeTeste!=0){

		scanf("%d",&numero);
			for(j=2; j <= numero; j++){
				contador =0;
				for(i=1 ; i<=j; i++){
					if (j%i==0)
					{
						contador++;
					}
				}
				if (contador%2==0)
				{
					quantidade++;
				}
				
			}
	printf("%d\n",quantidade);
	quantidade=0;
	quantidadeDeTeste--;
	}
	
	return 0;
}