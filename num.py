import threading
import requests
def cut(mylist,part):
    for i in range(0,len(mylist),part):
        yield mylist[i:i+part]
f=open("wordlist.txt",'r')
r=f.read()
l=r.split("\n")
print(len(l))
part=len(l)//20
def fun(li):
    try:
        for i in li:
            url="https://www.google.com/"
            r=requests.get(url+i)
            print(f"{url+i}-->[{len(r.content)} {r.status_code}]")
    except:
        print("n")
        
z=cut(l,part)
s=0
threads=[]
for i in z:
    threads.append(threading.Thread(target=fun,args=(i,)))
print(threads)
for i in threads:
    i.start()
