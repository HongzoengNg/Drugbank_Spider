import urllib
import urllib2
import re
page=1
drugItemList=[]
pattern = re.compile('<div class="hit-name"><a href="(.*?)">.*?</a></div>',re.S)
subpattern=re.compile('<tr><th>Name</th><td><strong>(.*?)</strong>.*?</td></tr>'+
                               '<tr><th>Accession Number</th><td><strong>(.*?)</strong>.*?</td></tr>'+
                               '<tr><th>Type</th><td>(.*?)</td></tr>.*?'+
                               '<tr><th>CAS number</th><td>(.*?)</td></tr>',re.S)
uniprots_pattern=re.compile('<a target="_blank" class="wishart-link-out" href="http://www.uniprot.org/uniprot/.*?">(.*?)<span class="glyphicon glyphicon-new-window">.*?</span></a>',re.S)
while page<=52:
    url='https://www.drugbank.ca/unearth/q?approved=1&button=&c=_score&d=down&filter=true&page='+str(page)+'&query=diabetes+mellitus%2Ctype+2&searcher=drugs&us=1&vet_approved=1'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    headers = { 'User-Agent' : user_agent }
    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request)
    content=response.read().decode('utf-8')
    items = re.findall(pattern,content)
    for item in items:
        drugArr=[]
        itemtt='https://www.drugbank.ca'+item
        url2=itemtt
        request1=urllib2.Request(url2,headers=headers)
        response1=urllib2.urlopen(request1)
        subcontent=response1.read().decode('utf-8')
        drugAttr=re.findall(subpattern,subcontent)
        for i in drugAttr[0]:
            drugArr.append(i)
        uniprotsArr=re.findall(uniprots_pattern,subcontent)
        if uniprotsArr is not None:
            for i in uniprotsArr:
                drugArr.append(i)
        else:
            drugArr.append('null')
        print drugArr
        drugItemList.append(drugArr)
    page+=1
fr=open('spider_drugbank.txt','w')
for drugArr in drugItemList:
    inputstr=drugArr[0]
    for i in range(1,len(drugArr)):
        inputstr=inputstr+'\t\t'+drugArr[i]
    fr.write(inputstr+'\n')
fr.close()
