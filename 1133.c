#include <stdio.h>

int main(int argc, char const *argv[])
{
	int n,f;
	int i;
	scanf("%d",&n);
	scanf("%d",&f);

	if (n<f)
	{	
		for ( i = n+1; i < f; i++)
		{
			if (i%5==2 || i%5==3)
			{
				
				printf("%d\n",i);
			}
			
		}
	}
	else{
		for ( i = f+1; i < n; i++)
		{
			if (i%5==2 || i%5==3)
			{
				
				printf("%d\n",i);
			}
			
		}
	}
	return 0;
}