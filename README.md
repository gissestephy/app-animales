VETERINARIA

Crear un programa que le permita al usuario cargar los datos y ver los registros de una lista. Dicha lista sera “animales[ ]”

Solicitar al usuario que indique la cantidad de registros que desea. Indicar luego con un print que “Se van a insertar (numero ingresado por el usuario) animales”

• Crear el bucle para recorrer la cantidad ingresada y generar los registros. Se recomienda trabajar desde un FOR y que el registro esté representado por un DICCIONARIO. Campos de la tabla animales:

Especie (String) Ejemplo: Elefante. Población (El dato ingresado debe Integer). Este contendra un condicional que, segun el dato ingresado, si es menor a 10mil, mostrara “En vias de extincion”, Si es mayor o igual a 10mil “Fuera de peligro de extincion”, y si es cero “Extinto”. Ubicacion(String): puede ser pais o continente. Este bucle debe guardar los registros creados en la LISTA animales[ ] de manera ANIDADA (cada registro creado con especie,poblacion y ubicacion debe ser un diccionario dentro de la lista animales[ ])

• Incluir dentro de una funcion llamada CargaDeAnimales el codigo del punto 2. La funcion debe retornar la lista animales creada.

• Crear una funcion que me permita hacer una consulta a animales[ ] y traer todos los diccionarios que contiene e imprimir llave y valor. Si la lista esta vacia, mostrara “la lista esta vacia”. Consulta de animales debe actualizarse si decidimos ingresar mas registros

• Crear un condicional que dara inicio al programa dando la bienvenida preguntando que accion se va a realizar y mostrando las siguientes opciones: 1: Ingresar registro de animales (usar la funcion del punto 3) 2: consultar registro de animales cargados (usar funcion del punto 4) 3: salir del programa agradeciendo al usuario

Si ingresa otro numero, dira que la opcion elegida no es valida. Este condicional entrara en un bucle mientras que la opcion no sea salir.
