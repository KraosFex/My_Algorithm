import urllib3
resp = urllib3.request("GET", "https://httpbin.org/robots.txt")
print(f"[+] El estado de la respuesta es {resp.status}")
print(resp.data)
