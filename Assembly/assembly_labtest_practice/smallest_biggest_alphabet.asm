.MODEL SMALL
.STACK 100H

.DATA
MSG DB 'Enter the string',0AH,0DH,'$'
X DB 80 DUP(?)
MIN DB 127
MAX DB 0

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
     
    MOV DI,0000H 
    ITERATE:
        CMP SI,DI
        JZ NEXT2
        CMP X[DI],'a'
        JL ELSE
        CMP X[DI],'z'
        JG ELSE
        
        MOV BH,X[DI]
        CMP MIN,BH
        JG MINCHECK
        CMP MAX,BH
        JL MAXCHECK
        
        JMP ELSE
        MINCHECK:
            MOV MIN,BH
            INC DI
            JMP ITERATE
        MAXCHECK:
            MOV MAX,BH
            INC DI
            JMP ITERATE
        ELSE:
            INC DI
            JMP ITERATE                 
                
    NEXT2:
    MOV AH,02H
    MOV DL,MIN
    INT 21H
    
    MOV DL,MAX
    INT 21H
    
    
    MOV AH,4CH
    INT 21H
MAIN ENDP
END MAIN