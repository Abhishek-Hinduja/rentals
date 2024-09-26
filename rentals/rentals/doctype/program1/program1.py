# Copyright (c) 2024, BWH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Program1(Document):
	pass
    # def validate(self):
    #     self.calculate_total_credits()

    # def on_update(self):
    #     self.calculate_total_credits()

    # def calculate_total_credits(self):
    #     total_credits = 0
    #     for score in self.courses:
    #         print(score)
    #         credit=frappe.get_doc("Course",score).credits
    #         print(credit)
    #         total_credits+=credit
            
    #     self.total_credits = total_credits