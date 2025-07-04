import requests

print("\n[+] RTN-IP-TRACKER | TRACK ANY IP LOCATION\n")

ip = input("[?] Enter the IP address to track: ")

try:
    res = requests.get(f'http://ip-api.com/json/{ip}')
    data = res.json()

    if data['status'] == 'success':
        lat = data['lat']
        lon = data['lon']

        print(f"""
[+] IP: {ip}
[+] Country: {data['country']}
[+] Region: {data['regionName']}
[+] City: {data['city']}
[+] ZIP: {data['zip']}
[+] ISP: {data['isp']}
[+] Lat: {lat}
[+] Lon: {lon}

[+] Google Maps Link:
https://www.google.com/maps/search/?api=1&query={lat},{lon}
""")
    else:
        print("[!] Invalid IP address or API limit reached. Try again later.")
except:
    print("[!] Something went wrong. Check your internet connection.")
