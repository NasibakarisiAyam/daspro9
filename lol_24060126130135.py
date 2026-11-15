#   === IDENTITAS ===   #
# Nama: Athallah Nazif Arlis Pratama
# NIM : 24060126130135
# --------------------Tugas Latihan--------------------
# IsMemberS: elemen, list of list -> boolean
# {IsMemberS(x,S) mengembalikan true jika elemen x ada di dalam list of list S.
# Contoh aplikasi:
# IsMemberS(3, []) -> False
# IsMemberS(3, [2, 4, 3, [1], [4,5]]) -> True
# IsMemberS(3, [2, 4, 7, [1], [3,5]]) -> True
# }
# RemberList: elemen, List of List -> List of List
# {RemberList(x,S) menghapus semua elemen x yang ada di list of list S.
# Contoh aplikasi:
# Rember*(3, []) -> []
# Rember*(3, [4, 3, [2,4], 3]) -> [4, [2,4]]
# Rember*(3, [2, 4, [3,6,9], 5, 3]) -> [2, 4, [6,9], 5]
# MaxLOL: List of List -> elemen
# {MaxLOL(S) mengembalikan elemen maksimum di dalam list of list S.
# Contoh aplikasi:
# Max([4, 5, 6, [8,9,10], [12,0], 8]) -> 12
# Max([4, 15, 6, [8,9,10], [12,0], 8]) -> 15
# NBElmtAtom: List of List -> integer
# {NBElmtAtom(S) mengembalikan banyaknya elemen list of list S yang berupa atom.
# Contoh aplikasi:
# NBElmtAtom([4, 5, 6, [8, 9, 10], [12, 0], 8]) -> 4
# NBElmtAtom([4, 15, 6, [8, 9], 10, [12], 8]) -> 5
# NBElmtAtom([[8, 9, 10]]) -> 0}

# NBElmtList: List of List -> integer
# {NBElmtList(S) mengembalikan banyaknya elemen list of list S yang berupa list.
# Contoh aplikasi:
# NBElmtList([4, 5, 6, [8, 9, 10], [12, 0], 8]) -> 2
# NBElmtList([[4, 15], 6, [8, 9], 10, [12], 8]) -> 3
# NBElmtList([[8, 9, 10]]) -> 1

# SumLoL: List of List -> integer
# {SumLoL(S) mengembalikan jumlah semua elemen dalam list of list S.
# Contoh aplikasi:
# SumLoL([[]]) -> 0
# SumLoL([4, 5, 6, [2, 3, 1]]) -> 21
# SumLoL([[2, 3, 4]]) -> 9

# MaxNBElmtList: List of List -> integer
# {MaxNBElmtList(S) mengembalikan banyaknya elemen list maksimum yang ada pada list of list S.
# Contoh aplikasi:
# MaxNBElmtList([[4,5,6,7], [8,9,10], [12,0], 8]) -> 4
# MaxNBElmtList([[4,15], 6, [8, 9], 10, [12], 8]) -> 2
# MaxNBElmtList([8, 9, 10]) -> 0

# MaxSumElmt: List of List -> integer
# {MaxSumElmt(S) mengembalikan elemen maksimum pada list of list S;
# Jika elemen berupa list, maka dihitung sum dari elemen dalam list tersebut;
# Jika elemen berupa atom, maka nilainya adalah elemen tersebut.
# Contoh aplikasi:
# MaxSumElmt([1, 2], 9, [4, 5, 6], 8]) -> 15
# MaxSumElmt([1, 2], 90, [4, 5, 6], 8]) -> 90
# MaxSumElmt([8, 9, 10]) -> 10
# MaxSumElmt([[8, 9, 10]]) -> 27

#   === REALISASI ===   #
from list import *


def isEmptyList(s)->bool:
    return s == []

def isAtom(s)->bool:
    return type(s) != list

def isList(s)->bool:
    return type(s) == list


def konslo(e:list, s:list)->list:
    return [e] + s

def konsli(s:list, l:list)->list:
    return s + [l]


def firstList(s:list)->list:
    return s[0]

def lastList(s:list)->list:
    return s[-1]

def tailList(s:list)->list:
    return s[1:]

def headList(s:list)->list:
    return s[:-1]


def IsmemberList(x,s:list[list])->bool:
    if isEmptyList(s): return False
    elif isAtom(firstList(s)):
        if firstList(s) == x: return True
        else:
            return IsmemberList(x, tailList(s))

    else: return IsmemberList(x, firstList(s)) or IsmemberList(x, tailList(s))

def RemberList(x,s:list[list])->list[list]:
    if isEmptyList(s): 
        return []
    elif isAtom(firstList(s)):
        if firstList(s) == x: 
            return RemberList(x,tailList(s))
        else:
            return Konso(firstList(s), RemberList(x, tailList(s)))
    else: return konslo(RemberList(x, firstList(s)), RemberList(x, tailList(s)))

def max2(a,b):
    if a > b:
        return a
    else:
        return b

def MaxLOL(S):
    if isEmptyList(S):
        return float('-inf')
    elif isAtom(firstList(S)):
        return max2(firstList(S), MaxLOL(tailList(S)))
    else:
        return max2(MaxLOL(firstList(S)), MaxLOL(tailList(S)))

def NBElmntAtom(s:list[list])->int:
    if isEmptyList(s):
        return 0
    elif isAtom(firstList(s)):
        return 1 + NBElmntAtom(tailList(s))
    else:
        return NBElmntAtom(tailList(s))

def NBElmntList(s:list[list])->int:
    if isEmptyList(s):
        return 0
    elif isList(firstList(s)):
        return 1 + NBElmntList(tailList(s))
    else:
        return NBElmntList(tailList(s))
    
def sumLOL(s:list[list])->int:
    if isEmptyList(s):
        return 0
    elif isAtom(firstList(s)):
        return firstList(s) + sumLOL(tailList(s))
    else:
        return sumLOL(firstList(s)) + sumLOL(tailList(s))

def NBElmnt(s:list[list])->int:
    if isEmptyList(s):
        return 0
    else: 
        return 1 + NBElmnt(tailList(s))

def MaxNBElmntList(s:list[list])->int:
    if isEmptyList(s):
        return 0
    elif isAtom(firstList(s)):
        return MaxNBElmntList(tailList(s))
    else:
        return max2(NBElmnt(firstList(s)), MaxNBElmntList(tailList(s)))

def MaxSumElmnt(s:list[list])->list:
    if isEmptyList(s):
        return 0
    elif isAtom(firstList(s)):
        return max2(firstList(s), MaxSumElmnt(tailList(s)))
    else:
        return max2(sumLOL(firstList(s)), MaxSumElmnt(tailList(s)))


#   === APLIKASI ===   #
print(RemberList(3, [4, 3, [2, 4], 3]))  
print(MaxLOL([[1, 2], [3, 4], [5, 6]]))
print(NBElmntAtom([4, 5, 6, [8, 9, 10], [12, 0], 8]))
print(NBElmntList([[4, 15], 6, [8, 9], 10, [12], 8]))
print(sumLOL([[2, 3, 4]]))
print(MaxNBElmntList([[4,5,6,7], [8,9,10], [12,0], 8]))
print(MaxSumElmnt([[1, 2], 90, [4, 5, 6], 8]))
