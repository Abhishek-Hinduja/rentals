# Copyright (c) 2024, BWH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Course(Document):
	def before_insert(self):
		if not self.course_code:
			self.course_code = frappe.model.naming.make_autoname("CRS-.YYYY.-.#####")

