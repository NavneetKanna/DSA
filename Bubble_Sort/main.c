#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void bubble_sort(int arr[], int size){
    bool swapped = true;

    while(swapped){
        swapped = false;
        for(int i=0; i<size-1; i++){
            if(arr[i] > arr[i+1]){
                swapped = true;
                int temp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = temp;
            }
        }
        size = size - 1;
    }
}

int main(){
    int arr[] = {7, 4, 9, 1, 5};
    int size = sizeof(arr) / sizeof(arr[0]);

    bubble_sort(arr, size);

    printf("Sorted array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;


}
