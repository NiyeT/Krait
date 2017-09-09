import socket
import re

class server_template:
	def __init__(self,details):
		self.port=details['port']
		self.buffer_size=details['buffer_size']
		self.respond=details['unique']

	TCP_IP='127.0.0.1'

	def init(self):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.bind((self.TCP_IP,self.port))
		s.listen(0)
		return s		 

	def strip_headers(self,raw_header):
		pass

	def strip_commands(self,raw_header):
		header=re.match('GET /?([^\s]+)',raw_header).group(1)
		return header[1:len(header)]

	def format_commands(self,raw_commands):
		command=''
		sub_commands=[]
		raw_commands=re.findall('[^\&]+',raw_commands)
		for query in raw_commands:
			query=re.findall('[^\=]+',query)
			if(query[0]=='command'):
				command=query[1]
			else:
				sub_commands.append(query[1])
		return (command,sub_commands)

	def manage_response(self,response):
		self.strip_headers(response)
		raw_commands=self.strip_commands(response)
		return self.format_commands(raw_commands)

	def run_server(self):	
		s=self.init()
		print('Hosting @',(self.TCP_IP,self.port))
		while 1:
			conn,acc = s.accept()
			req = conn.recv(self.buffer_size)
			resp=self.manage_response(req.decode())
			self.respond(conn,resp)
			conn.close()

def test(connector,message):
	connector.send('redditors attempt? (:'.encode())

init={"port":8080,"buffer_size":2048,"unique":test}
template=server_template(init)
template.run_server()