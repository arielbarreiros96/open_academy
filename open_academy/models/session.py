from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'Session class'

    name = fields.Char(_("Name"), required=True)
    start_date = fields.Date(_("Start Date"), default=fields.Date.context_today)
    duration = fields.Integer(_("Duration"), help=_("Duration in min"))
    number_of_seats = fields.Integer(_("Number of seats"))
    taken_seats = fields.Float(_("Taken Seats"), compute='_compute_taken_seats')
    # This shuould be a many2many, or the session_instructor_ids on res_partner should be a one2many related to this one
    instructor = fields.Many2one("res.partner", string=_("Instructor"))
    course_id = fields.Many2one('openacademy.course', _("Course"))
    attendees_ids = fields.Many2many('res.partner', 'attendees_partner_rel', string=_("Attendees"))

    _sql_constraints = [
        ('check_number_of_seats', 'CHECK (number_of_seats <= 50)', 'No session can have more than 50 seats'),
    ]

    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('name'):
            default['name'] = _("%s (copy)", self.name)
        return super(Session, self).copy(default)

    @api.depends('attendees_ids')
    def _compute_taken_seats(self):
        for record in self:
            if record.number_of_seats != 0:
                record.taken_seats = 100*(len(record.attendees_ids)/record.number_of_seats)
            else:
                record.taken_seats = 0

    @api.onchange('attendees_ids, number_of_seats')
    def _onchange_attendees(self):
        if len(self.attendees_ids) > self.number_of_seats:
            raise ValidationError(_("The max number of seats for session %s is %s") % (self.name, self.number_of_seats))

    @api.constrains('attendees_ids', 'instructor')
    def _check_instructor(self):
        for record in self:
            if record.instructor in record.attendees_ids:
                raise ValidationError(_("Instructor is on the attendees list!!"))

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Not implemented on the form res.partner form view
    session_ids = fields.Many2many(
        'openacademy.session',
        'attendees_partner_rel',
        string=_('Sessions')
    )
    instructor = fields.Boolean(_("Instructor"))
    #Esto debería ser un one2many relacionado al campo instructor
    session_instructor_ids = fields.Many2many(
        'openacademy.session',
        string=_('Instructs on')
    )
