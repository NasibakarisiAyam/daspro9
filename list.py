## Nama: Athallah Nazif Arlis Pratama
## NIM : 24060126130135
## Tanggal : 24/10/2026

##==== DEFINISI DAN SPESIFIKASI TYPE ====##
# Konstruktor menambahkan elemen di awal, notasi prefix
# type List: [] atau [e o List]
# Konstruktor menambahkan elemen di akhir, notasi postfix
# type List: [] atau [List o e]

##==== DEFINISI DAN SPESIFIKASI KONSTRUKTOR LIST ====##
# Konso: elemen, List -> List
# {Konso(e, L) menghasilkan sebuah list dari e dan L
# dengan e sebagai elemen pertama dari L.}
#{Elemen tipe datanya bebas. Sesuaikan dengan jenis listnya}
# Konso: elemen, List -> List
# {Konso(e, L) menghasilkan sebuah list dari e dan L
# dengan e sebagai elemen pertama dari L.}
#{Elemen tipe datanya bebas. Sesuaikan dengan jenis listnya}

##==== DEFINISI DAN SPESIFIKASI SELEKTOR LIST ====##
# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstElmt(L): List tidak kosong -> elemen
# {FirstElmt(L) mengembalikan elemen pertama dari L.}
#{Elemen tipe datanya bebas. Sesuaikan dengan jenis listnya}
# LastElmt(L): List tidak kosong -> elemen
# {LastElmt(L) mengembalikan elemen terakhir dari L.}
#{Elemen tipe datanya bebas. Sesuaikan dengan jenis listnya}
# LastElmt(L): List tidak kosong -> elemen
# {LastElmt(L) mengembalikan elemen terakhir dari L.}
#{Elemen tipe datanya bebas. Sesuaikan dengan jenis listnya}
# LastElmt(L): List tidak kosong -> elemen
# {LastElmt(L) mengembalikan elemen terakhir dari L.}
#{Elemen tipe datanya bebas. Sesuaikan dengan jenis listnya}

##==== DEFINISI DAN SPESIFIKASI PREDIKAT LIST ====##
# LastElmt(L): List tidak kosong -> elemen
# {LastElmt(L) mengembalikan elemen terakhir dari L.}
#{Elemen tipe datanya bebas. Sesuaikan dengan jenis listnya}
# LastElmt(L): List tidak kosong -> elemen
# {LastElmt(L) mengembalikan elemen terakhir dari L.}
#{Elemen tipe datanya bebas. Sesuaikan dengan jenis listnya}

##==== DEFINISI DAN SPESIFIKASI FUNGSI OPERASI LIST ====##
# NbElmt(L): List -> integer
# {NbElmt(L) menghasilkan banyaknya elemen dalam list L.}

##==== DEFINISI DAN SPESIFIKASI ====##
# ElmtKeN: integer ≥ 0, List -> elemen
# {ElmtKeN(N, L) menghasilkan elemen ke-N dari list L.}
# IsMember: elemen, List -> boolean
# {IsMember(X, L) bernilai True apabila X merupakan elemen dari List.}
# Copy: List -> List
# {Copy(L) menghasilkan List yang identik dengan list asal.}
# Inverse: List -> List
# {Inverse(L) menghasilkan list L yang dibalik, yaitu
# yang urutan elemennya adalah kebalikan dari list awal.}
# Konkat: 2 List -> List
# {Konkat(L1, L2) menghasilkan List yang merupakan hasil konkatenasi # list L1 dan L2.}
# SumElmt(L): List of integer -> integer
# {SumElmt(L) menghasilkan bilangan bulat yang merupakan jumlah # nilai dari seluruh elemen L.}
# AvgElmt(L): List of integer -> real
# {AvgElmt(L) menghasilkan bilangan riil yang merupakan rata-rata # nilai dari seluruh elemen L.}
# MaxElmt(L): List of integer -> integer
# {MaxElmt(L) mengembalikan elemen dengan nilai maksimum dari list L.}
# MaxNB: List of integer -> = 1> # {MaxNB(L) menghasilkan tipe bentukan yang berisikan bilangan maksimum 
# pada list L dan seberapa banyak bilangan itu muncul di dalam list.}
# AddList: 2 List of integer -> List
# {AddList(L1, L2) menghasilkan list baru yang setiap elemennya adalah # hasil penjumlahan setiap elemen di L1 dan L2 pada posisi yang sama.}
# IsPalindrom: List of character -> boolean
# {IsPalindrom(L) bernilai True jika L merupakan kata palindrom, 
# # yakni kata yang sama jika dibaca dari kiri atau kanan.}
# IsEqual: 2 List -> boolean
# {IsEqual(L1,L2) true jika dan hanya jika kedua list sama, yaitu setiap elemen dan urutan kemunculannya sama}
# MinElmt: List of integer (tidak kosong) -> integer
# {MinElmt(L) mengembalikan elemen dengan nilai minimum dari list L.}
# CountN: character, list of character -> integer

