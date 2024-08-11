  var socket = io();

        document.getElementById('chat-form').onsubmit = function(e) {
            e.preventDefault();
            var nombre = document.getElementById('nombre').value;
            var mensaje = document.getElementById('nuevo_mensaje').value;
            socket.emit('mensaje', {nombre: nombre, mensaje: mensaje});
            document.getElementById('nuevo_mensaje').value = '';
        };

        socket.on('actualizar_mensaje', function(data) {
            var chatMessages = document.getElementById('chat-messages');
            var messageElement = document.createElement('p');
            messageElement.textContent = data.nombre + ': ' + data.mensaje;
            chatMessages.appendChild(messageElement);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        });