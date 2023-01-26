from requests import get
from datos import _DMNAME, _Contrasena, _Usuario
import datetime

problemas = False

def _getPublicIP():
    try:
        IP = get("https://api.ipify.org").text
        print("IP actual: {}".format(IP))
    except:
        print("Error en la solicitud de IP Publica actual.")
        problemas = True
    return IP

def _changeIPDNS(IP):
    try:
        print("Solicitando el cambio de IP.")
        respuesta = get('https://www.ovh.com/nic/update?system=dyndns&hostname={}&myip={}'.format(_DMNAME,IP), auth=(_Usuario,_Contrasena)).text
        print("Respuesta: " + respuesta)
    except:
        print("Error en la solicitud para el cambio de IP.")
        problemas = True
    return respuesta

def _writelog(IP,respuesta):
    if problemas == True:
        simbolo = "(✘)"
    else:
        simbolo = "(✔)"

    try:
        reloj = datetime.datetime.now()
        with open("./.ovhDNS.log","a") as zlogs:
            zlogs.write("{}{}/{}/{} [{}:{}:{}] IP-Publica: {} -> Respuesta: {}\n".format(simbolo,reloj.day,reloj.month,reloj.year,reloj.hour,reloj.minute,reloj.second,IP,respuesta))
    except:
        print("Error en la solicitud para guardar los zlogs.")

