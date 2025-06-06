# 🧑‍💻 Sistema de Gestión de Usuarios - Consola Interactiva

## 🎯 Objetivo Principal

Desarrollar un programa de consola interactivo que permita la **administración de usuarios** diferenciando sus **roles** (Administrador / Usuario estándar), asegurando un sistema de **registro**, **inicio de sesión** y **control de acceso** seguro, claro y modular.

El proyecto utiliza un **diagrama de clases con herencia** como base para la organización del código, aprovechando la reutilización y especialización de atributos y métodos.

---

## 🧩 Diagrama de Clases (Herencia)

Se implementó un diseño basado en **herencia** para representar los diferentes tipos de usuarios del sistema:

- `Usuario`: clase base abstracta.
- `Cliente`: hereda de `Usuario`. Representa al usuario estándar.
- `Administrador`: hereda de `Usuario`. Con acceso a funciones avanzadas.

---

## 📚 Objetivos Específicos

- Diseñar la base de datos: estructura relacional para almacenar usuarios y roles.
- Implementar consultas SQL: para crear, leer, actualizar y eliminar datos.
- Definir el diagrama de clases: aplicando principios de orientación a objetos.
- Desarrollar la lógica de usuarios: registrar, eliminar y mostrar datos.
- Integrar autenticación: validación de credenciales con control de acceso por rol.
- Diseñar un menú interactivo: navegación sencilla para el usuario vía consola.

---

## ✅ Requerimientos Funcionales

- Registro de usuarios con validaciones:
  - Contraseña de mínimo 6 caracteres.
  - Debe contener letras y números.
- Inicio de sesión con validación contra la base de datos.
- Diferenciación de permisos según el rol:
  - **Usuario estándar**: solo accede a sus datos personales.
  - **Administrador**: puede visualizar todos los usuarios, cambiar roles y eliminarlos.
- Manejo adecuado de errores y mensajes informativos ante entradas inválidas.

---

## 🛠️ Requerimientos No Funcionales

- **Modularidad**: código estructurado en módulos, clases y funciones.
- **Legibilidad**: uso de nombres descriptivos y estructura clara.
- **Usabilidad**: interfaz intuitiva basada en texto con mensajes claros.

---

## 🧪 Funcionalidades del Menú

### Usuario Estándar

- Visualizar sus propios datos.

### Administrador

- Listar todos los usuarios registrados.
- Cambiar el rol de un usuario.
- Eliminar usuarios registrados.

---

## 🗃️ Base de Datos

Se utiliza una base de datos **SQLite** para almacenar la información persistente de los usuarios. Se implementan operaciones SQL para insertar, consultar y eliminar registros.

---

## 💡 Tecnologías y Herramientas

- Python 3
- SQLite
- Programación Orientada a Objetos (POO)
- Menú interactivo en consola

---

## 📌 Actividades Realizadas

- ✅ Diseño del diagrama de clases
- ✅ Implementación del modelo en Python
- ✅ Conexión con base de datos SQLite
- ✅ Desarrollo del menú y lógica de roles
- ✅ Validaciones de seguridad y entrada

---

## ▶️ Ejecución del Proyecto

1. Clonar o descargar el repositorio.
2. Ejecutar el archivo principal en un entorno con **Python 3**.
3. Seguir las instrucciones del menú en consola.

---

## ✍️ Autor

**Ivo Konstantinow** – Desarrollador Web & Estudiante de Programación

**Lourdes Del Valle Pérez** – Estudiante de desarrollo web

**Noelia Karina Pucheta** – Estudiante de desarrollo web

**Daniela Lencina** – Estudiante de desarrollo web

**Guadalupe Villega.** – Estudiante de desarrollo web

---
