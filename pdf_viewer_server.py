#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler,HTTPServer
from urllib.parse import urlparse, parse_qs
from snowflake.snowpark import Session
import os
import cgi
import json
import requests


PORT_NUMBER = 8091
OUTPUT_MODE = 'json'

class coeSnowDemoHandler(BaseHTTPRequestHandler):

	__init__(server_name, port_number, c_params):
		super().__init__(server_name, port_number)
		connection_params = {
			"account": '"' + c_params['account'] + '"',
			"database": '"' + c_params['database'] + '"',
			"schema": '"' + c_params['schema'] + '"',
			"role": '"' + c_params['role'] + '"',
			"user": '"' + c_params['user'] + '"',
			"password": '"' + c_params['password'] + '"' 
		}
		new_session = Session.builder.configs(connection_params).create()

	#Handle GET requests
	def do_GET(self):
		arr_pdfdocs = new_session.sql("select docname, docdescription, docdate, build_scoped_file_url(doclocation) from pdfdocs").collect()
		q_components = dict(qc.split("=") for qc in urlparse(self.path).query.split("&"))
		print q_components["outputMode"]
		i = 0
		if q_components:
			OUTPUT_MODE = q_components["outputMode"]
		if OUTPUT_MODE == "html":
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()
			self.wfile.write(bytes("<!DOCTYPE html"), "utf-8")
			self.wfile.write(bytes("<html>", "utf-8"))
			self.wfile.write(bytes("<head>", "utf-8"))
			self.wfile.write(bytes("<title>The PDF Document (Policy) Library", "utf-8"))
			self.wfile.write(bytes("</title>", "utf-8"))
			self.wfile.write(bytes("</head>", "utf-8"))
			self.wfile.write(bytes("<body><center>", "utf-8"))
			self.wfile.write(bytes("<table border=1 cellpadding=4>", "utf-8"))
			self.wfile.write(bytes("<tr><th>personID</th><th>Document Name</th><th>Description</th><th>Date</th><th>URL</th></tr>", "utf-8"))
			while(i < len(arr_pdfdocs):
				print("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>", (arr_pdfdocs[i][0], arr_pdfdocs[i][1], arr_pdfdocs[i][2], arr_pdfdocs[i][3]))
				rowInfo = "<tr><td>" + str(arr_pdfdocs[i][0]) + "</td><td>" + arr_pdfdocs[i][1] + "</td><td>" + arr_pdfdocs[i][2] + "</td><td>" + arr_pdfdocs[i][3] + "</td></tr>"
				i += 1
				self.wfile.write(bytes(rowInfo, "utf-8"))
			self.wfile.write(bytes("</table></center>", "utf-8"))
			self.wfile.write(bytes("</body>", "utf-8"))
			self.wfile.write(bytes("</html>", "utf-8"))
			return
		elif OUTPUT_MODE == "json":
			self.send_response(200)
			self.send_header('Content-type', 'application/json')
			self.end_headers()
			self.wfile.write(bytes("{", "utf-8"))
			while(i < len(arr_pdfdocs):
				pdfdocHeader = '"pdfdocEntry" : {'
				self.wfile.write(bytes(personHeader, "utf-8"))
				rowInfo = '"docname" : "%s", "docdescription" : "%s", "docdate" : "%s", "docURL" : "%s"' % (arr_pdfdocs[i][0], arr_pdfdocs[i][1], arr_pdfdocs[i][2], arr_pdfdocs[i][3])
				self.wfile.write(bytes(rowInfo, "utf-8"))
				self.wfile.write(bytes("},", "utf-8"))
				i += 1
			self.wfile.write(bytes("}", "utf-8"))
			return

	def do_POST(self):
	# My Post Code will go here
		myForm = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={'REQUEST_METHOD':'POST', 'CONTENT_TYPE':self.headers['Content-Type'],})
		print("%s %s %s %s" % (myForm.getvalue("fld_fname"), myForm.getvalue("fld_lname"), myForm.getvalue("fld_middle"), myForm.getvalue("fld_bioURL")))
		self.wfile.write(bytes(str(num_rows_inserted), "utf-8"))
		self.send_response(200)
		self.end_headers()
		return

try:
	with open('connection_params.json', 'r') as f_params:
		f_data=f_params.read()
	c_params = json.loads(f_data)	
	server = HTTPServer(('', PORT_NUMBER, c_params), coeSnowDemoHandler)
	print( 'Started httpserver on port %s ' % PORT_NUMBER)
	server.serve_forever()

except KeyboardInterrupt:
    print( 'Kill signal received.  Terminiating server...')

