const toggleUmrahSection = (frm) => {
    let root_parent = getRootItemGroup(frm.doc.item_group);
    let company_item_group = getCompanyItemGroup("Duta Telaga Takwa")
    root_parent === company_item_group ? frm.toggle_display("umrah_section", true) : ""
}

frappe.ui.form.on("Item", {
    setup: (frm) => {
        frm.set_query("bandara_keberangkatan", function() {
			return {
				filters: [
					["Item Umrah Kota","destinasi", "=", 0]
				]
			}
        })
        frm.fields_dict['penerbangan'].grid.get_field("kota").get_query = function(doc, cdt, cdn) {
            return {
                filters: [
                    ["Item Umrah Kota","destinasi", "=", 1]
                ]
            }
        }
    },
    onload: function(frm) {
        toggleUmrahSection(frm)
    },
    refresh: function(frm) {
        toggleUmrahSection(frm)
    }
});