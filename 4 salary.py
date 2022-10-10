hra = 100
ta = 100
da = 100
profittax = 100
pf = 100
insurance = 100

p1 = int(input("Enter basic salary: "))
def allowances():
  
    global allowance
   
    allowance = hra*(.22*p1) + da*(.18*p1) + ta*(.10*p1)
    print("allowance",allowance)


def deductions():
    global deduction
    if p1 > 8000:
      temp = 200

    else:
          temp = 150

    deduction = profittax*temp + pf*(.12*p1) + insurance*(.12*p1)
    print("deduction",deduction)


def salary():

    gs = p1 + allowance
    ns = gs - deduction
    print("Gross salary",gs , "Net salary",ns)

