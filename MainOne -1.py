import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter.messagebox import askyesno
import socket
import dns.resolver
import sys
from bs4 import BeautifulSoup
import requests
from tkinter import messagebox
import os
from threading import Thread
import time
import threading
import re

root = tk.Tk()
root.geometry('1350x800')
root.title("Project")
root.config(bg="white")
root.resizable(False, False)

iptext = tk.StringVar()
ip1 = tk.StringVar()
filename = tk.StringVar()
text1 = tk.StringVar()
##img = Image.open('1.png')
##rezimg  = img.resize((700,750))
##messagebox.showinfo('Welcome','Welcome to INFOGAIN')
##image = ImageTk.PhotoImage(rezimg)
##label1 = tk.Label(root,image=image).place(x=0,y=0)
bgpic = Image.open("8.jpg")
bgpic1 = bgpic.resize((1350,950))
bgpic2 = ImageTk.PhotoImage(bgpic1)
label1 = tk.Label(root,image=bgpic2).place(x=0,y=0)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@------------------------------------------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##########...............

def onEnter2(e):
    inp.delete(0,"end")
def onLeave2(e):
    text = iptext.get()
    if text == "":
        inp.insert(0,"Enter Website Address")

def tools():
    toolWindow = tk.Toplevel(root)
    toolWindow.geometry("1350x800")
    toolWindow.config(bg="#f1b9fa")
    toolWindow.title("Tools")
    bgpic = Image.open("bg.jpg")
    bgpic1 = bgpic.resize((1350,800))
    bgpic2 = ImageTk.PhotoImage(bgpic1)
    label1 = tk.Label(toolWindow,image=bgpic2).place(x=0,y=0)
    website = iptext.get()
    if website == "Enter Website Address":
        website = "Website address Not Entered"
    try:
        ip = socket.gethostbyname(website)
    except socket.error:
        ip = "Can't find the ip address"
    tk.Label(toolWindow,text="Website Address    :",fg="Red",font=("Arial 15 italic"),bg="#c3c3c2").place(x=5,y=2)
    tk.Label(toolWindow,text=website,fg="Black",font=("Arial 15 italic"),bg="#c3c3c2").place(x=250,y=2)
    tk.Label(toolWindow,text="Website IP             :",fg="Red",font=("Arial 15 italic"),bg="#c3c3c2").place(x=5,y=30)
    tk.Label(toolWindow,text=ip,fg="Black",font=("Arial 15 italic"),bg="#c3c3c2").place(x=250,y=30)

    toolName = Label(toolWindow,text="INFO GAIN",fg="red",bg="black",font=("Times 25 italic"))
    toolName.place(x=900,y=20)

  #OUTPUT-------OUTPUT---------OUTPUT-------------OUTPUT--------OUTPUT--------OUTPUT--------OUTPUT------OUTPUT
    opFrame = Frame(toolWindow,width=645,height=650,bg='black') #,highlightbackground="blue",highlightthickness=2
    opFrame.place(x=690,y=75)
    opText = Text(opFrame,height=34,width=70,bg='#302f2a',fg='white',font=("Arial 13 bold"),wrap='word')
    opText.place(x=0,y=0)
    
    #toolFrame = Frame(toolWindow,width=640,height=700,bg='#d9dbdb').place(x=20,y=75) #,highlightbackground="blue",highlightthickness=2

  #SUBDOMAIN------SUBDOMAIN--------SUBDOMAIN--------SUBDOMAIN------SUBDOMAIN----------SUBDOMAIN
    #donnain=input("Enter the domain : ")
    def subdo():
        toolName['text']='Sub Domains'
        toolName['fg']="white"
        opText['highlightbackground'] = 'blue'
        opText['highlightthickness'] = 2
        file1=open('names.txt','r')
        Lines=file1.read()
        list1=Lines.split('\n')
        domain = website.split('.',1)[1]
        if opText != None:
            opText.delete('1.0',END)
        subd=[]
    #    list2 = []
        for subdon in list1:
            try:
                ip_value=dns.resolver.resolve(f'{subdon}.{domain}','A')
                if ip_value:
                    subd.append(f'{subdon}.{domain}')
                    if f"{subdon}.{domain}" in subd:
                        opText.insert(END,f'{subdon}.{domain}\n')                        #print(f'{subdon}.{donnain}')
                        #print(f'{subdon}.{domain}\n')
                    #  tk.op.pack(expand=1,fill = BOTH)
                    #print('Subdomain found')
            except dns.resolver.NXDOMAIN:
                pass
            except dns.resolver.NoAnswer:
                pass
            except KeyboardInterrupt:
                quit()
       # print(list2)
    subdopic = Image.open("domain.png")
    subdopicresize1 = subdopic.resize((75,75))
    subdopicresize3 = ImageTk.PhotoImage(subdopicresize1)    
    p1=Button(toolWindow,text="Sub-Domain",width=11,bg="#c3c3c2",cursor="hand2 red",border=0,font=("courier 12 italic bold"),fg="blue",command = subdo).place(x=130,y=190)
    l1=Label(toolWindow,image = subdopicresize3,fg="#e0556a",height=105,width=105,bg="#c3c3c2").place(x=130,y=80)

  #DNSLOOKUP--------------DNSLOOKUP-------------DNSLOOKUP-------------DNSLOOKUP-------------DNSLOOKUP
    def dnsLookup():
        toolName['text']='DNS Information'
        toolName['fg']="blue"
        opText['highlightbackground'] = 'green'
        opText['highlightthickness'] = 2
        record_types=['A','AAAA','NS','CNAME','MX','PTR','SOA','TXT']
        domain = website.split('.',1)[1]
        if opText != None:
            opText.delete('1.0',END)
        for records in record_types:
            try:
                answer=dns.resolver.resolve(domain,records)
                opText.insert(END,f'\n{records} Records\n')
            #print("*"*30)
                for server in answer:
                    opText.insert(END,server.to_text()+"\n")
            except dns.resolver.NXDOMAIN:
                opText.insert(END,f'{domain} doesn''t exist\n')
                quit()
            except dns.resolver.NoAnswer:
                opText.insert(END,'No record\n')
            except KeyboardInterrupt:
                opText.insert(END,'You enterupted\n')
                quit()
    dnspic = Image.open("dns.png")
    dnspicresize1 = dnspic.resize((75,75))
    dnspicresize3 = ImageTk.PhotoImage(dnspicresize1)
    p1=Button(toolWindow,text="DNS-Lookup",width=11,bg="#c3c3c2",cursor="hand2 red",border=0,font=("courier 12 italic bold"),fg="red",command = dnsLookup).place(x=370,y=190)
    l1=Label(toolWindow,image = dnspicresize3,fg="#e0556a",height=105,width=105,bg="#c3c3c2").place(x=370,y=80)
    
  #OPENPORT--------OPENPORT---------OPENPORT--------OPENPORT---------OPENPORT--------OPENPORT---------OPENPORT--------OPENPORT
    def openPorts():
        if opText != None:
            opText.delete('1.0',END)
        portsList = []
        port_info={20:"FTP. An outdated and insecure protocol, which utilize no encryption for both data transfer and authentication",21:"FTP. An outdated and insecure protocol, which utilize no encryption for both data transfer and authentication",22:"SSH. Typically, it is used for remote management. While it is generally considered secure, it requires proper key management.",23:"Telnet. A predecessor to SSH, is no longer considered secure and is frequently abused by malware",25:"SMTP. If not properly secured, it can be abused for spam e-mail distribution",53:"DNS. Very often used for amplification DDoS attacks",139:"NetBIOS. Legacy protocol primarily used for file and printer sharing",80:"Used by HTTP and HTTPS. HTTP servers and their various components are very exposed and often sources of attacks",443:"Used by HTTP and HTTPS. HTTP servers and their various components are very exposed and often sources of attacks",445:"SMB. Provides sharing capabilities of files and printers. Used in the 2017 WannaCry attack",1433:"SQL Server and MySQL default ports – used for malware distribution.",1434:"SQL Server and MySQL default ports – used for malware distribution.",3306:"SQL Server and MySQL default ports – used for malware distribution.",3389:"Remote Desktop. Utilized to exploit various vulnerabilities in remote desktop protocols, as well as weak user authentication. Remote desktop vulnerabilities are commonly used in real world attacks",80:"Hypertext Transfer Protocol (HTTP). It is the default network port used to send and receive unencrypted web pages",443:"HTTPS (Hypertext Transfer Protocol Secure) is a secured HTTP version where all traffic is bind with strong encryption that passes through 443. This port is also connected with TCP protocol and creates a secure connection between the webpages and browser"}
        def scan_port(port) :
            #print("scanning Port:",port)
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(3)
            conn=s.connect_ex((target,port))
            if(not conn):
                opText.insert(END,"Port {} is open\n".format(port))
                portsList.append(port)
                if port in port_info:
                    opText.insert(END,port_info[port]+'\n\n')
                time.sleep(5)
                    
            s.close()
        domain = website.split('.',1)[1]
        target=socket.gethostbyname(website)
        start_port=2
        end_port=5000
        try:
            for port in range(start_port,end_port+1):
                thread=threading.Thread(target=scan_port,args=(port,))
                thread.daemon=False
               # thread.start()
                try:
                    thread.start()
                except RuntimeError:
                    pass    
        except KeyboardInterrupt:
            opText.insert(END,'You quit this process')
    openportpic = Image.open("openport1.png")
    openportpicresize1 = openportpic.resize((75,75))
    openportpicresize3 = ImageTk.PhotoImage(openportpicresize1)
