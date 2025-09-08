#Dwayne Streeter
#CIS261
#Course Project Phase 4

F="users.txt"
class L:
    def __init__(s,u,p,a): s.u,s.p,s.a=u,p,a
U=lambda: [l.strip().split("|") for l in open(F)] if __import__("os").path.exists(F) else []
A=lambda u,p,a: open(F,"a").write(f"{u}|{p}|{a}\n")
def add():
    ids=[x[0]for x in U()]
    while 1:
        u=input("User ID (or End): ");
        if u.lower()=="end": break
        if u in ids: print("Exists"); continue
        p=input("Password: "); a=input("Auth(Admin/User): ").title()
        if a not in ["Admin","User"]: print("Invalid"); continue
        A(u,p,a); ids.append(u); print("Added")
def disp():
    for u,p,a in U(): print(f"ID:{u} | PW:{p} | Auth:{a}")
def log():
    d={u:(p,a) for u,p,a in U()}; u=input("Login ID: ");
    if u not in d: print("No user"); return
    p=input("Password: ");
    if p!=d[u][0]: print("Wrong"); return
    return L(u,p,d[u][1])
def get(): return input("From mm/dd/yyyy:"),input("To mm/dd/yyyy:")
def calc(h,r,t): g=h*r; x=g*t/100; return g,x,g-x
def payroll():
    e,t=[],{"emp":0,"hrs":0,"gross":0,"tax":0,"net":0}
    while(n:=input("Name(or End):")).lower()!="end":
        fd,td=get();h=float(input("H:"));r=float(input("R:"));t1=float(input("T%:"))
        e.append((fd,td,n,h,r,t1))
    for fd,td,n,h,r,t1 in e:
        g,x,n1=calc(h,r,t1)
        print(f"{fd}--{td} | {n} | Hrs:{h} | Rate:${r:.2f} | Gross:${g:.2f} | Tax%:{t1}% | Tax:${x:.2f} | Net:${n1:.2f}")
        t["emp"]+=1;t["hrs"]+=h;t["gross"]+=g;t["tax"]+=x;t["net"]+=n1
    print(f"\nTotal Emp:{t['emp']} | Hrs:{t['hrs']} | Gross:${t['gross']:.2f} | Tax:${t['tax']:.2f} | Net:${t['net']:.2f}")
def main():
    if input("Add users? y/n:").lower()=="y": add();disp()
    u=log();
    if not u: return
    print(f"\nWelcome {u.u}({u.a})"); payroll()
if __name__=="__main__": main()

