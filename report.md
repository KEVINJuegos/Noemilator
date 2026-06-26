<a id="top"></a>

<div align="center">
  <img src="https://img.icons8.com/color/96/calendar--v1.png" alt="Calendario">
  <img src="https://img.icons8.com/color/96/classroom.png" alt="Aula">
  <img src="https://img.icons8.com/color/96/school.png" alt="Escuela">
  <h1>Noemilator</h1>
  <p><em>Planificador de Horarios para Centros Educativos</em></p>
</div>

<p align="center">
  <a href="#">
    <img src="https://img.shields.io/badge/hecho%20con-Flet-2E7D32.svg" alt="Hecho con Flet">
  </a>
  <a href="https://www.python.org/downloads/" target="_blank">
    <img src="https://img.shields.io/badge/python-3.10%2B-blue.svg" alt="Python 3.10+">
  </a>
</p>

<div align="center">
  <a href="#-acerca-del-proyecto">Acerca del Proyecto</a>
  <span>&nbsp;✦&nbsp;</span>
  <a href="#-características">Características</a>
  <span>&nbsp;✦&nbsp;</span>
  <a href="#-tecnologías">Tecnologías</a>
  <span>&nbsp;✦&nbsp;</span>
  <a href="#-instrucciones-de-uso">Instrucciones de Uso</a>
</div>

<br>

## 📜 Acerca Del Proyecto

**Noemilator** es un programa de planificación de horarios semanales diseñado específicamente para centros educativos. Su propósito principal es organizar, crear y ofrecer una vista general de los horarios de las diferentes sesiones o clases de un centro educativo, relacionándolos con sus respectivos locales, personal docente, alumnos, materias y otros recursos relevantes.

El proyecto nació de la necesidad de contar con una herramienta sencilla pero funcional que permitiera a directores, coordinadores académicos y personal administrativo gestionar los horarios semanales de manera eficiente, sin depender de hojas de cálculo complejas o sistemas demasiado sofisticados que requieren una curva de aprendizaje extensa.

El programa fue diseñado con un enfoque centrado en el usuario: cómodo e intuitivo, práctico y funcional, pero sin perder la sencillez que lo hace accesible para cualquier persona del ámbito educativo, independientemente de su nivel técnico.

<p align="right">(<a href="#top">Volver al inicio 🔝</a>)</p>

## 💬 Características

- 📅 **Planificación semanal**: creación y gestión de horarios para toda la semana, organizados por días y franjas horarias.
- 🏫 **Gestión de locales**: asignación de aulas, laboratorios, salones y otros espacios físicos a cada sesión.
- 👨‍🏫 **Gestión de personal**: registro de docentes y su asignación a materias y horarios específicos.
- 📚 **Gestión de materias**: catalogación de asignaturas con sus respectivas características y requisitos.
- 👥 **Gestión de alumnos**: organización de grupos, cursos y estudiantes vinculados a cada horario.
- 🔍 **Vista general**: panel centralizado que muestra de un vistazo todos los horarios activos, conflictos y disponibilidad.
- ⚡ **Detección de conflictos**: alertas automáticas cuando se detectan superposiciones de horarios, asignaciones duplicadas de locales o docentes, o incompatibilidades.
- 💾 **Persistencia de datos**: guardado automático del estado del sistema en archivos JSON para recuperación rápida.
- 🎨 **Interfaz intuitiva**: diseño limpio y minimalista construido con Flet, pensado para ser usado sin necesidad de manual.

<p align="right">(<a href="#top">Volver al inicio 🔝</a>)</p>

## 🧰 Tecnologías

- **Python**: lenguaje principal del proyecto, aprovechando su legibilidad y ecosistema.
- **Flet**: framework para construir interfaces de usuario multiplataforma (web, escritorio y móvil) con Python, basado en Flutter.
- **JSON**: formato de persistencia de datos, facilitando la portabilidad y edición manual si es necesario.

<p align="right">(<a href="#top">Volver al inicio 🔝</a>)</p>

## 📋 Instrucciones de Uso

La aplicación está organizada en diferentes secciones accesibles desde la barra de navegación lateral:

### 1. 📅 Vista General (Dashboard)

- Observa de un vistazo todos los horarios de la semana.
- Filtra por día, docente, local o materia para encontrar rápidamente lo que buscas.
- Identifica conflictos visualmente: superposiciones se marcan en rojo para su fácil detección.