##    p1=Button(toolWindow,image = openportpicresize3,text="Team",height=105,width=105,bg="white",border=1,command = None).place(x=130,y=290)
##    l1=Label(toolWindow,text="Open Ports",font=("courier 15 italic bold"),fg="#e0556a",width=13,bg="#ebf0ec").place(x=99,y=410)
    p1=Button(toolWindow,text="Open Ports",width=11,bg="#c3c3c2",cursor="hand2 red",border=0,font=("courier 12 italic bold"),fg="green",command = openPorts).place(x=130,y=370)
    l1=Label(toolWindow,image = openportpicresize3,fg="#e0556a",height=105,width=105,bg="#c3c3c2").place(x=130,y=260)

  #WhoISLookUP-------WhoISLookUP--------WhoISLookUP-------WhoISLookUP--------WhoISLookUP-------WhoISLookUP--------WhoISLookUP
    def whoIsData():
        toolName['text']='Website Information'
        toolName['fg']="green"
        opText['highlightbackground'] = 'yellow'
        opText['highlightthickness'] = 2
        if opText != None:
            opText.delete('1.0',END)
        try: 
            r=requests.get(f'https://{website}')
            response=r.status_code
        except:
            #messagebox.showwarning("Warning","THE Domain is not avaible.Check again and type")
            pass
        don=website.split('.',1)[1]
       # print(don)
        r=requests.get(f'https://www.whois.com/whois/{don}').text
        soup=BeautifulSoup(r,'lxml')
        rate=soup.find('div',attrs={'class':'whois-data'})
        for i in rate.findAll('div',attrs={'class':'df-row'}):
            labell=i.find('div',attrs={'class':'df-label'}).text
            value=i.find('div',attrs={'class':'df-value'}).text
            opText.insert(END,f'{labell}{value}\n')
    whoispic = Image.open("whois.jpg")
    whoispicresize1 = whoispic.resize((75,75))
    whoispicresize3 = ImageTk.PhotoImage(whoispicresize1)
