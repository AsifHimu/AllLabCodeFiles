#include<stdio.h>
#include<string.h>

int isValidKeyword(char str[]){
    if(!strcmp(str,"if")||!strcmp(str,"else")||!strcmp(str,"while")||!strcmp(str,"continue")
    ||!strcmp(str,"break")||!strcmp(str,"do")||!strcmp(str,"return")||!strcmp(str,"int")||!strcmp(str,"float")
    ||!strcmp(str,"double")||!strcmp(str,"long")||!strcmp(str,"void")||!strcmp(str,"static")){
        return 1;
    }
    return 0;
}
int isValidIdentifier(char ch){
    if(ch>='a' && ch<='z' || ch>='A' && ch<='Z'){
        return 1;
    }
    return 0;
}
int isValidArithmeticOperator(char str[]){
    if(!strcmp(str,"+")||!strcmp(str,"-")||!strcmp(str,"*")||!strcmp(str,"/")||!strcmp(str,"^")||!strcmp(str,"=")){
        return 1;
    }
    return 0;
}
int isValidRelationalOperator(char str[]){
    if(!strcmp(str,"<")||!strcmp(str,">")||!strcmp(str,"==")||!strcmp(str,"!=")||!strcmp(str,"<=")||!strcmp(str,">=")){
        return 1;
    }
    return 0;
}
int isIntegar(char str[]){
    int len=strlen(str);
    for(int i=0;i<len;i++){
        if(str[i]>='0'&&str[i]<='9'){
            continue;
        }
        return 0;
    }
    return 1;
}
int isFloat(char str[]){
    int len=strlen(str),cnt=0;
    for(int i=0;i<len;i++){
        if(str[i]=='.'){
            cnt++;
        }
        else if(str[i]<'0' || str[i]>'9'){
            return 0;
        }
    }
    if(cnt==1)return 1;
    return 0;
}
int main(){
    char str[100];
    while(scanf("%s",str) != EOF){
        if(isValidKeyword(str)){
            puts("Keyword");
        }
        else if(isValidIdentifier(str[0])){
            puts("Identifier");
        }
        else if(isValidArithmeticOperator(str)){
            puts("Arithmetic Operator");
        }
        else if(isValidRelationalOperator(str)){
            puts("Relational Operator");
        }
        else if(isIntegar(str)){
            puts("Integar");
        }
        else if(isFloat(str)){
            puts("Float");
        }
        else{
            puts("Unknown");
        }
    }
    return 0;
}
