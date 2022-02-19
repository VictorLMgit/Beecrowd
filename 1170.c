#include <stdio.h>

int main(int argc, char const *argv[])
{
	int testes;
	scanf("%d",&testes);
	float estoque;
	int cont=0;
	int i;
	for ( i = 0; i < testes; i++)
	{
		scanf("%f",&estoque);
		cont =0;
		while(estoque>1){
			cont++;
			estoque = estoque/2;
		}
		printf("%d dias\n",cont );
	}
	return 0;
}