##    p1=Button(toolWindow,image = whoispicresize3,text="Team",height=105,width=105,bg="white",border=1,command = whoIsData).place(x=370,y=290)
##    l1=Label(toolWindow,text="WhoIs-LookUp",font=("courier 15 italic bold"),fg="#e0556a",width=13,bg="#ebf0ec").place(x=350,y=410)
    p1=Button(toolWindow,text="WhoIs-LookUp",width=13,bg="#c3c3c2",cursor="hand2 red",border=0,font=("courier 12 italic bold"),fg="yellow",command = whoIsData).place(x=370,y=370)
    l1=Label(toolWindow,image = whoispicresize3,fg="#e0556a",height=105,width=105,bg="#c3c3c2").place(x=370,y=260)
    
  #SUBDOMAINLIVE---------SUBDOMAINLIVE---------SUBDOMAINLIVE---------SUBDOMAINLIVE---------SUBDOMAINLIVE---------SUBDOMAINLIVE
    def subdoLive():
        toolName['text']='SubDomains Live'
        toolName['fg']="pink"
        opText['highlightbackground'] = 'white'
        opText['highlightthickness'] = 2
        command_argv="python subdo.py "+website
        os.system(command_argv)
    addpic = Image.open("domain2.jpg")
    addpicresize1 = addpic.resize((75,75))
    addpicresize3 = ImageTk.PhotoImage(addpicresize1)
