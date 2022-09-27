#include<stdio.h>
#include<mpi.h>

int main(int argc,char *argv[]){
	int rank;
	MPI_Init(NULL,NULL);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	
	int n = 12;
	int np = 4;
	int section = n / (np - 1);
	int root = 0;
	int sub[20];
	
	MPI_Status status;
	
	if(rank == root){
		int nums[20] = {1,2,3,4,5,6,7,8,9,10,11,12};
		MPI_Send(nums,section,MPI_INT,1,25,MPI_COMM_WORLD);
		MPI_Send(nums+(section*1),section,MPI_INT,2,25,MPI_COMM_WORLD);
		MPI_Send(nums+(section*2),section,MPI_INT,3,25,MPI_COMM_WORLD);
		
		int total = 0;
		for(int i=0;i<np-1;i++){
			int out;
			MPI_Recv(&out,1,MPI_INT,MPI_ANY_SOURCE,MPI_ANY_TAG,MPI_COMM_WORLD,&status);
			total+=out;
		}
		printf("Total: %d\n",total);
	}
	else{
		MPI_Recv(&sub,section,MPI_INT,MPI_ANY_SOURCE,MPI_ANY_TAG,MPI_COMM_WORLD,&status);
		int sum = 0;
		for(int i=0;i<section;i++){
			sum+=sub[i];
		}
		printf("From rank %d sum = %d\n",rank,sum);
		
		MPI_Send(&sum,1,MPI_INT,0,25,MPI_COMM_WORLD);
	}
	
	MPI_Finalize();
}
