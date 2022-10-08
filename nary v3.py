def run():
    try: a = int(input('starting base '))
    except: print('invalid input'); quit()
    try: b = int(input('ending base '))
    except: print('invalid input'); quit()
    try: n = int(input('number '))
    except: print('invalid input'); quit()

    d='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    def conv(a,b,n):
        v = 0; p = 1; s = []
        for i in str(n)[::-1]: v += d.index(i)*p; p *= a
        while v: s.append(d[v%b]); v//=b
        return ''.join(s[::-1])

    print(conv(a, b, n)); return

again = ''
while not (again == 'n' or again == 'no'):
    run()
    again = input('again?').lower()
