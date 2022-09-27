#include<stdio.h>
#include<mpi.h>

int main(int argc,char *argv[]){
	int rank;
	int np;
	MPI_Init(NULL,NULL);
	
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&np);
	
	printf("Hello I am process %d out of %d processes\n",rank,np);
	
	MPI_Finalize();
}
