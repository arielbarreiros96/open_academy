from odoo import models, fields, api, _

class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'Session class'

    name = fields.Char(_("Name"),required=True)
    start_date = fields.Date(_("Start Date"))
    duration = fields.Integer(_("Duration"), help=_("Duration in min"))
    number_of_seats = fields.Integer(_("Number of seats"))
    instructor = fields.Many2one("res.partner", string=_("Instructor"))
    course_id = fields.Many2one('openacademy.course', _("Course"))
    attendees_ids = fields.Many2many('res.partner', 'attendees_partner_rel', string=_("Attendees"))

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Not implemented on the form res.partner form view
    session_ids = fields.Many2many(
        'openacademy.session',
        'attendees_partner_rel',
        string='Sessions'
    )
