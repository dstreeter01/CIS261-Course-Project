#Dwayne Streeter
#CIS261
# Course Project Phase 1: Create and Call Functions with Parmeters (2nd Code)

def i(p, f=0): return float(input(p)) if f else input(p)
def c(h, r, t):
    g = h * r
    x = g * t / 100
    return g, x, g - x

    e = 0 # e = total employees
    th = 0 # th = total hr worked
    tg = 0 # tg = total gross 
    tt = 0 # tt = total tax
    tn = 0 # tn = total net

    while 1:
        n = i("Name (or End): ")
        if n.lower() == "end": break
        h = i("Hours: ", 1)
        r = i("Rate: ", 1)
        t = i("Tax%: ", 1)
        g, x, net = c(h, r, t)

        #Display Employee Final Summary
    print(f"\n{n} | Hours: {h} | Rate: ${r:.2f} | Gross: ${g:.2f} | Tax: ${x:.2f} | Net: ${net:.2f}\n")

    #Totals
    e +=1; th +=h; tg +=g; tt +=x; tn +=net

#Final Summray of Totals
    print(f"\nTotal Employees: {e}  | Hours: {th} | Gross: ${tg:.2f} | Tax: ${tt:.2f} | Net: ${tn:.2f}")

#i = input function, # c = calculate payroll, #f=1 is expect float , g= gross, x=income tax , e = total employees

