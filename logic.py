def data(age,amount):
    amount = 0
    monthyly_savings = 10000

# def InvestmentAmount(age, amount):
    # if (18<age<30):
    #     amount = 0.7*monthyly_savings
    # elif (31<age<50):
    #     amount = 0.5*monthyly_savings
    # elif (51<age<60):
    #     amount = 0.4*monthyly_savings
    # else:
    #     amount = 0.3* monthyly_savings

# def AreaOfInvestment(age, amount):
    if (18<age<30):
        t = { 'MF':'Small and Flexi Cap',
        'Bonds':'Infrastrucure(PPP)',
        'Gold':'Digital Gold',
        'Equity':'Small Cap',
        'Crypto':'AltCoins'}        
    elif (31<age<50):
        t = { 'MF':'Mid and Flexi Cap',
        'Bonds':'Infrastrucure(PPP)',
        'Gold':'Digital Gold',
        'Equity':'Small Cap',
        'Crypto':'StableCoins'}
    elif (51<age<60):
        t = { 'MF':'Large and Flexi Cap',
        'Bonds':'Govt.',
        'Gold':'Physical Gold',
        'Equity':'Mid Cap',
        'Crypto':'    -     '}
    else:
        t = { 'MF':'Small and Flexi Cap',
        'Bonds':'Infrastrucure(PPP)',
        'Gold':'Digital Gold',
        'Equity':'Small Cap',
        'Crypto':'AltCoins'}
    return t
    
