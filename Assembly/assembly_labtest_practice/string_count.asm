.MODEL SMALL
.STACK 100H

.DATA
MSG DB 'Enter the string',0AH,0DH,'$'

NW DB 0AH,0DH,'Number of words :$'
ND DB 0AH,0DH,'Number of digits :$'
NV DB 0AH,0DH,'Number of vowels :$'
NC DB 0AH,0DH,'Number of consonants :$'

X DB 80 DUP(?)
WC DB '0'
DC DB '0'
VC DB '0'
CC DB '0'

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
        JZ EXIT2
        CMP X[DI],'A'
        JL NOTALETTER
        CMP X[DI],'z'
        JG NOTALETTER
        CMP X[DI],'Z'
        JG CHECK
        JMP ENDCHECK
        CHECK:
            CMP X[DI],'a'
            JL NOTALETTER
        ENDCHECK:
        
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
        NOTALETTER:
            CMP X[DI],' '
            JZ WORD
            CMP X[DI],'0'
            JL NOTADIGIT
            CMP X[DI],'9'
            JG NOTADIGIT           
            INC DC
            INC DI
            JMP ITERATE
            
            WORD:
            INC WC
            INC DI
            JMP ITERATE
            NOTADIGIT:
            INC DI
            JMP ITERATE            
        
    EXIT2:
    ADD WC,1
    
    LEA DX,NW
    MOV AH,09H
    INT 21H
    
    MOV AH,02H
    MOV DL,WC
    INT 21H
    
    LEA DX,ND
    MOV AH,09H
    INT 21H
    
    MOV AH,02H
    MOV DL,DC
    INT 21H
    
    LEA DX,NV
    MOV AH,09H
    INT 21H
    
    MOV AH,02H
    MOV DL,VC
    INT 21H
    
    LEA DX,NC
    MOV AH,09H
    INT 21H
    
    MOV AH,02H
    MOV DL,CC
    INT 21H
    
    MOV AH,4CH
    INT 21H
MAIN ENDP
END MAIN