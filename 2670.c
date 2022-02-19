#include <stdio.h>
#include <limits.h>
int main(int argc, char const *argv[])
{
	int andar1;
	int andar2;
	int andar3;
	int aux[3];
	scanf("%d",&andar1);
	scanf("%d",&andar2);
	scanf("%d",&andar3);

	aux[0] = (andar2*2)+(andar3*4);
	aux[1] = (andar3*2)+(andar1*2);
	aux[2] = (andar1*4)+(andar2*2);
	int i;
	int menor=INT_MAX;
	for ( i = 0; i <3 ; i++)
	{
		if (aux[i] < menor)
		{
			menor=aux[i];
		}
	}
	printf("%d\n",menor );

	
	return 0;
}