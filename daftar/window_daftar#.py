import tkinter as tk
    

height = 1000
width = 1500
root = tk.Tk()

canvas = tk.Canvas(root,width = width,height = height)
canvas.pack()
control = "jancok"

#alamat

alamat_frame = tk.Frame(root,bg ="#80c1ff" ,bd=15)
alamat_frame.place(relx= 0.3,rely=0.05,relwidth= 0.5 ,relheight = 0.15,anchor = "n")

alamat_text = tk.Entry(alamat_frame,font = 40 ,bg="#f5ab45",)
alamat_text.place(relwidth = 0.65,relheight = 0.9)

alamat_label=tk.Label(alamat_frame,text="alamat",font = 40)
alamat_label.place(relx= 0.3,rely = 0.92,relwidth = 0.3,relheight = 0.25,anchor = "n")

alamat_button = tk.Button(alamat_frame,text="input",bg="grey")
alamat_button.place(relx=0.7,relheight=1,relwidth=0.3)


#bereich

bereich_frame = tk.Frame(root,bg ="#80c1ff" ,bd=15)
bereich_frame.place(relx= 0.3,rely=0.2,relwidth= 0.5 ,relheight = 0.15,anchor = "n")

bereich_text = tk.Entry(bereich_frame,font = 40 ,bg="#f5ab45",)
bereich_text.place(relwidth = 0.65,relheight = 0.9)

bereich_label=tk.Label(bereich_frame,text="im bereich",font = 40)
bereich_label.place(relx= 0.3,rely = 0.92,relwidth = 0.3,relheight = 0.25,anchor = "n")

bereich_button = tk.Button(bereich_frame,text="input",bg="grey")
bereich_button.place(relx=0.7,relheight=1,relwidth=0.3)

#tanggal

tanggal_frame = tk.Frame(root,bg ="#80c1ff" ,bd=15)
tanggal_frame.place(relx= 0.3,rely=0.35,relwidth= 0.5 ,relheight = 0.1,anchor = "n")

tanggal_text = tk.Entry(tanggal_frame,font = 40 ,bg="#f5ab45",)
tanggal_text.place(relwidth = 0.65,relheight = 0.9)

tanggal_label=tk.Label(tanggal_frame,text="website gefunden",font = 40)
tanggal_label.place(relx= 0.3,rely = 0.92,relwidth = 0.3,relheight = 0.25,anchor = "n")

tanggal_button = tk.Button(tanggal_frame,text="input",bg="grey")
tanggal_button.place(relx=0.7,relheight=1,relwidth=0.3)

#namafirma

firma_frame = tk.Frame(root,bg ="#80c1ff" ,bd=15)
firma_frame.place(relx= 0.3,rely=0.45,relwidth= 0.5 ,relheight = 0.1,anchor = "n")

firma_text = tk.Entry(firma_frame,font = 40 ,bg="#f5ab45",)
firma_text.place(relwidth = 0.65,relheight = 0.9)

firma_label=tk.Label(firma_frame,text="nama firma",font = 40)
firma_label.place(relx= 0.3,rely = 0.92,relwidth = 0.3,relheight = 0.25,anchor = "n")

firma_button = tk.Button(firma_frame,text="input",bg="grey",)
firma_button.place(relx=0.7,relheight=1,relwidth=0.3)



#ab
abval= ""
def getabval(ab_text):
    abval = ab_text
ab_frame = tk.Frame(root,bg ="#80c1ff" ,bd=15)
ab_frame.place(relx= 0.3,rely=0.55,relwidth= 0.5 ,relheight = 0.1,anchor = "n")

ab_text = tk.Entry(ab_frame,font = 40 ,bg="#f5ab45",)
ab_text.place(relwidth = 0.65,relheight = 0.9)

ab_label=tk.Label(ab_frame,text="praktikum ab ",font = 40)
ab_label.place(relx= 0.3,rely = 0.92,relwidth = 0.3,relheight = 0.25,anchor = "n")

ab_button = tk.Button(ab_frame,text="input",bg="grey",command=lambda :getabval(ab_text.get()))
ab_button.place(relx=0.7,relheight=1,relwidth=0.3)

#nama orang&sex

orangsex_frame = tk.Frame(root,bg ="#80c1ff" ,bd=15)
orangsex_frame.place(relx= 0.3,rely=0.65,relwidth= 0.5 ,relheight = 0.1,anchor = "n")

orangsex_text = tk.Entry(orangsex_frame,font = 40 ,bg="#f5ab45",)
orangsex_text.place(relwidth = 0.65,relheight = 0.9)