##    p1=Button(toolWindow,image = addpicresize3,text="Team",height=105,width=105,bg="white",border=1,command = subdoLive).place(x=130,y=460)
##    l1=Label(toolWindow,text="SubDomains Live",font=("courier 15 italic bold"),fg="#e0556a",width=17,bg="#ebf0ec").place(x=96,y=580)
    p1=Button(toolWindow,text="Sub-Domain Live",width=15,bg="#c3c3c2",cursor="hand2 red",border=0,font=("courier 12 italic bold"),fg="gold",command = subdoLive).place(x=110,y=540)
    l1=Label(toolWindow,image = addpicresize3,fg="#e0556a",height=105,width=105,bg="#c3c3c2").place(x=130,y=430)   
  #SAVESUBDOMAIN---------SAVESUBDOMAIN---------SAVESUBDOMAIN---------SAVESUBDOMAIN---------SAVESUBDOMAIN---------SAVESUBDOMAIN
    def subdomainSave():
        if  opText != None:
            opText.delete('1.0',END)
        def onEnter(e):
            inpEntry.delete(0,"end")
        def onLeave(e):
            text1 = opText.get()
            if text1 == "":
                inpEntry.insert(0,"Enter File Name...")
        def subdosave():
            file_name = filename.get()
            domain=website.split('.',1)[1]
            file1=open('names1.txt','r')
            Lines=file1.read()
            list1=Lines.split('\n')
            file2=open(file_name,'w')
            subd=[]
            for subdon in list1:
                try:
                    ip_value=dns.resolver.resolve(f'{subdon}.{domain}','A')
                    if ip_value:
                        subd.append(f'{subdon}.{domain}')
                        if f"{subdon}.{domain}" in subd:
                            file2.write(f'{subdon}.{domain}')
                            file2.write('\n')
                except dns.resolver.NXDOMAIN:
                    pass
                except dns.resolver.NoAnswer:
                    pass
                except KeyboardInterrupt:
                    quit()
            time.sleep(8+7)
            inpEntry.place_forget()
            inpsubbtn.place_forget()
            toolName.place(x=900,y=20)
        toolName.place_forget()
        opText['highlightbackground'] = 'pink'
        opText['highlightthickness'] = 2
        inpEntry = Entry(toolWindow,textvariable=filename,width=50,font=("Arial 13 italic bold"),fg='red')
        inpEntry.place(x=720,y=30)
        inpEntry.insert(END,"Enter File Name...")
        inpEntry.bind('<FocusIn>',onEnter)
        inpEntry.bind('<FocusOut>',onLeave)
        inpsubbtn = Button(toolWindow,text="Submit",width = 9,height=1,command=subdosave,fg="white",bg="blue")
        inpsubbtn.place(x=1220,y=30)

    
    add1pic = Image.open("domain1.png")
    add1picresize1 = add1pic.resize((75,75))
    add1picresize3 = ImageTk.PhotoImage(add1picresize1)
