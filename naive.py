import time

def NaiveAlgo(a):
    aa = time.clock()
    b = []
    d = []
    for i in range(10):
        for j in range(50):
            f = open('./dataset/' + str(i) + '_' + str(j) + '.txt', 'r')
            c = f.read().strip('[').strip(']').split(r',')
            ans = 0
            for k in range(2500):
                ans += (a[k] - int(c[k])) ** 2
            ans = ans ** 0.5
            d.append(ans)
    kk = max(d)
    return(time.clock() - aa)

