# Gestión de Cursos

Esta es una aplicación web de gestión de cursos creada con Flask y MySQL. Permite gestionar estudiantes, cursos e inscripciones.

## Requisitos

- Python 3.x
- MySQL
- Virtualenv (opcional pero recomendado)

## Instalación

1. *Clonar el repositorio:*


    - git clone (https://github.com/Dazaiyan/Gestion-Curso-Calidad-SW.git)
    - cd Gestion-Curso-Calidad-SW
    

2. *Crear un entorno virtual (opcional pero recomendado):*

    
    - python3 -m venv venv
    - source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    

3. *Instalar las dependencias:*

    
    - pip install flask
    - pip install flask-mysqldb
    
    

4. *Configurar la base de datos MySQL:*

    - Crear una base de datos llamada gestion_cursos.
    - Crear las siguientes tablas:
      
- SQL
   ```
    CREATE DATABASE gestion_cursos;

    USE gestion_cursos;

    CREATE TABLE Estudiantes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL
    );

    CREATE TABLE Cursos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL
    );

    CREATE TABLE Inscripciones (
        id INT AUTO_INCREMENT PRIMARY KEY,
        id_estudiante INT NOT NULL,
        id_curso INT NOT NULL,
        fecha_inscripcion DATE NOT NULL,
        FOREIGN KEY (id_estudiante) REFERENCES Estudiantes(id),
        FOREIGN KEY (id_curso) REFERENCES Cursos(id)
    );
    ```

6. *Configurar las credenciales de MySQL:*

    Editar el archivo app.py con tus credenciales de MySQL:
   
- python
    - app.config['MYSQL_HOST'] = 'localhost'
    - app.config['MYSQL_USER'] = 'root'
    - app.config['MYSQL_PASSWORD'] = 'TU_CONTRASEÑA'
    - app.config['MYSQL_DB'] = 'gestion_cursos'
    

## Ejecución

1. *Ejecutar la aplicación:*

    sh
    python app.py
    

2. *Abrir el navegador:*

    Visita http://localhost:5000 para ver la aplicación en funcionamiento.

## Estructura del Proyecto

- app.py: Archivo principal de la aplicación.
- templates/: Directorio que contiene las plantillas HTML.
  - index.html: Página principal que muestra los estudiantes.
  - cursos.html: Página que muestra los cursos.
  - inscripciones.html: Página que muestra las inscripciones.
  - edit_student.html: Formulario para editar estudiantes.
  - add_student.html: Formulario para añadir nuevos estudiantes.
  - edit_enrollment.html: Formulario para editar inscripciones.
  - add_enrollment.html: Formulario para añadir nuevas inscripciones.

## Uso

### Estudiantes

- *Añadir Estudiante:* Navegar a /add_student para añadir un nuevo estudiante.
- *Editar Estudiante:* Navegar a /edit_student/<id> para editar un estudiante existente.
- *Eliminar Estudiante:* Hacer clic en el botón de eliminar en la página principal.

### Cursos

- *Ver Cursos:* Navegar a /cursos para ver la lista de cursos.

### Inscripciones

- *Añadir Inscripción:* Navegar a /add_enrollment para añadir una nueva inscripción.
- *Editar Inscripción:* Navegar a /edit_enrollment/<id> para editar una inscripción existente.
- *Eliminar Inscripción:* Hacer clic en el botón de eliminar en la página de inscripciones.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, haz un fork del repositorio y envía un pull request con tus mejoras.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
