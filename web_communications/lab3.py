import urllib3


http = urllib3.PoolManager()
r = http.request("GET","http://wp.pl")

print("status: ", r.status)
print(r.data.decode("UTF-8"))



