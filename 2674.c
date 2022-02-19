#include <stdio.h>
int primos(int n){
	int i;
	if (n==1||n==0)
	{
		return 0;
	}
	for(i = 2 ; i < n ; i++){
		if (n%i==0)
		{
			return 0;
		}
	}
	return 1;
}
int main(int argc, char const *argv[])
{
	
	int n;

	while(scanf("%d",&n)!=EOF){
	
	
	int aux;
	int i=0;
	aux = n;

	int armazem[100];
	while(n>10){
		armazem[i]=n%10;
		i++;
		n=n/10;
	}
	armazem[i]=n;
	int k;
	k=i;
	int cont1 =0;
	
	for(i = 0; i <= k ; i++){
		if (primos(armazem[i])==0)
		{
			cont1++;
			
		}
	}
	if (primos(aux)==1 && cont1 ==0)
	{
		printf("Super\n");
	}
	else if(primos(aux)==1 && cont1>0){
		printf("Primo\n");
	}
	else if (primos(aux)==0)
	{
		printf("Nada\n");
	}

	}
	
	return 0;
}