##    p1=Button(toolWindow,image = add1picresize3,text="Team",height=105,width=105,bg="white",border=1,command = subdomainSave).place(x=370,y=460)
##    l1=Label(toolWindow,text="Save SubDomains",font=("courier 15 italic bold"),fg="#e0556a",width=17,bg="#ebf0ec").place(x=346,y=580)
    p1=Button(toolWindow,text="Save Sub-Domains",width=16,bg="#c3c3c2",cursor="hand2 red",border=0,font=("courier 12 italic bold"),fg="indigo",command = subdomainSave).place(x=360,y=540)
    l1=Label(toolWindow,image = add1picresize3,fg="#e0556a",height=105,width=105,bg="#c3c3c2").place(x=370,y=430)




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-------------Hidden Directories----------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@################
    def hidDir():
        toolName['text']='Hidden Directories'
        toolName['fg']="Yellow"
        opText['highlightbackground'] = 'orange'
        opText['highlightthickness'] = 2
        command_argv1="python hiddenDir.py "+website
        os.system(command_argv1)

    hiddirpic1 = Image.open('hidDir.png')
    hiddirpic2 = hiddirpic1.resize((75,75))
    hiddirpic = ImageTk.PhotoImage(hiddirpic2)
    
    p1=Button(toolWindow,text="Hidden Directories",width=18,bg="#c3c3c2",cursor="hand2 red",border=0,font=("courier 12 italic bold"),fg="blue",command = hidDir).place(x=10,y=710)
    l1=Label(toolWindow,image = hiddirpic,fg="#e0556a",height=105,width=105,bg="#c3c3c2").place(x=50,y=610)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-------------SUB-Domains----------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@################
    
    def subDom():
        pass

    subDompic1 = Image.open('subdomain.png')
    subDompic2 = subDompic1.resize((75,75))
    subDompic = ImageTk.PhotoImage(subDompic2)
    
    p1=Button(toolWindow,text="Resolved SubDo",width=18,bg="#c3c3c2",cursor="hand2 red",border=0,font=("courier 12 italic bold"),fg="blue",command = subDom).place(x=200,y=710)
    l1=Label(toolWindow,image = subDompic,fg="#e0556a",height=105,width=105,bg="#c3c3c2").place(x=250,y=610)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@------------API KEY----------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@################
    
    def setApi():
        pass

    apipic1 = Image.open('webdomain.png')
    apipic2 = apipic1.resize((75,75))
    apipic = ImageTk.PhotoImage(apipic2)
    
    p1=Button(toolWindow,text="SET API Key",width=18,bg="#c3c3c2",cursor="hand2 red",border=0,font=("courier 12 italic bold"),fg="blue",command = setApi).place(x=390,y=710)
    l1=Label(toolWindow,image = apipic,fg="#e0556a",height=105,width=105,bg="#c3c3c2").place(x=440,y=610)
    
    toolWindow.mainloop()

    

#label = tk.Label(root,text='Enter Website Address:',fg='blue',font=("Courier", 20, "italic","bold")).place(x=850,y=150)
inp = Entry(root,textvariable=iptext,width=42,border=0,font=("calibre",18,"normal"),fg='#ec81fc',bg="black" )
inp.place(x=750,y=200)
inp.insert(END,"Enter Website Address")
inp.bind('<FocusIn>',onEnter2)
inp.bind('<FocusOut>',onLeave2)
#inp.focus_force()
tk.Frame(root,width=550,height=2,bg="#42ecf5").place(x=750,y=225)
btn =tk.Button(root,text='Submit',bg="blue",fg="white",font=("Arial",16,"bold","italic"),width=15,command=tools).place(x=920,y=280)    #,command = lambda:askyesno("Let's Go","Let's find the results")
#tk.Entry(root,textvariable=ip1).place(x=950,y=350)





#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@------------------------------------------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@################

