#include <stdio.h>
#include <string.h>

int arr[26];

int count() {
  char name1[30], name2[30];
  int l1, l2, i, ct;
  
  printf("Enter name1: ");
  scanf("%s", name1);
  
  printf("Enter name2: ");
  scanf("%s", name2);
  
  for(i = 0; i < 26; i++)
    arr[i] = 0;
  
  l1 = strlen(name1);
  l2 = strlen(name2);

  for(i = 0; i < l1; i++)
    arr[name1[i] - 'a'] = arr[name1[i] - 'a'] + 1;
  
  ct = 0;
  
  for(i = 0; i < l2; i++)
    if(arr[name2[i] - 'a'] > 0){
      ct++;
      arr[name2[i] - 'a']--;
    }
  
  return l1 + l2 - 2 * ct;
}

char flames_calc(int count) {
  char flames[] = "flames";
  int a, i, l1, j;
  a = 6;
  i = 0;
  
  while(a > 1) {
    l1 = strlen(flames);
    i = (count + i - 1)%l1;
    
    for(j = i; j < l1 - 1; j++)
      flames[j] = flames[j + 1];
    flames[l1 - 1] = '\0';
    a--;
  }
  return flames[0];
}

