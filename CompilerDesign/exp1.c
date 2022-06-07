#include<stdio.h>

char str[100];

int is_digit(char ch){
    if(ch>='0' && ch<='9'){
        return 1;
    }
    return 0;
}

int is_char(char ch){
    if(ch>='a' && ch<='z' || ch>='A' && ch<='Z'){
        return 1;
    }
    return 0;
}
int is_vowel(char ch){
    if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u'||ch=='A'||ch=='E'||ch=='I'||ch=='O'||ch=='U'){
        return 1;
    }
    return 0;
}
void counting(){
    int letter_cnt=0,digit_cnt=0,others=0,word_cnt=1;
    for(int i=0;str[i];i++){
        if(str[i]==' ' && (is_char(str[i+1]) || is_digit(str[i+1]))){
            word_cnt++;
        }
        if(is_digit(str[i])){
            digit_cnt++;
        }
        if(is_char(str[i])){
            letter_cnt++;
        }
        if(!is_digit(str[i]) && !is_char(str[i])){
            others++;
        }
    }
    printf("Letter count: %d\n",letter_cnt);
    printf("Digit count: %d\n",digit_cnt);
    printf("Others count: %d\n",others);
    printf("Word count: %d\n",word_cnt);
    printf("\n");
}
void separate(){
    char letters[100],digits[100],other[100];
    int mark_letter=0,mark_digits=0,mark_other=0;
    for(int i=0;str[i];i++){
        if(is_char(str[i])){
            letters[mark_letter++]=str[i];
        }
        if(is_digit(str[i])){
            digits[mark_digits++]=str[i];
        }
        if(!is_digit(str[i]) && !is_char(str[i])){
            other[mark_other++]=str[i];
        }
    }
    letters[mark_letter]='\0';
    digits[mark_digits]='\0';
    other[mark_other]='\0';
    printf("Separated letters:%s\n",letters);
    printf("Separated digits:%s\n",digits);
    printf("Others:%s\n",other);
    printf("\n");
}
void vowel_and_consonant_count(){
    int vowel_cnt=0,consonant_cnt=0;
    for(int i=0;str[i];i++){
        if(is_vowel(str[i])){
            vowel_cnt++;
        }
        if(is_char(str[i]) && !is_vowel(str[i])){
            consonant_cnt++;
        }
    }
    printf("Vowel count: %d\n",vowel_cnt);
    printf("Consonant count: %d\n",consonant_cnt);
    printf("\n");
}
void vowel_and_consonant(){
    char vowel[100],consonant[100];
    int mark_vowel=0,mark_consonant=0;
    for(int i=0;str[i];i++){
        if(is_vowel(str[i])){
            vowel[mark_vowel++]=str[i];
        }
        if(is_char(str[i]) && !is_vowel(str[i])){
            consonant[mark_consonant++]=str[i];
        }
    }
    vowel[mark_vowel]='\0';
    consonant[mark_consonant]='\0';
    printf("Vowels :%s\n",vowel);
    printf("Consonants :%s\n",consonant);
    printf("\n");
}
void separate_word(){
    char vowel[100],consonant[100];
    int vow=0,cons=0;
    for(int i=0;str[i];i++){
        if(is_vowel(str[i])){
            while(str[i]!=' ' && str[i]!='\0'){
                vowel[vow++]=str[i++];
            }
            i--;
            vowel[vow++]=' ';
        }
        else if(is_char(str[i]) && !is_vowel(str[i])){
            while(str[i]!=' ' && str[i]!='\0'){
                consonant[cons++]=str[i++];
            }
            i--;
            consonant[cons++]=' ';
        }
    }
    vowel[vow]='\0';
    consonant[cons]='\0';
    printf("Vowel words:%s\n",vowel);
    printf("Consonant words:%s\n",consonant);
}
int main(){
    //Md. Tareq Zaman, Part-3, 2019 ami am khai
    scanf(" %[^\n]",str);
    counting();
    separate();
    vowel_and_consonant_count();
    vowel_and_consonant();
    separate_word();
    return 0;
}
