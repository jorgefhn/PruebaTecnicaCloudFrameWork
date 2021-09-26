import requests, json, random

class API():

    def __init__(self): 
        
        self.registered = {} #diccionario con usuarios registrados
        

    #método get: comprobación del usuario registrado (identificado por el correo)
    def get(self,url:str,email:str):
        try:
            token = self.registered[email]['token'] #buscamos token añadido
            headers = { 'X-WEB-KEY': 'Test2021', 
                    'X-DS-TOKEN' : token }
           
            response = requests.get(url)
            response.status_code = 200
                    
            return("Status code: 200\n"+str({"success": True}))

        except: #el token solicitado no es correcto / no se ha encontrado
            
            return("Error 401:\n" +str({"success": False}))
                




    #método post: registro del usuario
    def post(self,url:str,name:str,surname:str,email:str,phone:str):
        #comprobamos que el token no esté en la lista (token debe ser un id único)
        try:  
            tok = self.registered[email] #comprobamos si el usuario está registrado. Si ya lo está, sigue el flujo del programa (error)
            return ("Error 401:\n"+str({'success' : False}))#error: usuario ya registrado

        except: 
            #identificaremos al usuario por su correo electrónico
            token = random.randint(10000,99999)#generamos token
            self.registered[email] = {'name' : name, 'surname': surname, 
                                    'email' : email, 'phone' : phone, 'token': token}
            headers = { 'X-WEB-KEY': 'Test2021' }
            
            response = requests.post(url, data=json.dumps(self.registered), headers=headers) #utilizamos método post
            response.status_code = 201 #actualizamos código 
            return("Status code: 201\n"+str({ 'success': True, 'data': {'token': token}}))


    


