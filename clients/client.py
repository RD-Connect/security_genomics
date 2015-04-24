import requests
import urllib
service='http://localhost:8081'
username="rdconnect-test"
password="1234.abcd"
rep = requests.post("http://10.3.231.71:8080/cas/v1/tickets",data="username="+username+"&password="+password+"&service=prova")
location=rep.headers.get('location')
tgt = location[location.rfind('/') + 1:]

params = urllib.urlencode({'service': service })
respo = requests.post("http://10.3.231.71:8080/cas/v1/tickets/"+tgt,data=urllib.urlencode({'service': service }))
st = respo.text
validate = requests.post("http://10.3.231.71:8080/cas/serviceValidate?ticket="+st+"&service="+service)

#rep = requests.post("http://10.3.231.71:8080/cas/login",data="username=jleleu&password=jleleu&service=http://10.3.231.71:8080/securestaff")


delete = requests.delete("http://10.3.231.71:8080/cas/v1/tickets/"+tgt)