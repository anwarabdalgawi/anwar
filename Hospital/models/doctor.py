
from inspect import FullArgSpec
from odoo import models ,fields ,api ,_  

class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Doctor"
    _rec_name = 'name'
    
    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', copy=False, tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
        ],string='Gender', required=True, default='male', tracking=True)
    note = fields.Text(string='Description', tracking=True)
    image = fields.Binary(string="Patient Image", tracking=True)
    doctor_phone = fields.Char(string='Phone')
