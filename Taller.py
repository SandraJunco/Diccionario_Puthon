
grupo_estudiantes = [
    
    {
    'nombre': 'Alejandro',
    'apellido': 'García',
    'promedio': 3.78,
    'nivel_programación': 2,
    'edad': 21,
    'estado_civil': 'Soltera',
    },

    {
    'nombre': 'Juan',
    'apellido': 'Rivera',
    'promedio': 3.4,
    'nivel_programación': 3,
    'edad': 21,
    'estado_civil': 'Soltera',
    },

    {
    'nombre': 'Brayan',
    'apellido': 'Ortiz',
    'promedio': 3.09,
    'nivel_programación': 2,
    'edad': 20,
    'estado_civil': 'Soltera',
    },

    {
    'nombre': 'Jhon',
    'apellido': 'Neva',
    'promedio': 3.5,
    'nivel_programación': 2,
    'edad': 20,
    'estado_civil': 'Soltera',
    },

    {
    'nombre': 'Luisa',
    'apellido': 'Bentacourt',
    'promedio': 3.5,
    'nivel_programación': 3,
    'edad': 19,
    'estado_civil': 'Soltera',
    },

    {
    'nombre': 'Linda',
    'apellido': 'Ramos',
    'promedio': 3.61,
    'nivel_programación': 2,
    'edad': 25,
    'estado_civil': 'En relación',
    },

    {
    'nombre': 'Maria',
    'apellido': 'Pardo',
    'promedio': 3.8,
    'nivel_programación': 2,
    'edad': 23,
    'estado_civil': 'En relación',
    },

    {
    'nombre': 'Diana',
    'apellido': 'Soto',
    'promedio': 3.6,
    'nivel_programación': 2,
    'edad': 20,
    'estado_civil': 'En relación',
    },

    {
    'nombre': 'Johan',
    'apellido': 'Galindo',
    'promedio': 3.38,
    'nivel_programación': 2,
    'edad': 22,
    'estado_civil': 'Soltera',
    },

    {
    'nombre': 'Angel',
    'apellido': 'Molano',
    'promedio': 3.6,
    'nivel_programación': 3,
    'edad': 24,
    'estado_civil': 'En relación',
    },

    {
    'nombre': 'Nikole',
    'apellido': 'Florez',
    'promedio': 4.19,
    'nivel_programación': 2.5,
    'edad': 21,
    'estado_civil': 'Soltera',
    },

    {
    'nombre': 'Andres',
    'apellido': 'Segura',
    'promedio': 4.1,
    'nivel_programación': 3,
    'edad': 24,
    'estado_civil': 'En relación',
    },

    {
    'nombre': 'Ruth',
    'apellido': 'Duran',
    'promedio': 4.0,
    'nivel_programación': 3,
    'edad': 22,
    'estado_civil': 'En relación',
    },
        
    {
    'nombre': 'Sandra',
    'apellido': 'Junco',
    'promedio': 4.4,
    'nivel_programación': 2,
    'edad': 23,
    'estado_civil': 'Soltera',
    }
]

# Promedio de edad de los estudiantes del curso.
suma_edad = 0
for estudiante in grupo_estudiantes:
    edad_estudiante = estudiante['edad']
    suma_edad = suma_edad + edad_estudiante
promedio_edad = suma_edad / len(grupo_estudiantes)
print(f"El promedio de edad de los estudiantes del curso corresponde a: {promedio_edad}")

# Número de estudiantes solteros del curso.
estudiantes_solteros = 0
for estudiante in grupo_estudiantes:
    if estudiante['estado_civil'] == 'Soltera':
        estudiantes_solteros = estudiantes_solteros + 1
print(f"El número de estudiantes solteros del curso es de: {estudiantes_solteros}")

# Estudiante con mayor promedio del curso.
mayor_promedio = grupo_estudiantes[0]
for estudiante in grupo_estudiantes:
    if estudiante['promedio'] > mayor_promedio['promedio']:
        mayor_promedio = estudiante
print(f"El estudiante con mayor promedio del curso es: {mayor_promedio['nombre']} {mayor_promedio['apellido']} cuyo promedio es de {mayor_promedio['promedio']}")

# Estudiante con menor nivel de programación en el curso.
menor_nivel_program=grupo_estudiantes[0]
for estudiate in grupo_estudiantes:
    if estudiante['nivel_programación']<menor_nivel_program['nivel_programación']:
        menor_nivel_program = estudiante
print(f"El estudiante con menor nivel de programación es: {menor_nivel_program['nombre']} {menor_nivel_program['nombre']} el cual corresponde a {menor_nivel_program['nivel_programación']}")
