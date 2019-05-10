import os

x = [1701231, 
     1701569,
     1704306,
     1704126,
     1739730,
     1722765,
     1739744,
     1723824,
     1739771,
     1726069,
     1726094,
]

pxy = ""#"-x 127.0.0.1:1087"

c1 = "curl 'https://m.titi002.com/pages/?inviter={0}' -H 'Connection: keep-alive' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' -H 'AlexaToolbar-ALX_NS_PH: AlexaToolbar/alx-4.0.3' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6' -H 'Cookie: ciu_key=b04a76ca-8c94-4bed-a981-4ea8ca427d0e$103.206.188.68; inviteriid={0}; JSESSIONID=gda29sclwzrk1m7sfcrxvhaf8' --compressed {1}"


c2 = "curl 'https://m.titi002.com/query/lovs?types=SHARE_DES%2CSEARCH_DEFAULT%2CBOOK_TAGS%2CCUSTOMER_SERVICE%2CMOBILE_AMOUNT_DESC%2CANDROID_APP' -H 'Pragma: no-cache' -H 'AlexaToolbar-ALX_NS_PH: AlexaToolbar/alx-4.0.3' -H 'Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6' -H 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1' -H 'Accept: */*' -H 'Referer: https://m.titi002.com/pages/?inviter={0}' -H 'Accept-Encoding: gzip, deflate, br' -H 'Cookie: ciu_key=b04a76ca-8c94-4bed-a981-4ea8ca427d0e$103.206.188.68; inviteriid={0}; JSESSIONID=gda29sclwzrk1m7sfcrxvhaf8' -H 'Connection: keep-alive' -H 'Cache-Control: no-cache' --compressed {1}"


c3 = "curl 'https://m.titi002.com/user/detail?ticket=' -H 'Pragma: no-cache' -H 'Origin: https://m.titi002.com' -H 'AlexaToolbar-ALX_NS_PH: AlexaToolbar/alx-4.0.3' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6' -H 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1' -H 'Content-Type: text/plain;charset=UTF-8' -H 'Accept: */*' -H 'Cache-Control: no-cache' -H 'Referer: https://m.titi002.com/pages/?inviter={0}' -H 'Cookie: ciu_key=b04a76ca-8c94-4bed-a981-4ea8ca427d0e$103.206.188.68; inviteriid={0}; JSESSIONID=gda29sclwzrk1m7sfcrxvhaf8' -H 'Connection: keep-alive' --data-binary 'ticket=' --compressed {1}"


c4 = "curl 'https://m.titi002.com/query/books?filter=competitive&type=cartoon&paged=true&size=6&page=1' -H 'Pragma: no-cache' -H 'Origin: https://m.titi002.com' -H 'AlexaToolbar-ALX_NS_PH: AlexaToolbar/alx-4.0.3' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6' -H 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1' -H 'Content-Type: text/plain;charset=UTF-8' -H 'Accept: */*' -H 'Cache-Control: no-cache' -H 'Referer: https://m.titi002.com/pages/?inviter={0}' -H 'Cookie: ciu_key=b04a76ca-8c94-4bed-a981-4ea8ca427d0e$103.206.188.68; inviteriid={0}; JSESSIONID=gda29sclwzrk1m7sfcrxvhaf8' -H 'Connection: keep-alive' --data-binary 'filter=competitive&type=cartoon&paged=true&size=6&page=1' --compressed {1}"


for n in x:
    os.system(c1.format(n, pxy))
    os.system(c2.format(n, pxy))
    os.system(c3.format(n, pxy))
    os.system(c4.format(n, pxy))
    print(n)
    print('-------------')




