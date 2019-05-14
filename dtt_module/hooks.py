# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "dtt_module"
app_title = "DTT Module"
app_publisher = "Kataba"
app_description = "Module DTT"
app_icon = "octicon octicon-file-directory"
app_color = "yellow"
app_email = "info@kataba.id"
app_license = "MIT"
app_include_js = ["assets/dtt_module/js/company.js", "assets/dtt_module/js/sales_partner.js", "assets/dtt_module/js/sales_order.js", "assets/dtt_module/js/purchase_invoice.js", "assets/dtt_module/js/purchase_receipt.js", "assets/dtt_module/js/delivery_note.js", "assets/dtt_module/js/sales_invoice.js", "assets/dtt_module/js/kelengkapan_umrah.js", "assets/dtt_module/js/payment_entry.js", "assets/dtt_module/js/1utils.js", "assets/dtt_module/js/virtual_account.js", "assets/dtt_module/js/item.js", "assets/dtt_module/js/item_umrah_hotel.js", "assets/dtt_module/js/item_umrah.js"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/dtt_module/css/dtt_module.css"
# app_include_js = "/assets/dtt_module/js/dtt_module.js"

# include js, css files in header of web template
# web_include_css = "/assets/dtt_module/css/dtt_module.css"
# web_include_js = "/assets/dtt_module/js/dtt_module.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "dtt_module.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "dtt_module.install.before_install"
# after_install = "dtt_module.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "dtt_module.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"dtt_module.tasks.all"
# 	],
# 	"daily": [
# 		"dtt_module.tasks.daily"
# 	],
# 	"hourly": [
# 		"dtt_module.tasks.hourly"
# 	],
# 	"weekly": [
# 		"dtt_module.tasks.weekly"
# 	]
# 	"monthly": [
# 		"dtt_module.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "dtt_module.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "dtt_module.event.get_events"
# }

