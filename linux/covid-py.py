from tkinter import *
from tkinter import messagebox
from bs4 import BeautifulSoup as bs
import requests
import json

root = Tk()
root.geometry("680x400")
root.resizable(width=False,height=False)
root.configure(bg="lavender")
root.title("COVID19-LIVE-STATS")


try:
	r = requests.get("https://api.covid19india.org/data.json")
	r1 = requests.get("https://www.ndtv.com/coronavirus/helpline-numbers")
	soup1 = bs(r1.text,'lxml')
	soup = bs(r.text,'lxml')

except:
	messagebox.showinfo("error","check your connection")

news = []
tab1 = soup1.find('table',{'class':'corona'})
d = {}
jdata = json.loads(soup.text)
for i in jdata['statewise']:
	d[i['state']] = [i['confirmed'],i['active'],i['deaths'],i['recovered']]
	title = i['lastupdatedtime']

for i in tab1.findAll('tr'):
	cnt = 0
	for dat in i.findAll('td'):
		if cnt == 0:
			#print(dat.text)
			if dat.text == "Andaman & Nicobar":
				take = "Andaman and Nicobar Islands"
			elif dat.text =="Jammu":
				take = "Jammu and Kashmir"
			elif dat.text in d.keys():
				take = dat.text
			else:
				continue
		else:
			d[take] += [dat.text]

			#print(take,dat.text)
		cnt +=1
fr = Frame(root)
fr.pack(side=LEFT)



fr2 = Frame(root)
fr2.pack(side=LEFT)

def openwin():
        r2 = requests.get("https://www.hindustantimes.com/topic/coronavirus")
        s = bs(r2.text,'lxml')
        news = []
        try:
            for i1 in s.findAll('div',{'class':'authorListing'}):
                    for j1 in i1.findAll('a'):
                            news.append((j1.text).split("read more"))
        except:
            messagebox.showinfo("check your connection or else contact to developer.")
        newwin = Toplevel(root)
        newwin.geometry("1340x720")
        newwin.title("NEWS-BOX")
        newwin.configure(bg="lavender")
        county  = 0
        newslab = Label(newwin,text="HINDUSTAN-TIMES-HEADLINES"+" (last updated:"+str(title)+")",font=("Verdana",18),fg="blue",bg="lavender")
        newslab.pack()
        for i2 in news:
                if len(i2[0]) > 14:
                        labnew2 = Label(newwin,text=str(county+1)+"."+i2[0],font=("Verdana",10),fg="black",bg = "lavender")
                        labnew2.place(y=50+40*county,x=10)
                        county +=1
def quit():
	root.destroy()

def datafetch():
	x = lbx.get(ACTIVE)
	#print(x)
	if x == "Andaman and Nicobar":
		x = "Andaman and Nicobar Islands"
	#print(x)
	try:
		lab2.config(text=str(x)+"\n"+title+"\n\n       Total Cases: "+d[x][0]+"\n\n         Deaths: "+d[x][2]+"\n\n        Active: "+d[x][1]+"\n\n        Recovered:"+ d[x][3]+"\n\n         Helpline:\n"+d[x][4],bg="lavender",fg="black")
	except:
		lab2.config(text=str(x)+"\n"+title+"\n\n        Total Cases: "+d[x][0]+"\n\n        Deaths: "+d[x][2]+"\n\n      Cured: "+d[x][1],bg="lavender",fg="black")

def contactus():
	win1 = Toplevel(root)
	win1.geometry("680x400")
	win1.title("CONTACT-US")
	win1.configure(bg="lavender")
	win1text = "Developers:\n\n1.SAGAR SINGH \nEMAIL: singh.sagar@protonmail.com \n\nURL: https://github.com/S4GAR \n\n\n2.ROHIT VARDHANI \nEMAIL:rohit.17jccs050@jietjodhpur.ac.in \n\nURL:https://github.com/carnage3881"
	win1lab = Label(win1,text=win1text,font=("Verdana",17),fg="black",bg = "lavender")
	win1lab.pack()
