from odoo import models, fields, api, _

class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Course class'

    title = fields.Char(_("Title"), required=True)
    description = fields.Char()
    responsible = fields.Many2one('res.users', _("Responsible"))
