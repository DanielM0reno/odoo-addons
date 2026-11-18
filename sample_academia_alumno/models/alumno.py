from odoo import fields, models


class AcademiaAlumno(models.Model):
    _name = "academia.alumno"
    _description = "Alumno de la academia"
    _order = "name, apellidos"

    name = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento")
    email = fields.Char(string="Correo electrónico")
    activo = fields.Boolean(string="Activo", default=True)
