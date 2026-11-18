# Gestión de Alumnos — Odoo 19

Addon de ejemplo que crea el modelo `academia.alumno` y permite gestionar alumnos desde el menú **Academia → Alumnos**.

## Contenido
- Modelo Python con nombre, apellidos, fecha de nacimiento, email y estado activo.
- Vistas de lista, formulario y búsqueda.
- Acción y menús.
- Permisos de acceso para usuarios internos (`base.group_user`).

## Instalación
1. Copia la carpeta `academia_alumno` dentro de una ruta de addons personalizada.
2. Comprueba que esa ruta esté incluida en `addons_path` de tu archivo de configuración de Odoo.
3. Reinicia el servidor Odoo.
4. Activa el modo desarrollador.
5. Ve a Aplicaciones y pulsa **Actualizar lista de aplicaciones**.
6. Busca **Gestión de Alumnos** e instálalo.

## Nota
El permiso incluido concede lectura, escritura, creación y eliminación a todos los usuarios internos. En un proyecto real conviene definir grupos y permisos más restrictivos.
