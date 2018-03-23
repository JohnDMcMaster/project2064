Writes all permutations of the LUT in "Editblk BA"

; SOP form
; A B C D  O

; 0 0 0 0  1*
; 0 0 0 1  1*
; 0 0 1 0  1*
; 0 0 1 1  1*

; 0 1 0 0  0
; 0 1 0 1  0
; 0 1 1 0  0
; 0 1 1 1  1*

; 1 0 0 0  0
; 1 0 0 1  0
; 1 0 1 0  0
; 1 0 1 1  0

; 1 1 0 0  0
; 1 1 0 1  0
; 1 1 1 0  0
; 1 1 1 1  1*

0xF101
