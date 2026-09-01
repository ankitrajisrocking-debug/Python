#include <stdio.h>

int main() {
	int arr[10], i, sum =0;
	float avg;
	
	printf("enter 10 integers:\n");
	for (i =0; i< 10; i++)
		scanf("%d", &arr[i]);
		
	printf("Array Elements: ");
	for(int i=0; i< 10; i++)
		printf("%d ", arr[i]);
		
	for (i =0; i< 10; i++)
		sum+= arr[i];
		
	avg = (float) sum/10;
	
	printf("\nSum = %d", sum);
	printf("\nAverage = %.2f\n", avg);
	
	return 0;
}
	
