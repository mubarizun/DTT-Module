from __future__ import unicode_literals
import frappe, json
 
@frappe.whitelist()
def run_sql(sql):
	# For development only, remove on production
	return frappe.db.sql(sql)

@frappe.whitelist()
def test():
	pi = frappe.get_doc({
		"doctype": "Purchase Invoice",
		"credit_to": "2111.001 - Hutang Dagang Dalam Negeri - DUIB",
		"items": [
			{"item_code": "TKOA99", "qty": 11}
		]
	})
	pi.insert()

@frappe.whitelist()
def create_kelengkapan_umrah(frm_name, customer, count, item_code, item_name, grand_total):
	# doc = frappe.new_doc("Kelengkapan Umrah")
	# doc.update({

	# })
	kelengkapan_umrah = frappe.get_doc({
		"doctype": "Kelengkapan Umrah",
		"sales_order": frm_name,
		"contact": customer,
		"count": count,
		"total_sales_order": grand_total,
		"total_pembayaran": 0,
		"item": item_code,
		"customer": customer,
		"items": [
			{"item_code": item_code, "item_name": item_name, "against_sales_order": frm_name, "customer": customer, "count": count}
		]
	})
	kelengkapan_umrah.insert()

@frappe.whitelist()
def make_new_VA(VANO, docname):
	va = frappe.get_doc({
		"doctype": "Virtual Account",
		"virtual_account_no": VANO,
		"sales_order_no":docname,
		"status":"Planned"
	})
	va.insert()

	return str(va.name)

@frappe.whitelist(allow_guest=True)
def get_VA():
	sql = "select name from `tabVirtual Account`"
	return frappe.db.sql(sql)

@frappe.whitelist()
def update_VA_field(VANO, docname):
	sql = "update `tabSales Order` set virtual_account='" + VANO + "' where name='" + docname + "'"
	return frappe.db.sql(sql)

@frappe.whitelist()
def delete_VA(VANO, docname):
	#sql = "update `tabSales Order` set virtual_account=NULL where name ='"+docname+"'"
	#frappe.db.sql(sql)
	sql = "update `tabVirtual Account` set status = 'cancelled' where name ='"+VANO+"'"
	return frappe.db.sql(sql)

@frappe.whitelist()
def new_journal_entry(doc):
	from datetime import datetime
	doc = json.loads(doc)

	def get_je_items():
		return {
		"doctype": "Journal Entry",
		"voucher_type": "Journal Entry",
		"naming_series": "ACC-JV-.YYYY.-",
		"company": doc["company"],
		"posting_date": str(datetime.now())[:str(datetime.now()).index(" ")],
		"cheque_no": doc["name"],
		"cheque_date": doc["posting_date"]
	}

	je_item_1 = get_je_items()

	je_item_1["accounts"] = [
		{
			"account": doc["debit_to"],
			"cost_center": "Main - DTT", # change later
			"debit_in_account_currency": doc["agent_commission_rate"],
			"party_type": "Customer", # change later
			"party": "Customer 1", # change later
		},
		{
			"account": "2141.000 - Hutang Pajak - DTT", # change later
			"party_type": "Supplier",
			"party": doc["sales_partner"],
			"cost_center": "Main - DTT", # change later
			"credit_in_account_currency": doc["agent_commission_rate"]
		}
	]

	je_item_2 = get_je_items()

	je_item_2["accounts"] = [
		{
			"account": doc["debit_to"],
			"cost_center": "Main - DTT", # change later
			"debit_in_account_currency": doc["territory_commission_rate"],
			"party_type": "Customer", # change later
			"party": "Customer 1", # change later
		},
		{
			"account": "2141.000 - Hutang Pajak - DTT", # change later
			"party_type": "Supplier",
			"party": doc["sales_partner"], # change later
			"cost_center": "Main - DTT", # change later
			"credit_in_account_currency": doc["territory_commission_rate"]
		}
	]

	a = frappe.get_doc(je_item_1).insert()
	b = frappe.get_doc(je_item_2).insert()
	a.submit()
	b.submit()
	return ({"item_1":a.name,"item_2":b.name})
	
@frappe.whitelist()
def submit_so(sales_order_name):
	if sales_order_name != "":
		return frappe.db.sql("update `tabSales Order` set docstatus = 1 where name='"+sales_order_name+"'")

@frappe.whitelist()
def add_virtual_account(sales_order_name):
	def get_parent_item_group(item_group_name):
		item_group = {}
		parent = {}

		for item_group_data in frappe.get_all("Item Group"):
			if item_group_name == str(item_group_data.name):
				item_group = frappe.get_doc("Item Group", item_group_data.name)
		if item_group != {}:
			if item_group.parent_item_group == "Paket Umrah":
				parent = item_group
			else:
				parent = get_parent_item_group(item_group.parent_item_group)

		return parent


	def get_so(sales_order_name):
		sales_order = {}
		for so in frappe.get_all("Sales Order"):
			if str(sales_order_name) == str(so.name):
				sales_order = frappe.get_doc("Sales Order", so.name)

		return sales_order


	def gen_va(so):
		import datetime

		new_va = ""
		new_id = ""
		newRunningNumber = ""

		va_setup = {}
		for va_setup_data in frappe.get_all("VA Setup"):
			if str(so.company) == str(va_setup_data.name):
				va_setup = frappe.get_doc("VA Setup", va_setup_data.name)

		new_va += str(va_setup.company_prefix)

		typeFound = False
		for product_prefix in va_setup.product_prefix:
			if product_prefix.document_type == "Project" and product_prefix.document_type_id == so.project and typeFound == False:
				new_va += product_prefix.id
				new_id += product_prefix.id
				typeFound = True
			elif product_prefix.document_type == "Item Group":
				for item in so.items:
					if product_prefix.document_type_id == get_parent_item_group(item.item_group) and typeFound == False:
						new_va += product_prefix.id
						new_id += product_prefix.id
						typeFound = True
			else:
				new_id += "11"
				new_va += "11"
				typeFound = True
		new_va += str(datetime.datetime.today().year)[2:]
		
		va_list = get_VA()
		prefixes = []

		for va in va_list:
			va = va[0]

			id = va[4:6]
			running_number = int(va[10:])
			prefixes.append({
				"id": id,
				"running_number": running_number
			})

		prefixes = sorted(prefixes, key = lambda p: p["running_number"], reverse=True)

		new_running_number = ""
		idFound = False

		for prefix in prefixes:
			if prefix["id"] == new_id:
				rn = int(prefix["running_number"])+1
				new_running_number = str(rn).zfill(8)
				idFound = True
				break

		if len(va_list) == 0 or idFound == False:
			new_running_number = str(1).zfill(8)

		new_va += new_running_number

		return new_va

	so = get_so(sales_order_name)
	
	if so.docstatus == 1:
		if so.virtual_account == "" or so.virtual_account == None:
			va = gen_va(so)
			make_new_VA(va, so.name)
			update_VA_field(va, so.name)
			frappe.msgprint(str("New virtual account has been added to sales order "+so.name), raise_exception=False)
		else:
			frappe.msgprint("Sales order has virtual account already", raise_exception=True)
	else:
		frappe.msgprint("Submit sales order first", raise_exception=True)
