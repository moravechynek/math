def evaluate(latex):
    pyVyraz = priklad = latex
    i = 1
    # absolutní hodnota
    if pyVyraz.find('|'):
        while i <= priklad.count('|'):
            if i % 2 == 0:
                pyVyraz = pyVyraz.replace('|',')',1)
            elif i % 2 == 1:
                pyVyraz = pyVyraz.replace('|','abs(',1)
        i += 1
    i = 0

    # zlomky
    jmenovatel = ''
    citatel = ''
    position = priklad.find('\\frac{')
    if position != -1:
        while priklad[position + len('\\frac{') + i] != '}':
            jmenovatel += priklad[position + len('\\frac{')]
        i += 1
        i = 0
        while priklad[position + len('\\frac{' + jmenovatel + '}{') + i] != '}':
            citatel += priklad[position + len('\\frac{')]
            i += 1
        i = 0
        pyVyraz = pyVyraz.replace('\\frac{' + jmenovatel + '}{' + citatel + '}',str(int(jmenovatel)/int(citatel)))
    return pyVyraz