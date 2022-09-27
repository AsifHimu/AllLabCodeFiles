#include<stdio.h>
#include<mpi.h>

int main(int argc,char *argv[]){
	int rank;
	MPI_Init(NULL,NULL);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	int a = 20,b = 5;
	
	if(rank == 0){
		printf("Sum = %d\n",a+b);
	}
	else if(rank == 1){
		printf("Mul = %d\n",a*b);
	}
	else if(rank == 2){
		printf("Sub = %d\n",a-b);
	}
	else if(rank == 3){
		if(b > 0){
			printf("Div = %d\n",a/b);
		}
	}
	MPI_Finalize();
}
