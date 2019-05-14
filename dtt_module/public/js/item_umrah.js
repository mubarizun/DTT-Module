frappe.ui.form.on("Item Umrah", {
    kota: (frm) => {
        frm.doc.penerbangan.forEach((penerbangan, index) => {
            frm.fields_dict.penerbangan.grid.get_field('hotel').get_query = () => {
                return {
                    filters: {
                        "kota": penerbangan.kota
                    }
                }
            }
        })
        frm.refresh_field("penerbangan")
    }
})