// 1       1       1       1       1
// 2       2       2       2       2
// 3       3       3       3       3
// 4       4       4       4       4
// 5       5       5       5       5

#include<stdio.h>
void main(){
    int i, j, r, c;
    printf("Enter the number of rows: \n");
    scanf("%d", &r);
    printf("Enter the number of column: \n");
    scanf("%d", &c);
    for(i=1; i<=r; i++){
        for(j=1; j<=c; j++){
            printf("%d\t", i);
        }
        printf("\n");
    }
}
