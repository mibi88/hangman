from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from random import *
from re import *

#=== A hangman game by mibi88===

main = Tk()
main.title("Hangman game")
chooseframe = LabelFrame(main, text="Start a new game")
chooseframe.pack(fill="both")
#=================variables=================
dicoadress = StringVar("")
word = StringVar("")
resultword = StringVar("")
wordlen = IntVar()
nbtry = IntVar()
letterspressed = StringVar("")
#=========================================

#=========================================
#================Main game================
#=========================================

#================commands================
def run():
   gameover.pack_forget()
   nbtry.set(10)
   letterspressed.set("")
   filename = dicoadress.get()
   print(filename)
   dictionnary = open(filename, mode="r", encoding="utf8")
   fulldico = dictionnary.readlines()
   print(fulldico)
   dictionnarylist = fulldico
   """
   if "\n" in fulldico:
      compile(r"[\n\r\t]")
   #
   #
   linenumber = len(fulldico)
   dictionnarylist = []
   scrolledlines = 0
   line = dictionnary.readline()
   while scrolledlines != linenumber:
      dictionnarylist.append(line)
      line = dictionnary.readline()
      scrolledlines += 1
   selword = choice(dictionnarylist)
   word.set(selword)
   print(word.get())
   """
   selword = choice(dictionnarylist)
   while selword == "\n":
      selword = choice(dictionnarylist)
   if "\n" in selword:
      selword = selword.replace("\n", "", 1)
   selword = selword.upper()
   len_selword = len(selword)
   word.set(selword)
   wordlen.set(len_selword)
   scroll = 0
   resvar = ""
   while scroll != len_selword:
      resvar += "*"
      scroll += 1
   resultword.set(resvar)
   #print(word.get())
   print(wordlen.get())
   print(nbtry.get())
   chooseframe.pack_forget()
   mainframe.pack()
def tryletter(letter):
   usedletters = letterspressed.get()
   if not letter in usedletters:
      #try the letter
      org_res = resultword.get()
      wordvar = word.get()
      letters_full = wordlen.get()
      nbtryvar = nbtry.get()
      scrolled_letters = 0
      result = ""
      letterfound = 0
      while letters_full != scrolled_letters:
         endnb = scrolled_letters + 1
         lettertotest = wordvar[scrolled_letters:endnb]
         if lettertotest == letter:
            result += letter
            letterfound = 1
         else:
            in_word = org_res[scrolled_letters:endnb]
            if in_word == "*":
               result += "*"
            else:
               result += in_word
         scrolled_letters += 1
      if letterfound == 0:
         nbtryvar = nbtryvar - 1
      resultword.set(result)
      nbtry.set(nbtryvar)
      if nbtryvar == 0:
         game_over()
      if wordvar == result:
         win()
      usedletters += letter
      letterspressed.set(usedletters)
   else:
         showinfo("Info ...", "Already tested letter.")
def acom():
   tryletter("A")
def bcom():
   tryletter("B")
def ccom():
   tryletter("C")
def dcom():
   tryletter("D")
def ecom():
   tryletter("E")
def fcom():
   tryletter("F")
def gcom():
   tryletter("G")
def hcom():
   tryletter("H")
def icom():
   tryletter("I")
def jcom():
   tryletter("J")
def kcom():
   tryletter("K")
def lcom():
   tryletter("L")
def mcom():
   tryletter("M")
def ncom():
   tryletter("N")
def ocom():
   tryletter("O")
def pcom():
   tryletter("P")
def qcom():
   tryletter("Q")
def rcom():
   tryletter("R")
def scom():
   tryletter("S")
def tcom():
   tryletter("T")
def ucom():
   tryletter("U")
def vcom():
   tryletter("V")
def wcom():
   tryletter("W")
def xcom():
   tryletter("X")
def ycom():
   tryletter("Y")
def zcom():
   tryletter("Z")
def game_over():
   wordvar = word.get()
   msg = "Game Over !\nThe word was :\n" + wordvar
   gameover.config(text=msg)
   gameover.pack()
def win():
   gameover.config(text="You win !")
   gameover.pack()
#=========================================

#==================frame==================
mainframe = LabelFrame(main, text="Hangman game")
mainframe.pack(fill="both")
#:::
def go_back():
   mainframe.pack_forget()
   chooseframe.pack(fill="both")
