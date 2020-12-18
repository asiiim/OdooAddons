# @author Aashim Bajracharya <ashimbazracharya@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "Bulk Update Product Price",

    'summary': """
        Update cost and sale price of the product in bulk.""",

    'description': """
        Select the products you want to update the price (sale and cost price) and update the price.
    """,

    'author': "Aashim Bajracharya",
    'email': "ashimbazracharya@gmail.com",

    'category': 'Inventory',
    'version': '12.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
        # 'wizards/update_product_price.xml'
    ],

    'installable': False
}