# Copyright (c) 2024, BWH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime

class Student1(Document):
    def before_save(self):
        self.full_name = f"{self.first_name or ''} {self.middle_name or ''} {self.last_name or ''}".strip()

        frappe.msgprint(self.full_name)

    def validate(self):
        dob_date = datetime.strptime(self.date_of_birth, '%Y-%m-%d').date()
        today = datetime.today().date()
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))

        if age < 18:
            frappe.throw("Enter a valid DOB. Age must be 18 or older.")
        
