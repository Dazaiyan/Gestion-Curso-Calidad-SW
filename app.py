from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = '123456'

# Define los detalles del servidor MySQL, incluyendo host, usuario, contraseña y base de datos a utilizar.
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'gestion_cursos'

mysql = MySQL(app)

# Realiza una consulta a la base de datos para obtener los estudiantes y los muestra en `index.html`.
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM Estudiantes")
    if result_value > 0:
        students = cur.fetchall()
        return render_template('index.html', students=students)
    return render_template('index.html')

# Realiza una consulta a la base de datos para obtener los cursos y los muestra en `cursos.html`.
@app.route('/cursos')
def cursos():
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM Cursos")
    if result_value > 0:
        courses = cur.fetchall()
        return render_template('cursos.html', courses=courses)
    return render_template('cursos.html')

# Agregar Curso
@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        course_details = request.form
        nombre = course_details['nombre']
        descripcion = course_details['descripcion']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Cursos(nombre, descripcion) VALUES(%s, %s)", (nombre, descripcion))
        mysql.connection.commit()
        cur.close()
        flash('Curso Agregado Satisfactoriamente')
        return redirect(url_for('cursos'))
    return render_template('add_course.html')

# Editar curso
@app.route('/edit_course/<int:id>', methods=['GET', 'POST'])
def edit_course(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Cursos WHERE id = %s", [id])
    course = cur.fetchone()

    if request.method == 'POST':
        course_details = request.form
        nombre = course_details['nombre']
        descripcion = course_details['descripcion']

        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Cursos
            SET nombre = %s, descripcion = %s
            WHERE id = %s
        """, (nombre, descripcion, id))
        mysql.connection.commit()
        cur.close()
        flash('Curso Actualizado Satisfactoriamente')
        return redirect(url_for('cursos'))

    return render_template('edit_course.html', course=course)

# Eliminar curso
@app.route('/delete_course/<int:id>', methods=['POST'])
def delete_course(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Cursos WHERE id = %s", [id])
    mysql.connection.commit()
    cur.close()
    flash('Curso Eliminado Satisfactoriamente')
    return redirect(url_for('cursos'))

# Realiza una consulta a la base de datos para obtener las inscripciones y las muestra en `inscripciones.html`.
@app.route('/inscripciones')
def inscripciones():
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM Inscripciones")
    if result_value > 0:
        enrollments = cur.fetchall()
        return render_template('inscripciones.html', enrollments=enrollments)
    return render_template('inscripciones.html')

# Proporciona una interfaz para editar y actualizar la información de los estudiantes en la base de datos.
@app.route('/edit_student/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Estudiantes WHERE id = %s", [id])
    student = cur.fetchone()

    if request.method == 'POST':
        student_details = request.form
        nombre = student_details['nombre']
        email = student_details['email']

        cur.execute("""
            UPDATE Estudiantes
            SET nombre = %s, email = %s
            WHERE id = %s
        """, (nombre, email, id))
        mysql.connection.commit()
        cur.close()
        flash('Estudiante Actualizado Satisfactoriamente')
        return redirect(url_for('index'))

    return render_template('edit_student.html', student=student)

# Proporciona un formulario para ingresar los detalles de un nuevo estudiante y guardarlos en la base de datos.
@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student_details = request.form
        nombre = student_details['nombre']
        email = student_details['email']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Estudiantes(nombre, email) VALUES(%s, %s)", (nombre, email))
        mysql.connection.commit()
        cur.close()
        flash('Estudiante Agregado Satisfactoriamente')
        return redirect(url_for('index'))

    return render_template('add_student.html')

# Proporciona la funcionalidad para eliminar un estudiante de la base de datos mediante su ID.
@app.route('/delete_student/<int:id>', methods=['POST'])
def delete_student(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Estudiantes WHERE id = %s", [id])
    mysql.connection.commit()
    cur.close()
    flash('Estudiante Eliminado Satisfactoriamente')
    return redirect(url_for('index'))

# Proporciona un formulario para ingresar los detalles de una nueva inscripción y guardarlos en la base de datos.
@app.route('/add_enrollment', methods=['GET', 'POST'])
def add_enrollment():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, nombre FROM Estudiantes")
    students = cur.fetchall()
    cur.execute("SELECT id, nombre FROM Cursos")
    courses = cur.fetchall()

    if request.method == 'POST':
        enrollment_details = request.form
        id_estudiante = enrollment_details['id_estudiante']
        id_curso = enrollment_details['id_curso']
        fecha_inscripcion = enrollment_details['fecha_inscripcion']

        cur.execute("INSERT INTO Inscripciones(id_estudiante, id_curso, fecha_inscripcion) VALUES(%s, %s, %s)", 
                    (id_estudiante, id_curso, fecha_inscripcion))
        mysql.connection.commit()
        cur.close()
        flash('Inscripción Agregada Satisfactoriamente')
        return redirect(url_for('inscripciones'))

    return render_template('add_enrollment.html', students=students, courses=courses)

# Proporciona una interfaz para editar y actualizar la información de las inscripciones en la base de datos.
@app.route('/edit_enrollment/<int:id>', methods=['GET', 'POST'])
def edit_enrollment(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Inscripciones WHERE id = %s", [id])
    enrollment = cur.fetchone()

    cur.execute("SELECT id, nombre FROM Estudiantes")
    students = cur.fetchall()

    cur.execute("SELECT id, nombre FROM Cursos")
    courses = cur.fetchall()

    if request.method == 'POST':
        enrollment_details = request.form
        id_estudiante = enrollment_details['id_estudiante']
        id_curso = enrollment_details['id_curso']
        fecha_inscripcion = enrollment_details['fecha_inscripcion']

        cur.execute("""
            UPDATE Inscripciones
            SET id_estudiante = %s, id_curso = %s, fecha_inscripcion = %s
            WHERE id = %s
        """, (id_estudiante, id_curso, fecha_inscripcion, id))
        mysql.connection.commit()
        cur.close()
        flash('Inscripción Actualizada Satisfactoriamente')
        return redirect(url_for('inscripciones'))

    return render_template('edit_enrollment.html', enrollment=enrollment, students=students, courses=courses)

# Proporciona la funcionalidad para eliminar una inscripción de la base de datos mediante su ID.
@app.route('/delete_enrollment/<int:id>', methods=['POST'])
def delete_enrollment(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Inscripciones WHERE id = %s", [id])
    mysql.connection.commit()
    cur.close()
    flash('Inscripción Eliminada Satisfactoriamente')
    return redirect(url_for('inscripciones'))

# Punto de entrada de la aplicación que inicia el servidor web de Flask.
if __name__ == '__main__':
    app.run(debug=True)