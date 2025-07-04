import requests

ip = requests.get('https://api.ipify.org').text
print(f"\n[+] Your Public IP: {ip}")

res = requests.get(f'http://ip-api.com/json/{ip}')
data = res.json()

lat = data['lat']
lon = data['lon']

print(f"""
[+] Country: {data['country']}
[+] Region: {data['regionName']}
[+] City: {data['city']}
[+] ZIP: {data['zip']}
[+] ISP: {data['isp']}
[+] Lat: {lat}
[+] Lon: {lon}
""")

print(f"[+] Google Maps Link: https://www.google.com/maps/search/?api=1&query={lat},{lon}")

print(f"\n[+] Static Location Data:")
print("District: Goalpara")
print("State: Assam")
print("Country: India")
print("PIN: 783129\n")
