
{
    'name': 'Sales custom ',
    'version': '1.3',
    'category': 'sale',
    'description': """
add quotation for views user
""",
    'depends': ['sale','sales_team'],
    'data': ['secuirty/groups_view.xml','views/menus.xml','views/view_form.xml','secuirty/ir.model.access.csv'],
     
    'installable': True,
    'auto_install': True,
}
