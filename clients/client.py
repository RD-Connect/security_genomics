import requests
service='http://localhost:8081'
rep = requests.post("http://10.3.231.71:8080/cas/v1/tickets",data="username=jleleu&password=jleleu&service=prova")
location=rep.headers.get('location')
tgt = location[location.rfind('/') + 1:]

params = urllib.urlencode({'service': service })
respo = requests.post("http://10.3.231.71:8080/cas/v1/tickets/"+tgt,data=urllib.urlencode({'service': service }))
rep = requests.post("http://10.3.231.71:8080/cas/login",data="username=jleleu&password=jleleu&service=http://10.3.231.71:8080/securestaff")
