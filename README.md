# ovhIPDNSchanger
Programa basico para cambiar las IP's de los sub-dominios vinculados a dynDNS de OVH.com.

Ejemplo: 
  Uso en raspberry pi con Ubuntu server ARM64.
  
  Añadir opcion en el crontab -e para que este lo ejecute cada 15 min:
  
    - */15 * * * * python3 /home/(usuario)/.scripts/ovhIPChanger/app.py >> /home/(usuario)/.zlog/crontab.log 2>&1
    
    
    Saludos pringaos.
    by ussefzanna.
