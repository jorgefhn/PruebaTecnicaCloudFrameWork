from api import API
#batería de pruebas

url = 'https://www.marca.com/' #ejemplo de página web
api = API()
#método post: registro del usuario, resultado: Status code: 201{ 'success': True, 'data': {'token': <valor del token>}}. Probamos dos casos.
print(api.post(url,'Jorge','Ferrer','jorgeferrerhernaez@gmail.com','652144892'))
print(api.post(url,'Carlos','García','carlosgarcia@gmail.com','689231094'))
#método get: comprobación del estado de registro del usuario, resultado: Status code: 200 {"success": True}
print(api.get(url,'jorgeferrerhernaez@gmail.com'))

#comprobamos caso de ya registrado, resultado esperado: Error 401: {'success' : False}
print(api.post(url,'Jorge','Ferrer','jorgeferrerhernaez@gmail.com','652144892'))
#comprobamos caso no válido (email no registrado)
print(api.get(url,'email2@gmail.com'))