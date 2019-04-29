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
    },
    onload: function(frm) {
        toggleUmrahSection(frm)
    },
    refresh: function(frm) {
        toggleUmrahSection(frm)
    }
});