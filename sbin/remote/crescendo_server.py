import python_server_template

class crescendo_server:
	def __init__(self):
		pass

	def run_server(connector,commands):

		


		connector.send(''.encode())

crescendo=crescendo_server()


init={"port":8080,"buffer_size":2048,"unique":crescendo.run_server}
server_template=python_server_template(init)
server_template.run_server()