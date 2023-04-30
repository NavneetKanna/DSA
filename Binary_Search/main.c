#include <stdio.h>
#include <stdlib.h>


/*
When we pass an array to a function in C, we are actually passing a pointer to the first element of the array.
Therefore, the size of the array is not available inside the function, and you must pass it as a separate argument.
*/

int binary_search(int arr[], int size, int val){
    int low = 0;
    int high = size - 1;

    while(low<=high){
        int mid = (low+high) / 2;

        if(arr[mid] == val){
            return mid;
        }
        else if(arr[mid] < val){
                low = mid + 1;
        }
        else{
            high = mid - 1;
        }
    }
    return -1;
}


int main(){

    int test_list[] = {1, 3, 9, 11, 15, 19, 29};
    int size = sizeof(test_list) / sizeof(test_list[0]);

    int test_val1 = 25;
    int test_val2 = 15;

    int result1 = binary_search(test_list, size, test_val1);
    if (result1 == -1) {
        printf("%d does not exist\n", test_val1);
    } else {
        printf("%d found at index %d\n", test_val1, result1);
    }

    int result2 = binary_search(test_list, size, test_val2);
    if (result2 == -1) {
        printf("%d does not exist\n", test_val2);
    } else {
        printf("%d found at index %d\n", test_val2, result2);
    }

    return 0;

}
