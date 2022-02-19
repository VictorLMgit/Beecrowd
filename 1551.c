#include <stdio.h>
#include <string.h>
int main(int argc, char const *argv[])
{
	
	char frase [1002];
	int n;
	int k;
	
	scanf("%d",&n);
	fgets(frase,1002,stdin);
	while(n!=0)
	{
		n--;
		fflush(stdin);
		fgets(frase,1002,stdin);
		int tam = strlen(frase);
		int j,i;
		int cont =0;
		char alfabeto[] = "abcdefghijklmnopqrstuvxwyz";

		for (i = 0; i < tam; i++)
		{
			for ( j = 0; j < 26; j++)
			{
				if (frase[i]==alfabeto[j])
				{
					cont++;
					alfabeto[j]='%';
				}
			}
		}

		if (cont >= 26)
		{
			printf("frase completa\n");
		}
		else if (cont >= 13)
		{
			printf("frase quase completa\n");
		}
		else{
			printf("frase mal elaborada\n");
		}
	}
	
	

	return 0;
}