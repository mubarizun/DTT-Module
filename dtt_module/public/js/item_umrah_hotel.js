frappe.ui.form.on("Item Umrah Hotel", {
    setup: (frm) => {
        frm.set_query("kota", function() {
			return {
				filters: [
					["Item Umrah Kota","destinasi", "=", 1]
				]
			}
		})
    }
})
