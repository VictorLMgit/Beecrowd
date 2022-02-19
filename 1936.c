#include <stdio.h>

int fat(int i){
	if (i==0)
	{
		return 1;
	}
	else {
		return i*fat(i-1);
	}
}
int main(int argc, char const *argv[])
{
	int k;
	int cont=0;
	scanf("%d",&k);
	
	
		while(fat(8)<=k){
		cont++;
		k=k-fat(8);
		}
	
		while(fat(7)<=k){
			cont++;
			k=k-fat(7);
		}
	

		while(fat(6)<=k){
				cont++;
				k=k-fat(6);
			}
	
		while(fat(5)<=k){
			cont++;
			k=k-fat(5);
		}
	
		while(fat(4)<=k){
			cont++;
			k=k-fat(4);
		}
	
	
		while(fat(3)<=k){
			cont++;
			k=k-fat(3);
		}
	
	
		while(fat(2)<=k){
			cont++;
			k=k-fat(2);
		}
	
	
		while(fat(1)<=k){
			cont++;
			k=k-fat(1);
		}
	
	printf("%d\n",cont );
	return 0;
}