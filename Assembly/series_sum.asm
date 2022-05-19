.MODEL SMALL
.STACK 100H

.DATA
NUM DB ?
MSG DB 'Enter the number',0AH,0DH,'$'
MSG2 DB 0AH,0DH,'Series sum value: $'

.CODE
MAIN PROC
    MOV AX,@DATA
    MOV DS,AX
    
    LEA DX,MSG
    MOV AH,09H
    INT 21H
    
    INPUT:
    MOV AH,01H
    INT 21H
    
    MOV NUM,AL
    SUB NUM,'0'
    MOV BL,00H
    MOV CL,10
    
    SUM:
    CMP NUM,-1H
    JZ DISPLAY
    ADD BL,NUM
    DEC NUM
    JMP SUM
        
    DISPLAY:
    LEA DX,MSG2
    MOV AH,09H
    INT 21H
    
    MOV AH,00H
    MOV AL,BL
    DIV CL
    
    MOV NUM,AH
    
    MOV AH,02H
    MOV DL,AL
    ADD DL,'0'
    INT 21H
    
    MOV AH,02H
    MOV DL,NUM
    ADD DL,'0'
    INT 21H
    
    MOV AH,4CH
    INT 21H
MAIN ENDP
END MAIN
    
    
    
