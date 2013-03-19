/* A quicksort implementation in c
 * Spring 2013
 * By Andy Sayler
 * http://www.andysayler.com
 */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

inline void swap(void* a, void* b, size_t size){

    void* tmp = malloc(size);
    if(tmp == NULL){
	perror("swap: malloc of 'tmp' failed");
	return;
    }

    memcpy(tmp, a, size);
    memcpy(a, b, size);
    memcpy(b, tmp, size);

    return;
}

inline int partition(void* array, int left, int right, int pivot, size_t size, int (*compare)(const void*, const void*)){

    int i;
    void* ip = NULL;
    int store = left;
    void* storep = array + (store * size);
    void* rightp = array + (right * size);
 
    swap(rightp, (array + (pivot * size)), size);
    
    for(i = left; i < right; i++){
	ip = array + (i * size);
	if(compare(ip, rightp) < 0){
	    swap(ip, storep, size);
	    store++;
	    storep = array + (store * size);
	}
    }
    swap(rightp, storep, size);

    return store;
}

void quicksort(void* array, int left, int right, size_t size, int (*compare)(const void*, const void*)){

    int pivot;

    if(left < right){
	pivot = ((right - left) / 2) + left;
	pivot = partition(array, left, right, pivot, size, compare);
	quicksort(array, left, (pivot - 1), size, compare);
	quicksort(array, (pivot + 1), right, size, compare);
    }

    return;
}

void sort(void* array, size_t len, size_t size, int (*compare)(const void*, const void*)){
    
    quicksort(array, 0, len-1, size, compare);
    
    return;
}

int cmpint (const void * a, const void * b){

    const int* vala = a;
    const int* valb = b;

    return (*vala - *valb);
}

int main(){

    int values[] = { 40, 10, 100, 90, 20, 25, 100, 33, 0, -3, 20};
    size_t len = sizeof(values) / sizeof(*values);
    size_t i;

    fprintf(stdout, "Unsorted:\n");
    for(i = 0; i < len; i++){
	fprintf(stdout, "%d ", values[i]);
    }
    fprintf(stdout, "\n");

    sort(values, len, sizeof(*values), cmpint);

    fprintf(stdout, "Sorted:\n");
    for(i = 0; i < len; i++){
	fprintf(stdout, "%d ", values[i]);
    }
    fprintf(stdout, "\n");

    return 0;

}
