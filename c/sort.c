
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

void sort(void* array, size_t len, size_t size, int (*compare)(const void*, const void*)){

    size_t i;
    size_t pivot;
    void* pivotp = NULL;
    void* ip = NULL;

    /* ToDo: Make in-place */
    size_t lowl = 0;
    void* low = malloc(len * size);
    if(low == NULL){
	perror("sort: malloc of 'low' failed");
	return;
    }
    size_t highl = 0;
    void* high = malloc(len * size);
    if(high == NULL){
	perror("sort: malloc of 'high' failed");
	free(low);
	return;
    }

    //sleep(1);
    //fprintf(stderr, "len = %zd\n", len);

    if(len > 1){
	//fprintf(stderr, "Recurse\n");

	/* ToDo: Choose f,m,l median pivot */
	pivot = len/2;
	pivotp = array + (pivot * size);

	/* Split Array */
	for(i = 0; i < len; i++){
	    if(i != pivot){
		ip = array + (i * size);
		if(compare(ip, pivotp) < 0){
		    memcpy((low + (lowl * size)), ip, size);
		    lowl++;
		}
		else{
		    memcpy((high + (highl * size)), ip, size);
		    highl++;
		}
	    }
	}
	
	/* Reconstitute Array */
	//fprintf(stderr, "lowl = %zd\n", lowl);
	sort(low, lowl, size, compare);
	memcpy(array, low, (lowl * size));
	memcpy((array + (lowl * size)), pivotp, size);
	//fprintf(stderr, "highl = %zd\n", highl);
	sort(high, highl, size, compare);
	memcpy(array + ((lowl + 1) * size), high, (highl * size));

	free(low);
	free(high);

	return;
    }
    else{

	//fprintf(stderr, "End\n");

	free(low);
	free(high);	

	return;
    }

}

int cmpint (const void * a, const void * b){
    const int* vala = a;
    const int* valb = b;
    //fprintf(stderr, "vala = %d\n", *vala);
    //fprintf(stderr, "valb = %d\n", *valb);
    return ( *vala - *valb );
}

int main(){

    int values[] = { 40, 10, 100, 90, 20, 25 };
    size_t len = 6;
    size_t i;

    fprintf(stdout, "sizeof(*values) = %zd\n", sizeof(*values));

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

