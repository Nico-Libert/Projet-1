# coding: utf-8

# imports

import os, sys
os.system('')

# variables


def Map():


    sable ="\x1b[43m░░\x1b[0m"
    plaine = "\x1b[42m  \x1b[0m"
    jungle = "\x1b[42mϡ \x1b[0m"
    rocher =  "\x1b[40m▒▒\x1b[0m"
    eau = "\x1b[46m  \x1b[0m"
    mer = "\x1b[44m ~\x1b[0m"
    quete = "\x1b[31mЖЖ\x1b[0m"
    player = "\033[45m☺\x1b[0m"
    

    s = sable
    p= plaine
    j= jungle
    r = rocher
    e = eau
    m = mer
    q = quete
    l = player




    L1 = [r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r]
    L2 = [r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r]
    L3 = [r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,p,e,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r,r]
    L4 = [r,r,r,r,r,r,p,p,r,r,r,r,p,r,p,e,e,q,r,r,r,r,r,r,p,p,r,r,r,r,r,r,j,r,r,r,r,j,r,r,r,r,r,r,r,r,r,r,r,r]
    L5 = [r,r,r,r,r,r,p,p,r,p,r,p,p,p,p,e,e,p,p,p,r,p,r,r,p,p,r,p,p,r,p,r,j,j,r,j,j,j,j,j,r,r,r,r,r,r,r,r,r,r]
    L6 = [r,r,r,r,p,p,p,p,p,p,p,p,p,p,e,e,e,p,p,p,p,p,p,p,p,p,p,p,p,r,p,p,j,j,j,j,j,j,j,j,j,j,r,j,r,r,r,r,r,r]
    L7 = [r,r,r,r,r,r,r,p,p,p,p,p,p,p,p,e,e,e,p,p,p,p,p,p,p,p,p,p,p,p,p,p,j,j,j,j,j,j,j,j,j,j,j,j,r,r,r,r,r,r]
    L8 = [r,r,r,r,r,p,p,p,p,p,p,p,p,p,p,e,e,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,j,j,j,j,j,j,j,j,r,r,r,r,r,r]
    L9 = [r,r,r,r,r,r,p,p,p,p,p,p,p,p,p,e,e,e,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,j,j,j,j,j,j,j,q,r,r,r,r,r]
    L10 = [r,r,r,r,r,r,p,p,p,p,p,p,p,p,p,p,e,e,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,j,j,j,j,j,j,r,r,r,r,r,r]
    L11 = [r,r,r,r,r,r,p,p,p,p,p,p,p,p,p,p,e,e,e,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,j,j,j,j,j,r,r,r,r,r]
    L12 = [r,r,r,r,r,r,p,p,p,p,p,p,p,p,p,p,p,e,e,e,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,j,j,j,j,r,r,r,r,r]
    L13 = [r,r,r,r,r,p,p,p,p,p,p,p,p,p,p,p,p,e,e,e,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,j,j,r,r,r,r,r,r]
    L14 = [r,r,r,r,r,p,p,p,p,p,p,p,p,p,p,p,p,p,e,e,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,r,r,r,r,r]
    L15 = [r,r,r,r,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,j,j,j,j,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,r,r,r,r]
    L16 = [r,r,r,r,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,j,j,j,j,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,r,r,r,m]
    L17 = [m,r,r,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,j,j,j,j,j,p,p,p,p,p,p,p,p,p,p,p,s,s,s,s,s,s,p,p,r,r,r,m,m]
    L18 = [m,r,r,r,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,j,j,j,j,j,j,p,p,p,p,p,p,p,p,p,s,s,s,s,s,s,s,s,s,s,r,m,m,m]
    L19 = [m,r,r,r,r,j,j,j,j,j,q,j,j,j,j,j,j,e,e,e,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p,p,s,s,s,s,s,s,s,s,s,s,m,m,m,m]
    L20 = [m,m,r,r,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,j,j,j,j,j,j,j,j,j,j,j,p,p,p,p,p,s,s,s,s,s,s,s,s,s,m,m,m,m,m]
    L21 = [m,m,r,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,j,j,j,j,j,j,j,j,j,j,j,p,p,p,r,s,s,s,s,s,s,s,s,m,m,m,m,m,m]
    L22 = [m,m,r,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,j,j,j,j,j,j,j,j,j,j,j,j,p,r,r,s,s,s,s,s,s,s,m,m,m,m,m,m,m]
    L23 = [m,m,r,j,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,r,r,r,s,s,s,s,s,l,m,m,m,m,m,m,m,m]
    L24 = [m,m,r,j,j,j,j,j,j,j,j,j,j,j,j,j,j,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,r,r,r,r,s,s,s,s,s,m,m,m,m,m,m,m,m,m]
    L25 = [m,r,j,j,r,r,j,j,r,r,j,j,j,r,r,j,e,e,e,j,j,j,j,j,j,j,j,j,j,j,j,r,r,r,r,r,s,s,s,s,m,m,m,m,m,m,m,m,m,m]
    L26 = [m,m,r,r,r,r,r,j,r,r,r,j,r,r,r,r,e,e,e,j,j,j,j,r,j,j,j,j,j,q,j,r,r,r,r,r,r,s,s,m,m,m,m,m,m,m,m,m,m,m]
    L27 = [m,m,r,m,m,r,r,r,r,r,r,r,m,r,r,r,e,e,r,r,r,r,r,m,r,j,r,j,r,r,r,r,r,r,r,r,r,s,m,m,m,m,m,m,m,m,m,m,m,m]
    L28 = [m,m,m,m,m,m,r,m,m,m,r,m,m,m,r,m,m,m,m,r,r,m,m,m,m,r,m,r,m,m,m,m,m,m,m,m,r,m,m,m,m,m,m,m,m,m,m,m,m,m]
    L29 = [m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m]
    L30 = [m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m,m]

    carte = [L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L14,L15,L16,L17,L18,L19,L20,L21,L22,L23,L24,L25,L26,L27,L28,L29,L30]

    for valeur in carte :
        for i in valeur :
            print(i, end="")
        print(i)

# code starts here
if __name__ == "__main__":
    Map()
        