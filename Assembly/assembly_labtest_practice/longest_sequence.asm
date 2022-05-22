.MODEL SMALL
.STACK 100H

.DATA
MSG DB 'Enter the string',0AH,0DH,'$'
X DB 80 DUP(?)
LONG DB '0'

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
    MOV DL,'0'
    ITERATE:
        CMP SI,DI
        JZ EXIT2
        CMP X[DI],'a'
        JL ELSE
        CMP X[DI],'z'
        JG ELSE
        INC DI
        INC DL
        CMP LONG,DL
        JL MAXCHECK
        JMP ITERATE
        
        MAXCHECK:
            MOV LONG,DL
            JMP ITERATE        
        ELSE:
            MOV DL,'0'
            INC DI
            JMP ITERATE     
               
    
    EXIT2:
    MOV AH,02H
    MOV DL,LONG
    INT 21H
       
    MOV AH,4CH
    INT 21H
MAIN ENDP
END MAIN