#:::
wordl = Label(mainframe, textvariable = resultword)
wordl.pack()
#:::
tryf = Frame(mainframe, relief=FLAT)
tryf.pack(fill="both")
#---
gameover = Label(mainframe, text = "Game Over !")
gameover.pack()
#---
info1 = Label(tryf, text="Remaining tests :")
info1.pack(side=LEFT)
trynb_l = Label(tryf, textvariable = nbtry)
trynb_l.pack(side=LEFT)
#:::
#frames :
line1 = Frame(mainframe, relief=FLAT)
line1.pack(fill="both")
#---
line2 = Frame(mainframe, relief=FLAT)
line2.pack(fill="both")
#---
line3 = Frame(mainframe, relief=FLAT)
line3.pack(fill="both")
#---
line4 = Frame(mainframe, relief=FLAT)
line4.pack(fill="both")
#---
line5 = Frame(mainframe, relief=FLAT)
line5.pack(fill="both")
#buttons
#=A=
abutt = Button(line1, text="A", command=acom)
abutt.pack(fill="both", side=LEFT)
#=B=
bbutt = Button(line1, text="B", command=bcom)
bbutt.pack(fill="both", side=LEFT)
#=C=
cbutt = Button(line1, text="C", command=ccom)
cbutt.pack(fill="both", side=LEFT)
#=D=
dbutt = Button(line1, text="D", command=dcom)
dbutt.pack(fill="both", side=LEFT)
#=E=
ebutt = Button(line1, text="E", command=ecom)
ebutt.pack(fill="both", side=LEFT)
#=F=
fbutt = Button(line1, text="F", command=fcom)
fbutt.pack(fill="both", side=LEFT)
#=G=
gbutt = Button(line2, text="G", command=gcom)
gbutt.pack(fill="both", side=LEFT)
#=H=
hbutt = Button(line2, text="H", command=hcom)
hbutt.pack(fill="both", side=LEFT)
#=I=
ibutt = Button(line2, text="I", command=icom)
ibutt.pack(fill="both", side=LEFT)
#=J=
jbutt = Button(line2, text="J", command=jcom)
jbutt.pack(fill="both", side=LEFT)
#=K=
kbutt = Button(line2, text="K", command=kcom)
kbutt.pack(fill="both", side=LEFT)
#=L=
lbutt = Button(line2, text="L", command=lcom)
lbutt.pack(fill="both", side=LEFT)
#=M=
mbutt = Button(line3, text="M", command=mcom)
mbutt.pack(fill="both", side=LEFT)
#=N=
nbutt = Button(line3, text="N", command=ncom)
nbutt.pack(fill="both", side=LEFT)
#=O=
obutt = Button(line3, text="O", command=ocom)
obutt.pack(fill="both", side=LEFT)
#=P=
pbutt = Button(line3, text="P", command=pcom)
pbutt.pack(fill="both", side=LEFT)
#=Q=
qbutt = Button(line3, text="Q", command=qcom)
qbutt.pack(fill="both", side=LEFT)
#=R=
rbutt = Button(line3, text="R", command=rcom)
rbutt.pack(fill="both", side=LEFT)
#=S=
sbutt = Button(line4, text="S", command=scom)
sbutt.pack(fill="both", side=LEFT)
#=T=
tbutt = Button(line4, text="T", command=tcom)
tbutt.pack(fill="both", side=LEFT)
#=U=
ubutt = Button(line4, text="U", command=ucom)
ubutt.pack(fill="both", side=LEFT)
#=V=
vbutt = Button(line4, text="V", command=vcom)
vbutt.pack(fill="both", side=LEFT)
#=W=
wbutt = Button(line4, text="W", command=wcom)
wbutt.pack(fill="both", side=LEFT)
#=X=
xbutt = Button(line4, text="X", command=xcom)
xbutt.pack(fill="both", side=LEFT)
#=Y=
ybutt = Button(line5, text="Y", command=ycom)
ybutt.pack(fill="both", side=LEFT)
#=Z=
zbutt = Button(line5, text="Z", command=zcom)
zbutt.pack(fill="both", side=LEFT)
#"Go back" button :
backbutt = Button(mainframe, text="Go back", command=go_back)
backbutt.pack(fill="both")
#"Restart" button :
backbutt = Button(mainframe, text="Restart", command=run)
backbutt.pack(fill="both")
#Don't pack this frame :
mainframe.pack_forget()
#Don't pack the "game over !" label :
gameover.pack_forget()
#=========================================

#=========================================
#=========================================
#=========================================

#=========================================
#===Choose the dictionnary and launch the game===
#=========================================

#================commands================
def loaddict():
   filename = askopenfilename(title="Load your dictionnary",filetypes=[('Mibi dictionnaries','.mibidict'),('all files','.*')])
   dicoadress.set(filename)
   print(dicoadress.get())
def play():
   dictadress = dicoadress.get()
   print(dictadress)
   if dictadress != "":
      run()
   else:
      showerror("Error", "Please choose a dictionnary")
#==========================================
choosedictionnarybutt = Button(chooseframe, text="Load a dictionnary", command=loaddict)
choosedictionnarybutt.pack(fill="both")
#---
launchbutt = Button(chooseframe, text="Play !", command=play)
launchbutt.pack(fill="both")
#==========================================
#==========================================
#==========================================

main.mainloop()
