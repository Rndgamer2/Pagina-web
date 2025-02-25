from flask import Flask
import random

app = Flask(__name__)

def generar_contraseña(longitud=8):
    caracteres = "0123456789"
    return "".join(random.choice(caracteres) for _ in range(longitud))

contraseña = [generar_contraseña()]

facts_list = ["Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones",
"Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas",
"Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos",
"Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos"]

emojis = [":D (Sonrisa grande)",";) (Guiño)",":P (Sacando la lengua)",":O (Sorpresa)","^^ (Feliz o emocionado)",">:D (Risa malvada o traviesa)"
,"-_- (Indiferencia o cansancio)",":'( (Tristeza o llanto)","o_O (Sorpresa o confusión)","(^_^) (Felicidad o alegría)" ]



@app.route("/contraseña")
def password_random():
    return f'<p>{random.choices(contraseña)}</p>'

@app.route("/")
def hello_world():
    return f'<h1>Hello, esta es una pagina con datos interesantes!</h1> <a href="/random_fact">¡Ver un dato aleatorio!</a> <a href="/emoji">¡Ver un emoji aleatorio!</a> <a href="/contraseña">¡Ver una contraseña aleatoria!</a>'

@app.route("/random_fact")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/emoji")
def emoji_random():
    return f'<p>{random.choice(emojis)}</p>'

app.run(debug=True)