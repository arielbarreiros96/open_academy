from odoo import models, fields, api, _

class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'Session class'

    name = fields.Char(_("Name"),required=True)
    start_date = fields.Date(_("Start Date"))
    duration = fields.Integer(_("Duration"),help=_("Duration in min"))
    number_of_seats = fields.Integer(_("Number of seats"))
    instructor = fields.Many2one("res.partner", string=_("Instructor"))
    course = fields.Many2one('openacademy.course', _("Course"))
