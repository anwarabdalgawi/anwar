
from inspect import FullArgSpec
from odoo import models ,fields ,api ,_  

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"
    _rec_name = 'patient_name'
    
    patient_name = fields.Char(string='Patient Name', required=True, tracking=True)
    age = fields.Integer(string='Age', copy=False, tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
        ],string='Gender', required=True, default='male', tracking=True)
    note = fields.Text(string='Description', tracking=True)
    image = fields.Binary(string="Patient Image", tracking=True)
    phone = fields.Char(string='Phone', related='doctor_id.doctor_phone')
    doctor_id = fields.Many2one('hospital.doctor', string='Name Doctor')
