# test-django-autocomplete_bug
Autocomplete_fields in django with custom monthfield not working

Pasos para reproducir el problema:
1. Ejecutar el servidor con python manage.py runserver 0.0.0.0:8000
2. Ingresar en 127.0.0.1:8000/admin
3. Ingresar a agregar un registro en Bug_movimientos.

Explicación del problema:

Al utilizar el widget personalizado monthfield el campo autocompletar deja de funcionar.
Se puede observar en la tabla Movimientos como sin el campo personalizado el autocompletar funciona normalmente.