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
        CMP X[DI],'a'
        JL ELSE
        CMP X[DI],'z'
        JG ELSE
        
        MOV DH,X[DI] 
        
        CMP MIN,DH
        JG MIN_ASCII
        
        CMP MAX,DH
        JL MAX_ASCII
        
        JMP ELSE        
        
        MIN_ASCII:
            MOV MIN,DH
            INC DI
            JMP ITERATE
        MAX_ASCII:
            MOV MAX,DH
            INC DI
            JMP ITERATE        
        ELSE:
            INC DI
            JMP ITERATE
                    
    EXIT2:
        MOV DL,MIN
        INT 21H
        
        MOV DL,MAX
        INT 21H
                    
    ;EXIT TO DOS
    MOV AH,4CH
    INT 21H
    
MAIN ENDP
END MAIN
    