class personas:

    #declaramos el constructor con los atributos
    def __init__(self, nombre, altura, peso, email):
        self.nombre = nombre
        self.altura = altura
        self.peso = peso
        self.email = email
    

    #declaramos el metodo imprimir el cual genera una salida en pantalla con todos los datos enviados por el objeto
    def imprimir(self):
        print(f'el nombre {self.nombre} altura {self.altura} peso {self.peso} email {self.email}')
    
#creamos el objpersona e intanciamos la clase personas
#le pasamos los valores de los atriutos
objpersona = personas("pablo", "1.70", 65, "pabloestebancd@gmail.com" )

#invocamos el metodo imprimir para generar unha salida en pantalla de los atriutos declarados
objpersona.imprimir()

#crear una clase ya sea con una lista/diccionario con 10 personas con nombre apellido edad telefono y crear una funcion random que
#selecione que casa a la de grifindor o slytherin van a ir (todos los datos deben ser ingresados, no puede haber datos guarados)

