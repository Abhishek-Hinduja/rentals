# Copyright (c) 2024, BWH and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Test(Document):
	def before_save(self):
		self.name1="xyz"
	
