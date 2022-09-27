#include<stdio.h>
#include<mpi.h>

int main(int argc,char *argv[]){
	int rank;
	MPI_Init(NULL,NULL);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	
	if(rank % 2 == 0){
		printf("%d->Even rank\n",rank);
	}
	else{
		printf("%d->Odd rank\n",rank);
	}
	MPI_Finalize();
}