def help():
	win2 = Toplevel(root)
	win2.geometry("750x340")
	win2.title("HELP")
	win2.configure(bg="lavender")
	win2text = "\nThe application is built with considering the userfriendly interface.\nPerhaps, the Guidelines to use the applications are as follows:"
	win2text1 = "\n\n1.Drag the scroll bar to find your state. Once you find it, select the state with\n a mouse press.\n\n2.If the state is highlighted then only press the select button to get the data."
	win2text2 = "\n\n3.To get update from news headlines.Click on NEWS-BOX Button.\n\n\n\n # STAY SAFE STAY UPDATED."
	win2text = win2text + win2text1 + win2text2
	win2lab = Label(win2,text=win2text,font=("verdana",14),fg="black",bg="lavender")
	win2lab.pack()
def aboutapp():
	win3 = Toplevel(root)
	win3.geometry("700x380")
	win3.title("aboutapp")
	win3.configure(bg="lavender")
	win3text = "\nThe application is designed exclusively for windows.\n The application delivers the Novel corona live statistics of all the states \nand union territories and also integrates other features like a list\n of headlines that has been scraped from websites and a state-wise\n helpline numbers in case of an emergency."
	win3text1 = "\n\nCREDITS:\n\n All the data has been fetched from these respective sites. A huge thanks to them."
	win3text2 = "\n\n[1] https://www.mohfw.gov.in/ \n\n[2] https://www.ndtv.com/coronavirus/helpline-numbers \n\n[3] https://www.hindustantimes.com/topic/coronavirus \n\n\n #STAY HOME STAY SAFE & STAY UPDATED."
	win3text = win3text + win3text1 +win3text2
	win3lab = Label(win3,text=win3text,font={"verdana",20},fg="black",bg="lavender")
	win3lab.pack()



sbr = Scrollbar(fr,bg="red")
sbr.pack(side=RIGHT,fill="y")

lbx = Listbox(fr,font=("Verdona",16),bg="lavender blush",fg="black")
lbx.pack(side=LEFT,fill="x",expand=True)
c = 0
for i in d.keys():
	c +=1
	if i == "Andaman and Nicobar Islands":
		i = "Andaman and Nicobar"
	if i != "Cases being reassigned to states":
		lbx.insert(c,str(i))
	else:
		pass

sbr.config(command=lbx.yview)
lbx.config(yscrollcommand = sbr.set)

lab = Label(root,text="CORONA STATS",font=("Helvetica",18),padx=220,pady=5,bg="lavender",fg="black")
lab.place(x=0,y=0)

lab2 = Label(fr2,text="INDIA\n\n"+title+"\n\n Confirmed: "+d['Total'][0]+"\n\n Active: "+d['Total'][1]+"\n\n Death: "+d['Total'][2]+"\n\nRecovered: "+d['Total'][3]+"\n\nHelpLine No: "+'011-23978046',font=("Helvetica",16),bg="lavender",fg="black")
lab2.pack(side=TOP)

btn = Button(root,text="Select",font=("Verdana",16),command = datafetch)
btn.place(x=30,y=350)

#btn2 = Button(root,text="NEWS-BOX",font=("Verdana",14),command = openwin)
#btn2.place(x=150,y=350)
btn3 = Button(root,text="Quit",font=("Verdana",14),command= quit)
btn3.place(x=600,y=350)

menubar = Menu(root)
menubar.add_command(label="About-App",command=aboutapp,activeforeground='RED',font=("Verdana",14))
menubar.add_command(label="Contact-Us",command=contactus,activeforeground='RED',font=("Verdana",14))
menubar.add_command(label="Help",command=help,activeforeground='RED',font=("Verdana",14))

menubar.config(bg="lavender",fg='black')
root.config(menu = menubar)
root.mainloop()
