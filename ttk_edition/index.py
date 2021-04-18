from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from tkinter.messagebox import *
from random import *

#=== A hangman game by mibi88===

main = Tk()
main.title("Hangman game")
chooseframe = ttk.LabelFrame(main, text="Start a new game")
chooseframe.pack(fill="both", expand = True)
#=================variables=================
dicoadress = StringVar("")
word = StringVar("")
resultword = StringVar("")
wordlen = IntVar()
nbtry = IntVar()
letterspressed = StringVar("")
imgvar = StringVar("")
#=========================================

#=========================================
#================Main game================
#=========================================

#================commands================
# Bind this letters
def letterbind():
    main.bind("a",acom)
    main.bind("b",bcom)
    main.bind("c",ccom)
    main.bind("d",dcom)
    main.bind("e",ecom)
    main.bind("f",fcom)
    main.bind("g",gcom)
    main.bind("h",hcom)
    main.bind("i",icom)
    main.bind("j",jcom)
    main.bind("k",kcom)
    main.bind("l",lcom)
    main.bind("m",mcom)
    main.bind("n",ncom)
    main.bind("o",ocom)
    main.bind("p",pcom)
    main.bind("q",qcom)
    main.bind("r",rcom)
    main.bind("s",scom)
    main.bind("t",tcom)
    main.bind("u",ucom)
    main.bind("v",vcom)
    main.bind("w",wcom)
    main.bind("x",xcom)
    main.bind("y",ycom)
    main.bind("z",zcom)
    main.bind("A",acom)
    main.bind("B",bcom)
    main.bind("C",ccom)
    main.bind("D",dcom)
    main.bind("E",ecom)
    main.bind("F",fcom)
    main.bind("G",gcom)
    main.bind("H",hcom)
    main.bind("I",icom)
    main.bind("J",jcom)
    main.bind("K",kcom)
    main.bind("L",lcom)
    main.bind("M",mcom)
    main.bind("N",ncom)
    main.bind("O",ocom)
    main.bind("P",pcom)
    main.bind("Q",qcom)
    main.bind("R",rcom)
    main.bind("S",scom)
    main.bind("T",tcom)
    main.bind("U",ucom)
    main.bind("V",vcom)
    main.bind("W",wcom)
    main.bind("X",xcom)
    main.bind("Y",ycom)
    main.bind("Z",zcom)
def unbind_ev():
    main.unbind("a")
    main.unbind("b")
    main.unbind("c")
    main.unbind("d")
    main.unbind("e")
    main.unbind("f")
    main.unbind("g")
    main.unbind("h")
    main.unbind("i")
    main.unbind("j")
    main.unbind("k")
    main.unbind("l")
    main.unbind("m")
    main.unbind("n")
    main.unbind("o")
    main.unbind("p")
    main.unbind("q")
    main.unbind("r")
    main.unbind("s")
    main.unbind("t")
    main.unbind("u")
    main.unbind("v")
    main.unbind("w")
    main.unbind("x")
    main.unbind("y")
    main.unbind("z")
    main.unbind("A")
    main.unbind("B")
    main.unbind("C")
    main.unbind("D")
    main.unbind("E")
    main.unbind("F")
    main.unbind("G")
    main.unbind("H")
    main.unbind("I")
    main.unbind("J")
    main.unbind("K")
    main.unbind("L")
    main.unbind("M")
    main.unbind("N")
    main.unbind("O")
    main.unbind("P")
    main.unbind("Q")
    main.unbind("R")
    main.unbind("S")
    main.unbind("T")
    main.unbind("U")
    main.unbind("V")
    main.unbind("W")
    main.unbind("X")
    main.unbind("Y")
    main.unbind("Z")
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
   scroll = 0
   while scroll != len_selword:
      letter = selword[scroll:scroll + 1]
      totrypossibleletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
      if letter in totrypossibleletters:
         baddico = False
      else:
         errormsg = "Bad dictionnary\nBad letter \"" + letter + "\".\nError number 2"
         showerror("Error ...", errormsg)
         baddico = True
         break
      scroll += 1
   if baddico == False:
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
      mainframe.pack(fill = "both", expand = True)
      #hangman_drawing.pack(side = RIGHT, fill = "both", expand=True)
      letterbind()
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
def acom(event=None):
   tryletter("A")