#footFrame = tk.Frame(root,width=620,height=150,border=5,bg="white").place(x=720,y=530)
def devTeam():
    devWindow = tk.Toplevel(root)
    devWindow.geometry("1125x600")
    devWindow.title("Developer Team")
    devWindow.config(bg="yellow")
    devWindow.resizable(False, False)

    
    mampic1 = Image.open('madam.png')
    mampic2 = mampic1.resize((200,200))
    mampic = ImageTk.PhotoImage(mampic2)
    Button(devWindow,text="Mrs.Krishna Priya",width=18,bg="white",border=0,cursor='hand2',command = None,font=("courier 13 italic bold"),fg="black").place(x=450,y=50)
    labelmam = tk.Button(devWindow,image=mampic,fg="#e0556a",height=130,width=130,bg="black").place(x=200,y=50)

    
    jaggupic1 = Image.open('jaggu.png')
    jaggupic2 = jaggupic1.resize((150,150))
    jaggupic = ImageTk.PhotoImage(jaggupic2)
    Button(devWindow,text="Monangi Jagadeesh",width=18,bg="white",border=0,cursor='hand2',command = None,font=("courier 13 italic bold"),fg="black").place(x=10,y=400)
    labeljaggu = tk.Button(devWindow,image=jaggupic,fg="#e0556a",height=105,width=105,bg="black").place(x=50,y=270)
    label0 = Label(devWindow,text='N170985',width=18,bg='white',border=0,font=("courier 13 italic bold"),fg="black").place(x=10,y=440)

    sripic1 = Image.open('sri.png')
    sripic2 = sripic1.resize((150,150))
    sripic = ImageTk.PhotoImage(sripic2)
    Button(devWindow,text="Lambani Srikanth",width=18,bg="white",border=0,cursor='hand2',command = None,font=("courier 13 italic bold"),fg="black").place(x=250,y=400)
    labelsri = tk.Button(devWindow,image=sripic,fg="#e0556a",height=105,width=105,bg="black").place(x=290,y=270)
    label3 = Label(devWindow,text='N170874',width=18,bg='white',border=0,font=("courier 13 italic bold"),fg="black").place(x=250,y=440)

    ragpic1 = Image.open('rag.png')
    ragpic2 = ragpic1.resize((150,150))
    ragpic = ImageTk.PhotoImage(ragpic2)
    Button(devWindow,text="Billa Raghava",width=18,bg="white",border=0,cursor='hand2',command = None,font=("courier 13 italic bold"),fg="black").place(x=470,y=400)
    labelrag = tk.Button(devWindow,image=ragpic,fg="#e0556a",height=105,width=105,bg="black").place(x=510,y=270)
    label2 = Label(devWindow,text='N171080',width=18,bg='white',border=0,font=("courier 13 italic bold"),fg="black").place(x=470,y=440)

    lakhpic1 = Image.open('lakh.png')
    lakhpic2 = lakhpic1.resize((150,150))
    lakhpic = ImageTk.PhotoImage(lakhpic2)
    Button(devWindow,text="Karnam Lakshmi",width=18,bg="white",border=0,cursor='hand2',command = None,font=("courier 13 italic bold"),fg="black").place(x=690,y=400)
    labellakh = tk.Button(devWindow,image=lakhpic,fg="#e0556a",height=105,width=105,bg="black").place(x=730,y=270)
    label1 = Label(devWindow,text='N170___',width=18,bg='white',border=0,font=("courier 13 italic bold"),fg="black").place(x=690,y=440)
    

    likhpic1 = Image.open('likh.png')
    likhpic2 = likhpic1.resize((150,150))
    likhpic = ImageTk.PhotoImage(likhpic2)
    Button(devWindow,text="Bunga Likitha",width=18,bg="white",border=0,cursor='hand2',command = None,font=("courier 13 italic bold"),fg="black").place(x=910,y=400)
    labellikh = tk.Button(devWindow,image=likhpic,fg="#e0556a",height=105,width=105,bg="black").place(x=950,y=270)
    label5 = Label(devWindow,text='N170___',width=18,bg='white',border=0,font=("courier 13 italic bold"),fg="black").place(x=910,y=440)





    
    devWindow.mainloop()
