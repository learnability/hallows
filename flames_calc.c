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
		
		d=(c+i)%(j+1);
		if(d==0)
			i=j;
		else
			i=d-1;
		if(flames[i]!='$')
			flames[i]='$';
		else
		{
			while(flames[i]=='$')
			{	
				i++;
				if(i==j+1)
					i=0;
			}
			flames[i]='$';	
		}
		
		for(k=0; k<j; k++)
		{
			int h=k;
			if(flames[k]=='$')
			{
				while(h<j)
				{
					flames[h]=flames[h+1];
					h++;
					if(h==j+1)
					h=0;}
				
				}
			flames[j]='\0';	
		}
		printf("%s\n", flames);
		j--;
	}
	
	for(i=0; i<6; i++)
	{
		if(flames[i]!='$' && flames[i]!='\0')
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
		default: 	printf("error\n"); break;
		}
		
	return 0;
}
	
