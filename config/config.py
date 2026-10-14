
import os

prefix = '/'

# Credenciales obtenidas desde variables de entorno
room = os.getenv('HIGHRISE_ROOM_ID', '').strip()
token = os.getenv('HIGHRISE_API_TOKEN', '').strip()

# Datos del bot
botID = '68654c84f77cce8a0c95eb1b'
botName = 'BotiNera'
ownerName = 'IamDakota'

coordinates = {
    'x': 0,
    'y': 0,
    'z': 0,
    'facing': 'FrontRight'
}

# Comprobar que las credenciales estén configuradas
if not room:
    raise RuntimeError(
        'Falta configurar la variable HIGHRISE_ROOM_ID.'
    )

if not token:
    raise RuntimeError(
        'Falta configurar la variable HIGHRISE_API_TOKEN.'
    )
