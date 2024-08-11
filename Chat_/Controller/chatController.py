from flask import render_template, request, Blueprint,session


chat_bp = Blueprint('chat', __name__, url_prefix='/')

mensajes = []


@chat_bp.route('/', methods=['GET', 'POST'])
def chat_live():
    if request.method == 'POST':
        nombre = request.form.get('nombre')

        nuevo_mensaje = request.form.get('nuevo_mensaje')
        if nombre and nuevo_mensaje:
            session['nombre']=nombre

            mensaje_formateado = f'{nombre}:{nuevo_mensaje}'
            mensajes.append(mensaje_formateado)
    return render_template('chat.html', mensajes=mensajes,nombre=session.get('nombre'))
