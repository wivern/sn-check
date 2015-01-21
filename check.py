#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import model

urls = (
  '/', 'index'
)

web.config.debug = True
### Templates
render = web.template.render('templates', base='base')

class index:

	form = web.form.Form(
        web.form.Textbox('serial', web.form.notnull, description="Серийный номер:", placeholder="введите серийный номер"),
	)
	
	def GET(self):
		web.header("Content-Type", "text/html; charset= utf-8") 
		form = self.form()
		return render.index(form)
		
	def POST(self):
		web.header("Content-Type", "text/html; charset= utf-8") 
		form = self.form()
		if not form.validates():
			return render.index(form)
		serial = form.d.serial
		items = model.get_serial_numbers(serial)
		return render.result(items,serial)
		
		
if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()      