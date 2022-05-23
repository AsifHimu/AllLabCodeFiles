.MODEL SMALL
.STACK 100H

.DATA
MSG DB 'Enter the values(NUM2>NUM1)',0AH,0DH,'$'
ADDITION DB 0AH,0DH,'Addition :$'
SUBTRACTION DB 0AH,0DH,'Suntraction :$'
MULTIPLICATION DB 0AH,0DH,'Multiplication :$'
DIVISION DB 0AH,0DH,'Division :$'
NUM1 DB ?
NUM2 DB ?

REM DB 0AH,0DH,'Remainder :$'
QUO DB 0AH,0DH,'Quotient :$'

.CODE
MAIN PROC
    MOV AX,@DATA
    MOV DS,AX
    
    LEA DX,MSG
    MOV AH,09H
    INT 21H
    
    MOV AH,01H
    INT 21H
    
    MOV NUM1,AL
    SUB NUM1,'0'
    
    MOV AH,01H
    INT 21H
    
    MOV NUM2,AL
    SUB NUM2,'0'
    
    MOV BH,NUM2
    MOV BL,NUM1
    
    ADDI:
    LEA DX,ADDITION
    MOV AH,09H
    INT 21H
    
    ADD BH,BL
    
    MOV AH,02H
    MOV DL,BH
    ADD DL,'0'
    INT 21H
    
    SUBT:
    LEA DX,SUBTRACTION
    MOV AH,09H
    INT 21H
    
    MOV BH,NUM2    
    SUB BH,BL
    
    MOV AH,02H
    MOV DL,BH
    ADD DL,'0'
    INT 21H
    
    MULT:
    LEA DX,MULTIPLICATION
    MOV AH,09H
    INT 21H
    
    MOV BH,NUM2
    MOV BL,NUM1
    
    MOV AL,BL    
    MUL BH    
    
    MOV AH,02H
    MOV DX,AX
    ADD DX,'0'
    INT 21H
    
    DIVI:
    LEA DX,DIVISION
    MOV AH,09H
    INT 21H
    
    MOV BH,NUM2
    MOV BL,NUM1
    MOV AH,0000H
    MOV AL,BH
    
    DIV BL
    
    MOV CH,AH
    MOV CL,AL
    
    LEA DX,QUO
    MOV AH,09H
    INT 21H
    
    MOV AH,02H
    MOV DL,CL
    ADD DL,'0'
    INT 21H
    
    LEA DX,REM
    MOV AH,09H
    INT 21H
    
    MOV AH,02H
    MOV DL,CH
    ADD DL,'0'
    INT 21H        
    
    MOV AH,4CH
    INT 21H
    
MAIN ENDP
END MAIN
    
    
    
     
    
    

