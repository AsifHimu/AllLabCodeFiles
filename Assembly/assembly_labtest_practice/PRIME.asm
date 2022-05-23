.MODEL SMALL
.STACK 100H

.DATA
MSG DB 'Enter the number',0AH,0DH,'$'
PRIME DB 0AH,0DH,'PRIME NUMBER$'
NOTPRIME DB 0AH,0DH,'NOT PRIME NUMBER$'
NUM DB ?

.CODE
MAIN PROC
    MOV AX,@DATA
    MOV DS,AX
    
    LEA DX,MSG
    MOV AH,09H
    INT 21H
    
    MOV AH,01H
    INT 21H
    
    CMP AL,'0'
    JZ IS_NOT_PRIME
    CMP AL,'1'
    JZ IS_NOT_PRIME
    
    SUB AL,'0'
    MOV NUM,AL
    
    MOV CL,2
    
    ITERATE:
        CMP CL,NUM
        JGE IS_PRIME
        MOV AH,00H
        DIV CL
        CMP AH,00H
        JE IS_NOT_PRIME
        MOV AL,NUM
        INC CL
        JMP ITERATE
        
    IS_PRIME:
        LEA DX,PRIME
        MOV AH,09H
        INT 21H
        JMP EXIT
    IS_NOT_PRIME:
        LEA DX,NOTPRIME
        MOV AH,09H
        INT 21H
        JMP EXIT
    EXIT:
    MOV AH,4CH
    INT 21H
MAIN ENDP
END MAIN
    
    
    
    