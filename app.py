from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")













# correo = "foo@foo.com"
# nombre= "foozi"
# edad = 40
# edad=edad+1
# edad=edad+1

# correos = ["foo@foo.com", "x@foo.com","y@foo.com"]

#             0             1             3
#            -3            -2            -1




#correos.append("zoo@zoo.com") #agregar

#correos.insert(0,"zoo@zoo.com") #insertar al inicio

# del correos[0] #eliminar al inicio

#correos.pop(0) #eliminar al inicio

#correos.remove("foo@foo.com") #eliminar al inicio



#r=correos.pop(0) #eliminar al inicio

#print (r)


#slice [inicio:final]

#print (correos [-1])

#correo_mayuscula=correo.upper()
#comentario
#print(correo, 
      #nombre,
      #correos[0],
     #edad,correo_mayuscula)
     
     
#print (correos)