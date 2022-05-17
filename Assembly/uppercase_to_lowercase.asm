.MODEL SMALL
.STACK 100H

.DATA
MSG DB 'Enter the string',0AH,0DH,'$'
X DB 80 DUP(?)

.CODE
MAIN PROC
    MOV AX,@DATA
    MOV DS,AX
    
    LEA DX,MSG
    MOV AH,09H
    INT 21H
    
    MOV SI,0000H
    MOV AH,01H
    NEXT:
    INT 21H
    CMP AL,0DH
    JZ EXIT
    MOV X[SI],AL
    INC SI
    JMP NEXT
    EXIT:
    
    MOV AH,02H
    MOV DL,0AH
    INT 21H
    MOV DL,0DH
    INT 21H
    
    MOV DI,SI
    MOV SI,0000H
    NEXT2:
    CMP SI,DI
    JZ EXIT2
    
    MOV DL,X[SI]
    CMP DL,65
    JL ELSE
    CMP DL,90
    JG ELSE
    OR DL,20H
    INT 21H
    INC SI
    JMP NEXT2
    ELSE:
    MOV DL,X[SI]
    INT 21H
    INC SI
    JMP NEXT2    
    EXIT2:
    
    MOV AH,4CH
    INT 21H
MAIN ENDP
END MAIN