### 2. ➕ Crear Horario

- Selecciona el día de la semana y la franja horaria.
- Elige la materia que se impartirá.
- Asigna un docente disponible; el sistema muestra solo aquellos que no tengan clase en ese horario.
- Selecciona un local libre; aulas ocupadas se muestran deshabilitadas.
- Define el grupo o curso al que va dirigido.
- Guarda el horario; el sistema valida automáticamente que no existan conflictos antes de confirmar.

**Ejemplo práctico:**

> Quieres programar la clase de Matemáticas para el grupo 10-A el lunes de 8:00 a 9:30. Seleccionas "Lunes", "08:00-09:30", "Matemáticas", y el sistema te muestra los docentes de matemáticas disponibles (por ejemplo, Prof. García y Prof. López). Eliges al Prof. García. Luego seleccionas el local: el sistema indica que el Aula 101 está libre, pero el Laboratorio de Ciencias está ocupado por Física. Guardas el horario y aparece en el dashboard.

### 3. 👨‍🏫 Gestión de Docentes

- Registra nuevos docentes con su nombre, especialidad y disponibilidad horaria.
- Edita o elimina docentes existentes.
- Visualiza la carga horaria semanal de cada docente.

### 4. 🏫 Gestión de Locales

- Añade, edita o elimina aulas, laboratorios, salones y otros espacios.
- Define la capacidad y características de cada local.
- Consulta la ocupación semanal de cada espacio.

### 5. 📚 Gestión de Materias

- Crea materias con nombre, código, duración por sesión y requisitos especiales (por ejemplo, necesita laboratorio).
- Asocia materias a docentes competentes.

### 6. 👥 Gestión de Grupos

- Organiza grupos, cursos o secciones.
- Asigna alumnos a grupos y consulta los horarios asignados a cada uno.

### 7. ⚙️ Configuración

- **Exportar**: descarga el estado actual del centro educativo como archivo JSON.
- **Importar**: carga un archivo JSON previamente exportado para restaurar el estado.
- **Reiniciar**: vuelve a la configuración por defecto.

<p align="right">(<a href="#top">Volver al inicio 🔝</a>)</p>

## 🎓 Aprendizajes Durante el Desarrollo

Durante la creación de Noemilator, el proceso de desarrollo fue una experiencia de aprendizaje continuo. A continuación se detallan los principales conocimientos y habilidades adquiridos:

### Aprendizaje de Flet

Uno de los mayores aprendizajes fue el dominio de **Flet**, un framework relativamente nuevo que permite construir interfaces de usuario multiplataforma utilizando únicamente Python. Su aprendizaje presentó desafíos: la documentación era limitada, lo que requirió experimentacion con horas de prueba y error.

### Uso de Dataclasses

Otro aprendizaje fundamental fue el uso extensivo de **dataclasses** de Python. Las dataclasses permiten definir clases de datos de forma concisa, eliminando la necesidad de escribir repetidamente métodos `__init__`, `__repr__` y `__eq__`. Esto resultó especialmente útil para modelar las entidades del dominio de Noemilator: `Horario`, `Docente`, `Local`, `Materia`, `Grupo`, entre otras. Gracias a las dataclasses, el código de los modelos es limpio, legible y fácil de mantener. Además, al combinarlas con el módulo `json`, la serialización y deserialización de objetos se simplificó enormemente, permitiendo guardar y cargar el estado completo del sistema con pocas líneas de código.

### Manejo de JSON para Persistencia

La persistencia de datos mediante **JSON** fue otra aprendizaje. Se optó por JSON por su simplicidad, legibilidad y portabilidad. A diferencia de una base de datos relacional compleja, JSON permite inspeccionar y editar los datos directamente con un editor de texto, lo cual es una ventaja para un programa en desarrollo o para usuarios técnicos. Permitiendo su exportación y exportación sencilla sin cifrados.

<p align="right">(<a href="#top">Volver al inicio 🔝</a>)</p>

## 🧠 Dificultades Encontradas y Cómo Se Resolvieron


<p align="right">(<a href="#top">Volver al inicio 🔝</a>)</p>

<br>
<hr>
<p align="center">📅 ¡Planifica con claridad, gestiona con confianza! 📅</p>
<sub><sup>Un proyecto creado con dedicación para el ámbito educativo.</sup></sub>
