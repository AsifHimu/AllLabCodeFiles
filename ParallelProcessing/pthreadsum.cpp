#include<bits/stdc++.h>
#include<pthread.h>
using namespace std;
#define MAX 16
#define TH 4
int ar[MAX],sum[TH],part;
void* arraysum(void* arg){
    int thread_id = part++;
    for(int i=thread_id*TH;i<(thread_id+1)*(MAX/TH);i++){
        sum[thread_id]+=ar[i];
    }
}
int main(){
    pthread_t thread[TH];
    int total=0;
    for(int i=0;i<MAX;i++){
        ar[i] = 1;
        cout<<ar[i]<<" ";
    }
    cout<<endl;
    for(int i=0;i<TH;i++){
        pthread_create(&thread[i],NULL,arraysum,(void*)NULL);
    }
    for(int i=0;i<TH;i++){
        pthread_join(thread[i],NULL);
    }
    for(int i=0;i<TH;i++){
        cout<<sum[i]<<" ";
        total+=sum[i];
    }
    cout<<endl;
    cout<<"SUM = "<<total<<endl;
    return 0;
}

