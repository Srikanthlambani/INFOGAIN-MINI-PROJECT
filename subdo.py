import dns.resolver
import sys
import time
file1=open('names1.txt','r')
Lines=file1.read()
list1=Lines.split('\n')
#donnain=input("Enter the domain : ")
domain=sys.argv[1]
donnain='.'.join(domain.split('.')[1:])
print(donnain)
def main():
    subd=[]
    for subdon in list1:
            try:
                ip_value=dns.resolver.resolve(f'{subdon}.{donnain}','A')
                if ip_value:
                    subd.append(f'{subdon}.{donnain}')
                    if f"{subdon}.{donnain}" in subd:
                        print(f'{subdon}.{donnain}')
            except dns.resolver.NXDOMAIN:
                pass
            except dns.resolver.NoAnswer:
                pass
            except KeyboardInterrupt:
                quit()
main()
time.sleep(15)


