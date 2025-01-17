from odoo import models, fields

class AbsenceEtudiant(models.Model):
    _name = 'gestion.absence.etudiant'
    _description = 'Gestion des Absences des Étudiants'

    name = fields.Char(string="Motif d'absence", required=True)
    student_id = fields.Many2one('res.partner', string="Étudiant", required=True)
    date_debut = fields.Date(string="Date de début", required=True)
    date_fin = fields.Date(string="Date de fin", required=True)
    type_absence = fields.Selection([
        ('conge', 'Congé'),
        ('maladie', 'Maladie'),
        ('autre', 'Autre'),
    ], string="Type d'absence", required=True)
    justification = fields.Text(string="Justification", required=True)
    status = fields.Selection([
        ('draft', 'Brouillon'),
        ('submitted', 'Soumis'),
        ('approved', 'Approuvé'),
        ('rejected', 'Rejeté'),
    ], string="Statut", default='draft')
