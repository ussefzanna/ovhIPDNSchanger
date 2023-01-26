# Programa utilizado para cambiar el dyndns en OVH con el usuario y password del subdominio sub.domain.es
# https://www.ovh.com/nic/update?system=dyndns&hostname=$HOSTNAME&myip=$IP (ejemplo de ovh.com)
# De uso personal.
# Programa By UssefZanna, Welcome to zanna.es

from funciones import _getPublicIP, _changeIPDNS, _writelog

# Recupera la IP Publica.
IP = _getPublicIP()

# Solicita el cambio de la IP para el subdominio DynDNS.
respuesta = _changeIPDNS(IP)

# Esta funcion se utiliza para escribir los avisos en el ovhDNS.log.
_writelog(IP,respuesta)