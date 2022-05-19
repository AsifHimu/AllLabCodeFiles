.MODEL SMALL
.STACK 100H

.DATA
MSG DB 'Enter the string',0AH,0DH,'$'
X DB 80 DUP(?)

NW DB 'Number Of Word : $'
NV DB 'Number Of Vowels : $'
NC DB 'Number Of Consonants : $'
ND DB 'Number Of Digits : $'

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
        CMP X[DI],'z'
        JG NOTLETTER
        CMP X[DI],'A'
        JL NOTLETTER
        
        ;COMMENT @
        CMP X[DI],'Z'
        JG TOPP
        JMP ENDTOPP
        TOPP:
            CMP X[DI],'a'
            JL NOTLETTER
            ;CMP X[DI],'z'
            ;JLE ENDTOPP
        ENDTOPP:
        ;@   
        CMP X[DI],'A'
        JZ VOWEL
        CMP X[DI],'E'
        JZ VOWEL
        CMP X[DI],'I'
        JZ VOWEL
        CMP X[DI],'O'
        JZ VOWEL
        CMP X[DI],'U'
        JZ VOWEL     
        CMP X[DI],'a'
        JZ VOWEL
        CMP X[DI],'e'
        JZ VOWEL
        CMP X[DI],'i'
        JZ VOWEL
        CMP X[DI],'o'
        JZ VOWEL
        CMP X[DI],'u'
        JZ VOWEL
        
        INC CC
        INC DI
        JMP ITERATE   
        VOWEL:
            INC VC
            INC DI
            JMP ITERATE        
        NOTLETTER:
            CMP X[DI],' '
            JZ SPACE
            
            CMP X[DI],'0'
            JL NOTDIGIT
            CMP X[DI],'9'
            JG NOTDIGIT
            INC DC
            INC DI
            JMP ITERATE
            SPACE:
                INC WC
                INC DI
                JMP ITERATE            
            NOTDIGIT:
                JMP ITERATE
            
    EXIT2:
    ADD WC,1
    
    LEA DX,NW
    MOV AH,09H
    INT 21H
    
    MOV AH,02H
    MOV DL,WC
    INT 21H
    
    MOV AH,02H
    MOV DL,0AH
    INT 21H
    MOV DL,0DH
    INT 21H
    
    LEA DX,NV
    MOV AH,09H
    INT 21H
    
    MOV AH,02H
    MOV DL,VC
    INT 21H
    
    MOV AH,02H
    MOV DL,0AH
    INT 21H
    MOV DL,0DH
    INT 21H
    
    LEA DX,NC
    MOV AH,09H
    INT 21H
    
    MOV AH,02H
    MOV DL,CC
    INT 21H
    
    MOV AH,02H
    MOV DL,0AH
    INT 21H
    MOV DL,0DH
    INT 21H
    
    LEA DX,ND
    MOV AH,09H
    INT 21H
    
    MOV AH,02H
    MOV DL,DC
    INT 21H       
    
    ;EXIT TO DOS
    MOV AH,4CH
    INT 21H
MAIN ENDP
END MAIN