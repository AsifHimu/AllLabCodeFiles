.MODEL SMALL
.STACK 100H

.DATA
MSG DB 'Enter the string',0AH,0DH,'$'
X DB 80 DUP (?)

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
        JZ NEXT
        MOV X[SI],AL
        INC SI
        JMP INPUT
    NEXT:    
    MOV AH,02H
    MOV DL,0AH
    INT 21H
    MOV DL,0DH
    INT 21H
    
    DEC SI
    ITERATE:
        CMP SI,-1H
        JZ NEXT2
        MOV DL,X[SI]
        DEC SI
        INT 21H    
        JMP ITERATE
    NEXT2:    
    MOV AH,4CH
    INT 21H
MAIN ENDP
END MAIN