# {CountN(C, T) menghasilkan banyaknya kemunculan karakter C pada list of character (T)}
# Atleast: integer > 0, character, list of character -> boolean
# {Atleast (N,C,T) benar, jika karakter C minimal muncul N kali pada list of character (T)}
# IsXElmtKeN (N,L) :elemen, integer ≥ 0, List (tidak kosong) → boolean
# {IsXElmtKeN (L) true jika X adalah elemen ke-N list L, N ≥ 0, dan N ≤ banyaknya elemen list, false jika tidak}
# DelFirstElmt: List of integer (tidak kosong) → List of integer DelFirstElmt(Li) mengembalikan list L tanpa elemen pertamanya. kondisi: List L tidak kosong.}
# MultiRember: elemen, List -> List
# {MultiRember(X, L) menghapus seluruh kemunculan elemen X dari list L.}
#CountGenap: List of Integer -> integer
# {CountGenap(L) menghasilkan banyaknya elemen bernilai genap dalam list L.}
# IndexOf: integer, list of integer -> integer
# {IndexOf(X, Li) menghasilkan indeks (dimulai dari 0) kemunculan pertama X di list L. Jika Xx tidak ada di L, hasilnya -1.}




def IsEmpty(L):
    return len(L) == 0
 
def IsOneElmt(L):
    return len(L) == 1
 
def FirstElmt(L):
    return L[0]
 
def LastElmt(L):
    return L[-1]
 
def Tail(L):
    return L[1:]
 
def Head(L):
    return L[:-1]
 
def Konso(e, L):
    return [e] + L
 
def Konsi(L, e):
    return L + [e]
 
def NbElmt(L):
    if IsEmpty(L):
        return 0
    return 1 + NbElmt(Tail(L))

def ElmtKeN(N, L):
    if N == 0:
        return FirstElmt(L)
    return ElmtKeN(N - 1, Tail(L))
 
 

def IsMember(X, L):
    if IsEmpty(L):
        return False
    if FirstElmt(L) == X:
        return True
    return IsMember(X, Tail(L))
 
 

def Copy(L):
    if IsEmpty(L):
        return []
    return Konso(FirstElmt(L), Copy(Tail(L)))
 
 

def Inverse(L):
    if IsEmpty(L):
        return []
    return Konsi(Inverse(Tail(L)), FirstElmt(L))
 
 

def Konkat(L1, L2):
    if IsEmpty(L1):
        return L2
    return Konso(FirstElmt(L1), Konkat(Tail(L1), L2))
 
 

def SumElmt(L):
    if IsEmpty(L):
        return 0
    return FirstElmt(L) + SumElmt(Tail(L))
 
 

def AvgElmt(L):
    return SumElmt(L) / NbElmt(L)
 
 

def MaxElmt(L):
    if IsOneElmt(L):
        return FirstElmt(L)
    sisa = MaxElmt(Tail(L))
    return FirstElmt(L) if FirstElmt(L) > sisa else sisa
 
 

def MaxNB(L):
    if IsOneElmt(L):
        return (FirstElmt(L), 1)
    r = MaxNB(Tail(L))
    if FirstElmt(L) > r[0]:
        return (FirstElmt(L), 1)
    if FirstElmt(L) == r[0]:
        return (r[0], r[1] + 1)
    return r
 
 

def AddList(L1, L2):
    if IsEmpty(L1):
        return []
    return Konso(FirstElmt(L1) + FirstElmt(L2), AddList(Tail(L1), Tail(L2)))
 
 

def IsPalindrom(L):
    if IsEmpty(L) or IsOneElmt(L):
        return True
    return FirstElmt(L) == LastElmt(L) and IsPalindrom(Tail(Head(L)))
 
 

def IsEqual(L1, L2):
    if IsEmpty(L1) and IsEmpty(L2):
        return True
    if IsEmpty(L1) or IsEmpty(L2):
        return False
    return FirstElmt(L1) == FirstElmt(L2) and IsEqual(Tail(L1), Tail(L2))
 
 

def MinElmt(L):
    if IsOneElmt(L):
        return FirstElmt(L)
    sisa = MinElmt(Tail(L))
    return FirstElmt(L) if FirstElmt(L) < sisa else sisa
 
 

def CountN(C, T):
    if IsEmpty(T):
        return 0
    if FirstElmt(T) == C:
        return 1 + CountN(C, Tail(T))
    return CountN(C, Tail(T))
 
 

def Atleast(N, C, T):
    if N <= 0:
        return True
    if IsEmpty(T):
        return False
    if FirstElmt(T) == C:
        return Atleast(N - 1, C, Tail(T))
    return Atleast(N, C, Tail(T))
 
 

def IsXElmtKeN(X, N, L):
    if N == 0:
        return FirstElmt(L) == X
    if IsOneElmt(L):          
        return False
    return IsXElmtKeN(X, N - 1, Tail(L))
 
 

def DelFirstElmt(L):
    return Tail(L)
 
 
def MultiRember(X, L):
    if IsEmpty(L):
        return []
    if FirstElmt(L) == X:
        return MultiRember(X, Tail(L))
    return Konso(FirstElmt(L), MultiRember(X, Tail(L)))
 
 

def CountGenap(L):
    if IsEmpty(L):
        return 0
    if FirstElmt(L) % 2 == 0:
        return 1 + CountGenap(Tail(L))
    return CountGenap(Tail(L))
 
 

def IndexOf(X, L):
    if IsEmpty(L):
        return -1
    if FirstElmt(L) == X:
        return 0
    r = IndexOf(X, Tail(L))
    return -1 if r == -1 else 1 + r


##==== APLIKASI ====##
##