def bcom(event=None):
   tryletter("B")
def ccom(event=None):
   tryletter("C")
def dcom(event=None):
   tryletter("D")
def ecom(event=None):
   tryletter("E")
def fcom(event=None):
   tryletter("F")
def gcom(event=None):
   tryletter("G")
def hcom(event=None):
   tryletter("H")
def icom(event=None):
   tryletter("I")
def jcom(event=None):
   tryletter("J")
def kcom(event=None):
   tryletter("K")
def lcom(event=None):
   tryletter("L")
def mcom(event=None):
   tryletter("M")
def ncom(event=None):
   tryletter("N")
def ocom(event=None):
   tryletter("O")
def pcom(event=None):
   tryletter("P")
def qcom(event=None):
   tryletter("Q")
def rcom(event=None):
   tryletter("R")
def scom(event=None):
   tryletter("S")
def tcom(event=None):
   tryletter("T")
def ucom(event=None):
   tryletter("U")
def vcom(event=None):
   tryletter("V")
def wcom(event=None):
   tryletter("W")
def xcom(event=None):
   tryletter("X")
def ycom(event=None):
   tryletter("Y")
def zcom(event=None):
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
mainframe = ttk.LabelFrame(main, text="Hangman game")
mainframe.pack(fill="both", expand = True)
#:::
def go_back():
   mainframe.pack_forget()
   chooseframe.pack(fill="both", expand = True)
   unbind_ev()
#:::
leftframe = ttk.Frame(mainframe, relief=FLAT)
leftframe.pack(fill="both", expand = True, side = LEFT)