devpic = Image.open("team.png")
devresize = devpic.resize((90,90))
devpic1 = ImageTk.PhotoImage(devresize)
tk.Button(root,text="Team",width=9,bg="black",border=0,cursor='hand2',command = devTeam,font=("courier 13 italic bold"),fg="blue").place(x=850,y=663)
labeldev = tk.Label(root,image=devpic1,fg="#e0556a",height=105,width=105,bg="black").place(x=850,y=550)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@------------------------------------------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#################

def about():
    aboutWindow = tk.Toplevel(root)
    aboutWindow.geometry("1000x600")
    aboutWindow.title("About")
    aboutWindow.config(bg="#ec81fc")
    aboutWindow.resizable(False, False)

    def domain():
        if textInfo == None:
            pass
        else:
            textInfo.delete(1.0,END)
        file = open('doc\dns.txt','r' , encoding="utf-8")
        lines = file.read()
        lines = lines.split('\n')
        for i in lines:
            textInfo.insert(END,i+'\n')
    def portsDoc():
        if textInfo == None:
            pass
        else:
            textInfo.delete(1.0,END)
        file = open('doc\Ports.txt','r' , encoding="cp1252")
        lines = file.read()
        lines = lines.split('\n')
        for i in lines:
            textInfo.insert(END,i+'\n')
    def subdoDoc():
        if textInfo == None:
            pass
        else:
            textInfo.delete(1.0,END)
        file = open('doc\subd.txt','r' , encoding='cp1252')
        lines = file.read()
        lines = lines.split('\n')
        for i in lines:
            textInfo.insert(END,i+'\n')
    def whoisDoc():
        if textInfo == None:
            pass
        else:
            textInfo.delete(1.0,END)
        file = open('doc\who is.txt','r' , encoding="cp1252")
        lines = file.read()
        lines = lines.split('\n')
        for i in lines:
            textInfo.insert(END,i+'\n')
    
    mainmenu = Menu(aboutWindow)
    aboutWindow.config(menu=mainmenu)
    textInfo = Text(aboutWindow,width=135,height=40,font=('Arial 9 bold'),wrap='word')
    textInfo.place(x=20,y=20)
    file = open('doc\header.txt','r')
    lines = file.read()
    lines = lines.split('\n')
    for i in lines:
        textInfo.insert(END,i+'\n')
    file = Menu(mainmenu , tearoff=0)
    mainmenu.add_cascade(label="Main",menu = file)
    file.add_command(label='DNS',command=domain)
    file.add_command(label='OpenPorts',command=portsDoc)
    file.add_command(label='Sub-Domain',command=subdoDoc)
    file.add_command(label='WhoIs LookUp?',command=whoisDoc)
    file.add_separator()
    file.add_command(label='GUI',command=None)
    dns = Menu(mainmenu , tearoff=0)
    mainmenu.add_cascade(label='DNS',menu=dns)
    dns.add_command(label='DNS',command=domain)
    dns.add_command(label='Domain',command=None)
    dns.add_command(label='Sub-Domain',command=subdoDoc)
    ports = Menu(mainmenu , tearoff=0)
    mainmenu.add_cascade(label='openPorts',menu=ports)
    ports.add_command(label='Ports',command=portsDoc)
    whois = Menu(mainmenu , tearoff=0)
    mainmenu.add_cascade(label='WhoIs?',menu=whois)
    whois.add_command(label='WhoIs LookUp?',command=whoisDoc)
    gui = Menu(mainmenu , tearoff=0)
    mainmenu.add_cascade(label='GUI',menu=gui)
    gui.add_command(label='What is Tkinter?',command=None)



    
    aboutWindow.mainloop()
    
devpic2 = Image.open("info.png")
devresize1 = devpic2.resize((75,75))
devpic3 = ImageTk.PhotoImage(devresize1)
tk.Button(root,text="APP-Info",width=9,bg="black",border=0,cursor='hand2',command =about,font=("courier 12 italic bold"),fg="blue").place(x=1055,y=663)
tk.Label(root,image=devpic3,fg="#e0556a",height=105,width=105,bg="black").place(x=1050,y=550)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@------------------------------------------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@################























root.mainloop()
