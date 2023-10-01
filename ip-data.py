import requests
from termcolor import colored

decoracion = '''
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
ccccc;::::::::::::::::::::::::;:::::::::::;:::::::::::::;:,ccc
ccccc;ccccccccccc:ccccccccc:,:;,;:cccccccccccccccccccccccc,ccc
ccccc;ccccccc:ccccccccccc:'.      ...,:ccccccccccccccccccc,ccc
ccccc;cccccccccccccccccc'              .cccccccccccccccccc,ccc
ccccc;ccccccccccccccccc.                .:cccccccccccccccc,ccc
ccccc;cccccccccccccccc'                  .cccccccccccccccc,ccc
ccccc;cccccccc:ccccccc.                  .cccccccccccccccc,ccc
ccccc;cccccccc:ccccccc     .'.    .';.   'cccccccccccccccc,ccc
ccccc;cccccccccccccccc.   .;,'.   .';.   .cccccccccccccccc,ccc
ccccc,cccccccccccccccc'             ..   .cccccccc:ccccccc,ccc
ccccc;cccccccccccccccc.     .       .    'cccccccccccccccc,ccc
ccccc;ccccc:cccccccccc,     .           .ccccccccccccccccc,ccc
ccccc,ccccccccccccccccc:.   .       .  .cccccc:c:ccccccccc,ccc
ccccc;ccccccccccccccccccc.          . .:cccccccccccccccccc,ccc
ccccc,cc:ccccccccccccc;:.             .,,:cccccccc:;cccccc,ccc
ccccc;cccccccccccc:'.                     ..,:cccccccccccc,ccc
ccccc;cccc:cccccc,.                           .;cccccccccc,ccc
ccccc;cccc::ccc:.                              .,:cc:ccccc;ccc
ccccc;cccccccc'.                                 ':ccccccc,ccc
ccccc;ccccccc,.                                  .;ccccccc,ccc
ccccc;cccccc:                                     ,:cccccc:ccc
ccccc,cccccc.           MOHA√CR ⁅B᤻ᳱᮩᮢᮣZ⁆ᮢ⅌᪼ᩬ🇲🇦 ⃘⃕‌⃤         .;cccccc;ccc
ccccc,ccccc,                                       .:ccccc;ccc
ccccc,ccccc.              BY: @PREBOYX              .ccccc;ccc
ccccc;:::::.            TG: @BSZ_CRACKING            ;:::::ccc
cccccccccc:.                                         ,cccccccc
cccccccccc.                                          .cccccccc
cccccccccc.                                          'ccccccc
'''

print(colored(decoracion, "green"))


def obtener_informacion_ip(ip):
    url = f"https://ipapi.co/{ip}/json/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return f"Información de la IP {ip}:\n\n" \
               f"🌍 País: {data['country_name']}\n" \
               f"📍 Región: {data['region']}\n" \
               f"🏙️ Ciudad: {data['city']}\n" \
               f"📮 Código postal: {data['postal']}\n" \
               f"🌐 Latitud: {data['latitude']}\n" \
               f"🌐 Longitud: {data['longitude']}\n" \
               f"⏰ Zona horaria: {data['timezone']}\n" \
               f"🌐 Isp: {data['org']}\n" \
               f"📞 Código de llamada de país: {data['country_calling_code']}\n" \
               f"🗣️ Lenguaje: {data['languages']}\n"\
               f"🔢 Código ISO 3166-1 alfa-2: {data['country_code']}\n"\
               f"🔢 Código ISO 3166-1 alfa-3: {data['country_code_iso3']}"
    else:
        print(colored("No se pudo obtener información de la IP. Inténtalo de nuevo.", "red"))
        return None

while True:
    opcion = input(colored("Elige una opción:\n1. Buscar información sobre una dirección IP\n2. Salir del script\n", "green", attrs=["bold"]))
    
    if opcion == "1":
        ip = input(colored("Introduce una dirección IP:", "green", attrs=["bold"]))
        informacion_ip = obtener_informacion_ip(ip)
        
        if informacion_ip:
            print(informacion_ip)
    
    elif opcion == "2":
        break
    
    else:
        print(colored("Opción inválida. Por favor, elige una opción válida.", "red"))