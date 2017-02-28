def processfile():
    drugitem=[]
    fr=open('spider_drugbank.txt','r')
    for line in fr.readlines():
        linearr=line.strip().split('\t\t')
        if(linearr[3]=='<span class=\'wishart wishart-not-available\'>Not Available</span>'):
            linearr[3]='null'
        drugitem.append(linearr)
    fr=open('spider_drugbank.txt','w')
    for drugArr in drugitem:
        inputstr=drugArr[0]
        for i in range(1,len(drugArr)):
            inputstr=inputstr+'\t\t'+drugArr[i]
        fr.write(inputstr+'\n')
    fr.close()
    return
