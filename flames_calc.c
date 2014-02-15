#include <stdio.h>
#include "flinp.c"
int main()
{
	int c, i, j, d, k;
	char result;
	char flames[7] = {'f', 'l', 'a', 'm', 'e', 's' };
	c=count();
	printf("%d\n", c);
	j=5;
	i=0;
	while(j)
	{
		
		//k=(c+i+1)/(j+1);
		d=(c+i+1)%(j+1);
		if(d==0)
			i=5;
		else
			i=d-1;
		if(flames[i]!='$')
			flames[i]='$';
		else
		{
			while(flames[i]=='$')
			{	
				i++;
				if(i==6)
					i=0;
			}
			flames[i]='$';	
		}
		printf("%d\n", i);
		j--;
				
				
	}
	
	for(i=0; i<6; i++)
	{
		if(flames[i]!='$')
			result=flames[i];
	}
	printf("result %c\n", result);
	printf("%s\n", flames);
	switch(result)
		{
		case 'f':	printf("Friends :)\n"); break;
		case 'l':	printf("Lovers  <3\n");	break;
		case 'a':	printf("Aquantances :)\n"); break;
		case 'm':	printf("Married...!!!\n"); break;
		case 'e':	printf("Enemies :P\n"); break;
		case 's':	printf("Sisters or well..brothers :D\n"); break;
		default: 	printf("error\n");
		}
		
	return 0;
}
	