orangsex_label=tk.Label(orangsex_frame,text="nama orang 1",font = 40)
orangsex_label.place(relx= 0.3,rely = 0.92,relwidth = 0.3,relheight = 0.25,anchor = "n")

orangsex_button = tk.Button(orangsex_frame,text="input",bg="grey",)
orangsex_button.place(relx=0.7,relheight=1,relwidth=0.3)

#sex 0=male 1=Female
framesex = tk.Frame (orangsex_frame)
var = tk.IntVar()
framesex.place(relx= 0.6,relwidth= 0.15 ,relheight = 0.9,anchor = "n")
R1 = tk.Radiobutton(framesex, text="Male", variable=var, value=0)

R1.pack( anchor = "w" )

R2 = tk.Radiobutton(framesex, text="Female", variable=var, value=1)
R2.pack( anchor = "w" )

#nama orang 2

orangsex_frame_2 = tk.Frame(root,bg ="#80c1ff" ,bd=15)
orangsex_frame_2.place(relx= 0.3,rely=0.75,relwidth= 0.5 ,relheight = 0.14,anchor = "n")

orangsex_text2 = tk.Entry(orangsex_frame_2,font = 40 ,bg="#f5ab45",)
orangsex_text2.place(relwidth = 0.65,relheight = 0.9)

orangsex_label2=tk.Label(orangsex_frame_2,text="nama orang 2",font = 40)
orangsex_label2.place(relx= 0.3,rely = 0.92,relwidth = 0.3,relheight = 0.25,anchor = "n")

orangsex_button2 = tk.Button(orangsex_frame_2,text="input",bg="grey",)
orangsex_button2.place(relx=0.7,relheight=1,relwidth=0.3)

#sex 0=male 1=Female
framesex = tk.Frame (orangsex_frame_2)
var2 = tk.IntVar()
framesex.place(relx= 0.6,relwidth= 0.15 ,relheight = 0.9,anchor = "n")
R3 = tk.Radiobutton(framesex, text="Male", variable=var2, value=2)

R3.pack( anchor = "w" )

R4 = tk.Radiobutton(framesex, text="Female", variable=var2, value=3)
R4.pack( anchor = "w" )

R5 = tk.Radiobutton(framesex, text="keine", variable=var2, value=4)
R5.pack( anchor = "w" )


