# -*- coding: utf-8 -*-
# from odoo import http


# class MyCustom(http.Controller):
#     @http.route('/my_custom/my_custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_custom/my_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_custom.listing', {
#             'root': '/my_custom/my_custom',
#             'objects': http.request.env['my_custom.my_custom'].search([]),
#         })

#     @http.route('/my_custom/my_custom/objects/<model("my_custom.my_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_custom.object', {
#             'object': obj
#         })

