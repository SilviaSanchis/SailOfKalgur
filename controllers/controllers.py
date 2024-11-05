# -*- coding: utf-8 -*-
# from odoo import http


# class SailOfKalgur(http.Controller):
#     @http.route('/sail_of_kalgur/sail_of_kalgur', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sail_of_kalgur/sail_of_kalgur/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sail_of_kalgur.listing', {
#             'root': '/sail_of_kalgur/sail_of_kalgur',
#             'objects': http.request.env['sail_of_kalgur.sail_of_kalgur'].search([]),
#         })

#     @http.route('/sail_of_kalgur/sail_of_kalgur/objects/<model("sail_of_kalgur.sail_of_kalgur"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sail_of_kalgur.object', {
#             'object': obj
#         })

