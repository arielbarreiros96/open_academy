from odoo import models, fields, api

class Course(models.Model):
    _name = 'open_academy.course'
    _description = 'Course class'

    title = fields.Char(required=True)
    description = fields.Char()
