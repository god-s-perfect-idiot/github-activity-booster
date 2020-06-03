import random
from essential_generators import DocumentGenerator

def gen():
    con = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','x']
    vow = ['a','e','i','o','u']

    lent = random.randint(3,7)

    wd = ""

    for i in range(lent):

        if(i%2==0):
            cr = random.randint(0,20)
            wd += con[cr]
        else:
            chance = random.randint(1,10)
            if(chance==1):
                cr = random.randint(0,20)
                wd += con[cr]
            else:
                cv = random.randint(0,4)
                wd += vow[cv]

    return wd

def gen_file():

        g = DocumentGenerator()
        content = g.paragraph()
        a = ['py','java','c','cs','js','sh']
        s = random.randint(0,5)
        c = gen()
        name = c+"."+a[s]
        with open(name,'w') as f:
            f.write(content)

        return name