#fulltext
motivation_1 = "\n\nauf ihre Anzeige am "
motivation_2= " bin ich an die Stellenausschreibung für ein Pflichtpraktikum aufmerksam geworden. Aktuell befinde ich mich im 11.Semester des Bachelorstudium im Fach Elektro-Informationstechnik am Karlsruher Institute für Technologie. Ich bin sehr interessiert an der Aussicht auf ein Praktikum in Ihrem Unternehmen absolvieren zu dürfen. Ich möchte mein Pflichtpraktikum ab "
motivation_3 = " für 13 Wochen machen.\n \nDurch den verschiedenen Workshops und Praktikum, die ich während meinem Studium gemacht habe , habe ich gelernt meine Kenntnisse und technischen Fähigkeiten umzusetzen um ein Problem zu lösen z.B. Hardwarenähe Programmierung, Messdaten erfassen, auswerten, und visualisieren mit MATLAB, Schaltung-Design für Audiofilter und Sensoren mit LTspice, sowie praktische Fähigkeit mit Digitalmultimeter, Oszilloskop, und Funktionsgenerator. Neben meine Studium programmiere ich in meinem Freizeit gelegenheitlich verschiedene Projekten mit Python. Weiterhin bin ich eine neugierige und zielorientierte Person und freue mich darauf, mein erworbenes Wissen zur Anwendung zu bringen. Die Technologie entwickelt sich immer weiter und ich bin bereit neue Dinge zu lernen. \n \n Außerhalb meines Studiums Arbeite ich auch bei der Vereinigung indonesischer Studenten, in dem ich als Ausschuss bei verschiedenen Veranstaltungen beteiligte. Ich arbeite auch bei International Student Office an der KIT. Ich sammelte Arbeitserfahrungen, wie man mit Kunden, Kollegen, und Vorgesetzten, umgehen soll. Was ich für wichtig halte ist, wenn man als ein Team zusammen auf ein Ziel hinarbeitet, ist alles möglich. \n\n Ich finde ein Praktikum ist einer der wichtigsten Schritte um ins Berufsleben zu kommen und daher ist es wichtig, es bei der richtigen Firma zu absolvieren. "
motivation_4 = "ist ein zukunftsorientiertes Unternehmen und ich bin sicher, wenn ich bei Ihnen absolvieren dürfte, ist meine Zukunft im Teil „gesichert“. Daher bewerbe ich mich für einen Praktikumsstelle bei Ihnen. Ich freue mich auf die Möglichkeit diese Erfahrungen und Kenntnisse bei Ihnen anzubringen. Ich freue mich sehr über eine Einladung zu einem persönlichen Gespräch und verbleibe"
def keluar():
    namafirma = firma_text.get()
    abval= ab_text.get()
    namaorang = orangsex_text.get() +", "
    namaorang2 = orangsex_text2.get() +","
    website = tanggal_text.get()
    fall= var.get()
    fall2 = var2.get()
    clear()
    if fall == 0 :
        grüß = "Sehr geehrter Herr "
        if namaorang2 == "":
            fulltext_text.insert(tk.INSERT,grüß + namaorang  + motivation_1 + website + motivation_2 + abval +   motivation_3 + namafirma + " " + motivation_4)
        else:
            if fall2 == 2:
                grüß2 = "Sehr geehrter Herr "
                fulltext_text.insert(tk.INSERT,grüß + namaorang + grüß2  + namaorang2 + motivation_1+website+motivation_2 + abval +   motivation_3 + namafirma + " " + motivation_4)
            elif fall2 == 3:
                grüß2 = "Sehr geehrte Frau "
                fulltext_text.insert(tk.INSERT,grüß + namaorang +grüß2+ namaorang2+ motivation_1+website+motivation_2 + abval +   motivation_3 + namafirma + " " + motivation_4)
            else :
                fulltext_text.insert(tk.INSERT,grüß + namaorang + motivation_1 + website+ motivation_2 + abval +   motivation_3 + namafirma + motivation_4)

    elif fall ==1 :
        grüß = "Sehr geehrte Frau "
        if namaorang2 == "":
            fulltext_text.insert(tk.INSERT,grüß + namaorang + motivation_1 + website + motivation_2 + abval +   motivation_3 + namafirma + " " + motivation_4)
        else:
            if fall2 == 2:
                grüß2 = "Sehr geehrter Herr "
                fulltext_text.insert(tk.INSERT,grüß + namaorang + grüß2 + namaorang2 + motivation_1 + website + motivation_2 + abval  + motivation_3 + namafirma + " " + motivation_4)
            elif fall2 == 3:
                grüß2 = "Sehr geehrte Frau "
                fulltext_text.insert(tk.INSERT,grüß + namaorang + grüß2 + namaorang2  + motivation_1 + website + motivation_2 + abval +  motivation_3 + namafirma + " " + motivation_4)
            else:
                fulltext_text.insert(tk.INSERT,grüß + namaorang + motivation_1 + website + motivation_2 + abval + motivation_3 + namafirma + " " + motivation_4)


def clear ():
    fulltext_text.delete("1.0",tk.END)



fulltext_frame = tk.Frame(root,bg ="#80c1ff" ,bd=15)
fulltext_frame.place(relx= 0.55,rely=0.05,relwidth= 0.4 ,relheight = 0.8,anchor = "nw")

fulltext_button=tk.Button(fulltext_frame,text="fulltext",font = 40,command=lambda : keluar())
fulltext_button.place(relx=0.5 ,rely = 0.9,relwidth = 0.3,relheight = 0.1,anchor = "n")

fulltext_button=tk.Button(fulltext_frame,text="clear",font = 40,command=lambda : clear())
fulltext_button.place(relx=0.85 ,rely = 0.9,relwidth = 0.3,relheight = 0.1,anchor = "n")

fulltext_text = tk.Text(fulltext_frame,font = 40 ,bg="#f5ab45",)
fulltext_text.place(relwidth = 1,relheight = 0.9)





'''
#adjektiv
adjektiv_frame = tk.Frame(root,bg ="#80c1ff" ,bd=15)
adjektiv_frame.place(relx= 0.3,rely=0.75,relwidth= 0.5 ,relheight = 0.1,anchor = "n")

orangsex_text = tk.Entry(adjektiv_frame,font = 40 ,bg="#f5ab45",)
orangsex_text.place(relwidth = 0.65,relheight = 0.9)

orangsex_label=tk.Label(adjektiv_frame,text="adjektiv",font = 40)
orangsex_label.place(relx= 0.3,rely = 0.92,relwidth = 0.3,relheight = 0.25,anchor = "n")

orangsex_button = tk.Button(adjektiv_frame,text="input",bg="grey")
orangsex_button.place(relx=0.7,relheight=1,relwidth=0.3)
'''

root.mainloop()



