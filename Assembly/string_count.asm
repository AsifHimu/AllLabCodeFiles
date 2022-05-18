.MODEL SMALL
.STACK 100H

.DATA
MSG DB 'Enter the string',0AH,0DH,'$'
X DB 80 DUP(?)

NW DB 'Number Of Word :$'
NV DB 'Number Of Vowels :$'
NC DB 'Number Of Consonants :$'
ND DB 'Number Of Digits :$'

WC DB '0'
VC DB '0'
CC DB '0'
DC DB '0'

.CODE
MAIN PROC
    MOV AX,@DATA
    MOV DS,AX
    
    LEA DX,MSG
    MOV AH,09H
    INT 21H
    
    MOV SI,0000H
    MOV AH,01H
    INPUT:
        INT 21H
        CMP AL,0DH
        JZ EXIT
        MOV X[SI],AL
        INC SI
        JMP INPUT
    EXIT:
    MOV AH,02H
    MOV DL,0AH
    INT 21H
    MOV DL,0DH
    INT 21H
    
    MOV DI,0000H
    ITERATE:
        CMP DI,SI
        JZ EXIT2
        
         
    
    
    
    
    
    EXIT2:
    
    
    
    ;EXIT TO DOS
    MOV AH,4CH
    INT 21H
MAIN ENDP
END MAIN