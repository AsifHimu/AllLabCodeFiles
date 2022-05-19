.MODEL SMALL
.STACK 100H

.DATA
MSG DB 'Enter the number',0AH,0DH,'$'
MSG2 DB 0AH,0DH,'Factorial Value :$'
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
    
    MOV NUM,AL
    SUB NUM,'0'
    MOV AL,01H
    
    FACTORIAL:
    CMP NUM,00H
    JZ EXIT
    MUL NUM
    DEC NUM
    JMP FACTORIAL
    
    EXIT:
    