wordl = ttk.Label(leftframe, textvariable = resultword)
wordl.pack()
#:::
tryf = ttk.Frame(leftframe, relief=FLAT)
tryf.pack(fill="both")
#---
gameover = ttk.Label(leftframe, text = "Game Over !")
gameover.pack()
#---
info1 = ttk.Label(tryf, text="Remaining tests :")
info1.pack(side=LEFT)
trynb_l = ttk.Label(tryf, textvariable = nbtry)
trynb_l.pack(side=LEFT)
#:::
#frames :
line1 = ttk.Frame(leftframe, relief=FLAT)
line1.pack(fill="both", expand = True)
#---
line2 = ttk.Frame(leftframe, relief=FLAT)
line2.pack(fill="both", expand = True)
#---
line3 = ttk.Frame(leftframe, relief=FLAT)
line3.pack(fill="both", expand = True)
#---
line4 = ttk.Frame(leftframe, relief=FLAT)
line4.pack(fill="both", expand = True)
#---
line5 = ttk.Frame(leftframe, relief=FLAT)
line5.pack(fill="both", expand = True)
#buttons
#=A=
abutt = ttk.Button(line1, text="A", command=acom)
abutt.pack(side=LEFT, fill="both", expand = True)
#=B=
bbutt = ttk.Button(line1, text="B", command=bcom)
bbutt.pack(side=LEFT, fill="both", expand = True)
#=C=
cbutt = ttk.Button(line1, text="C", command=ccom)
cbutt.pack(side=LEFT, fill="both", expand = True)
#=D=
dbutt = ttk.Button(line1, text="D", command=dcom)
dbutt.pack(side=LEFT, fill="both", expand = True)
#=E=
ebutt = ttk.Button(line1, text="E", command=ecom)
ebutt.pack(side=LEFT, fill="both", expand = True)
#=F=
fbutt = ttk.Button(line1, text="F", command=fcom)
fbutt.pack(side=LEFT, fill="both", expand = True)
#=G=
gbutt = ttk.Button(line2, text="G", command=gcom)
gbutt.pack(side=LEFT, fill="both", expand = True)
#=H=
hbutt = ttk.Button(line2, text="H", command=hcom)
hbutt.pack(side=LEFT, fill="both", expand = True)
#=I=
ibutt = ttk.Button(line2, text="I", command=icom)
ibutt.pack(side=LEFT, fill="both", expand = True)
#=J=
jbutt = ttk.Button(line2, text="J", command=jcom)
jbutt.pack(side=LEFT, fill="both", expand = True)
#=K=
kbutt = ttk.Button(line2, text="K", command=kcom)
kbutt.pack(side=LEFT, fill="both", expand = True)
#=L=
lbutt = ttk.Button(line2, text="L", command=lcom)
lbutt.pack(side=LEFT, fill="both", expand = True)
#=M=
mbutt = ttk.Button(line3, text="M", command=mcom)
mbutt.pack(side=LEFT, fill="both", expand = True)
#=N=
nbutt = ttk.Button(line3, text="N", command=ncom)
nbutt.pack(side=LEFT, fill="both", expand = True)
#=O=
obutt = ttk.Button(line3, text="O", command=ocom)
obutt.pack(side=LEFT, fill="both", expand = True)
#=P=
pbutt = ttk.Button(line3, text="P", command=pcom)
pbutt.pack(side=LEFT, fill="both", expand = True)
#=Q=
qbutt = ttk.Button(line3, text="Q", command=qcom)
qbutt.pack(side=LEFT, fill="both", expand = True)
#=R=
rbutt = ttk.Button(line3, text="R", command=rcom)
rbutt.pack(side=LEFT, fill="both", expand = True)
#=S=
sbutt = ttk.Button(line4, text="S", command=scom)
sbutt.pack(side=LEFT, fill="both", expand = True)
#=T=
tbutt = ttk.Button(line4, text="T", command=tcom)
tbutt.pack(side=LEFT, fill="both", expand = True)
#=U=
ubutt = ttk.Button(line4, text="U", command=ucom)
ubutt.pack(side=LEFT, fill="both", expand = True)
#=V=
vbutt = ttk.Button(line4, text="V", command=vcom)
vbutt.pack(side=LEFT, fill="both", expand = True)
#=W=
wbutt = ttk.Button(line4, text="W", command=wcom)
wbutt.pack(side=LEFT, fill="both", expand = True)
#=X=
xbutt = ttk.Button(line4, text="X", command=xcom)
xbutt.pack(side=LEFT, fill="both", expand = True)
#=Y=
ybutt = ttk.Button(line5, text="Y", command=ycom)
ybutt.pack(side=LEFT, fill="both", expand = True)
#=Z=
zbutt = ttk.Button(line5, text="Z", command=zcom)
zbutt.pack(side=LEFT, fill="both", expand = True)
#"Go back" button :
backbutt = ttk.Button(leftframe, text="Go back", command=go_back)
backbutt.pack(fill="both", expand = True)
#"Restart" button :
backbutt = ttk.Button(leftframe, text="Restart", command=run)
backbutt.pack(fill="both", expand = True)
#===
#Don't pack this frame :
mainframe.pack_forget()
#hangman_drawing.pack_forget()
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
   filename = askopenfilename(title="Load your dictionnary.",filetypes=[('Mibi dictionnaries','.mibidict'),('all files','.*')])
   dicoadress.set(filename)
   print(dicoadress.get())
def play():
   dictadress = dicoadress.get()
   print(dictadress)
   if dictadress != "":
      run()
   else:
      showerror("Error", "Please choose a dictionnary.\nError number 1")
#==========================================
choosedictionnarybutt = ttk.Button(chooseframe, text="Load a dictionnary", command=loaddict)
choosedictionnarybutt.pack(fill="both", expand = True)
#---
launchbutt = ttk.Button(chooseframe, text="Play !", command=play)
launchbutt.pack(fill="both", expand = True)
#==========================================
#==========================================
#==========================================

main.mainloop()