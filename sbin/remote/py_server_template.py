import socket
import re

class server_template:
	def __init__(self,details):
		self.PORT=details['port']
		self.BUFFER_SIZE=details['buffer_size']
		self.unique=details['unique']
		self.PORT=details['port']
		self.BUFFER_SIZE=details['buffer_size']
		self.unique=details['unique']

	TCP_IP='127.0.0.1'

	def init(self):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.bind((self.TCP_IP,self.PORT))
		s.listen(0)
		return s	

	def normalize(self,data):
		data=data.decode()
		print('#'*40)
		print(data)
		print('#'*40)
		return data

	def strip_commands(self,header):
		try:
			header=re.match('GET /?([^\s]+)',header).group(1)
			return header[1:len(header)]
		except:
			return False

	def format_commands(self,commands):
		temp={}
		queries=re.findall('[^\&]+',commands)
		for query in queries:
			query=re.findall('[^\=]+',query)
			temp.update({query[0]:query[1]})
		try:
			temp.sub_commands=temp.sub_commands.replace('\.','\,')
			return (temp.command,temp.sub_commands)
		except Exception as err:
			print(err)

	def response_template(self):
		return 'HTTP/1.1 200 OK\n'

	def start_server(self):
		s=self.init()
		while 1:
			conn,acc = s.accept()
			data = conn.recv(self.BUFFER_SIZE)
			unformatted_commands=self.strip_commands(self.normalize(data))
			if(not unformatted_commands): break
			formatted_commands=self.format_commands(unformatted_commands)

			# unique=self.unique(format_commandstted_commands)
			# unique=self.response_template() + unique
			# conn.send(unique.encode())
			conn.send('unique\n'.encode())
			conn.close()