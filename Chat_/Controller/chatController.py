from flask import render_template, request, Blueprint, session
from flask_socketio import emit
from Chat_ import socketio

from flask import render_template, request, Blueprint,session


chat_bp = Blueprint('chat', __name__, url_prefix='/')

mensajes = []


@chat_bp.route('/', methods=['GET', 'POST'])
def chat_live():
    if request.method == 'POST':
        nombre = request.form.get('nombre')

        nuevo_mensaje = request.form.get('nuevo_mensaje')
        if nombre and nuevo_mensaje:
            session['nombre'] = nombre
            mensaje_formateado = f'{nombre}: {nuevo_mensaje}'
            mensajes.append(mensaje_formateado)
            # Emitir el mensaje a todos los clientes
            socketio.emit('actualizar_mensaje', {'nombre': nombre, 'mensaje': nuevo_mensaje}, broadcast=True)
    return render_template('chat.html', mensajes=mensajes, nombre=session.get('nombre'))


@socketio.on('mensaje')
def manejar_mensaje(data):
    nombre = data['nombre']
    nuevo_mensaje = data['mensaje']
    mensaje_formateado = f'{nombre}: {nuevo_mensaje}'
    mensajes.append(mensaje_formateado)
    emit('actualizar_mensaje', {'nombre': nombre, 'mensaje': nuevo_mensaje}, broadcast=True)


        nuevo_mensaje = request.form.get('nuevo_mensaje')
        if nombre and nuevo_mensaje:
            session['nombre']=nombre

            mensaje_formateado = f'{nombre}:{nuevo_mensaje}'
            mensajes.append(mensaje_formateado)
    return render_template('chat.html', mensajes=mensajes,nombre=session.get('nombre'))

