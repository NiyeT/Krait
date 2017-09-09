from re import findall
from json import loads
import os
from termcolor import colored																																												
	
# class user:
# 	def __init__(self):
# 		pass

# 	username='Public@Krait: '

# 	paths='//home/cress/Lucy/bin://home/cress/Lucy/applications'

# 	#takes:
# 		#username
# 	#returns:
# 		#user location
# 	def user_search(self,username):
# 		username=username + '.data'
# 		user_container=os.getcwd() + '/users/'
# 		usernames=os.listdir(user_container)
# 		for file in usernames:
# 			if(username == file):
# 				return  user_container + username
# 		return False

# 	#takes:
# 		#user location
# 	#returns:
# 		#json encoded user info
# 	def user_load(self,user_location):
# 		user_location=open(user_location).read()
# 		user_data=loads(user_location)
# 		return user_data				

# 	#takes:
# 		#location of user info
# 	#returns:
# 		#boolean representing user's login attempt
# 	def verify_user(self,mix):
# 		def failed_login():
# 			pass

# 		tries=3
# 		for attempt in range(tries):
# 			passw=input('Credentials: ')
# 			# passw=krypt.nKrypt(passw)
# 			if(passw==mix): break
# 			if(attempt==tries-1):
# 				failed_login()
# 				return False
# 		return True

# 	#takes:
# 		#user_info
# 	#void:
# 		#sets user info
# 	def set_user(self,user_info):
# 		self.username=user_info['username']
# 		self.paths=user_info['paths']

# 	#takes:
# 		#username
# 	#void:
# 		#sets user data if username exists and correct credentials are provided
# 	def login(self,username):
# 		user_location=self.user_search(username)
# 		if(not user_location): return False
# 		user_data=self.user_load(user_location)
# 		verify_user=self.verify_user(user_data['mix'])
# 		if (not verify_user): return False
# 		self.set_user(user_data)

# 	def fork(self,command,sub_commands):
# 		if(command=='/login'):
# 			self.login(sub_commands)
# 			return True

class init:
	def __init__(self):
		pass

	username="Public@Krait: "

	curLoc=os.path.dirname(os.path.realpath(__file__))

	path=curLoc+'/bin:'+curLoc+'/applications'

class PyLine:
	def __init__(self):
		pass

	#takes:
		#user input
	#void:
		#recurs command line loop
	def prompt(self):
		self.stack(input(colored(init.username,'green')))
		self.prompt()

	#takes:
		#user input
	#returns:
		#command and sub commands
	def init(self,command):
		command=findall('[^\s]+',command)
		try:
			sub_commands=command[1:len(command)]
			command=command[0]
		except:
			return None
		return (command,sub_commands)

	#takes:
		#command
	#returns:
		#path to command if found
		#False if command is not found
	def find_command(self,command):
		paths=findall('[^\:]+',init.path)
		for directory in paths:
			commands=os.listdir(directory)
			for file in commands:
				if(file==command):
					return directory + '/' + command
		return False

	#takes:
		#command location
	#returns:
		#command source code
	def load_command(self,file):
		try:
			source=self.memory[file]
		except:
			source=open(file).read()
			self.malloc(file,source)
		return source

	#takes:
		#source code
	#void:
		#stores source according to memory available and request frequency
		#removes existing source according to memory available request frequency
	def malloc(self,file,source):
		return False
		self.memory.update({file:source})

	#takes:
		#command
		#sub command
	#void:
		#calls exec on command
	def execute(self,command,sub_commands):
		instructions={'PATH':init.path}
		for instr in range(len(sub_commands)):
			append={'param' + str(instr):sub_commands[instr]}
			instructions.update(append)	
		try:
			exec(command,instructions)
		except Exception as err:
			print(err)
		# print('Parameter requirements unfulfilled.')			

	#takes:
		#command
	#void:
		#executes commands
	def stack(self,random):
		init=self.init(random)
		if(not init): return None
		try:
			fork=user.fork(init[0],init[1][0])
			if(fork): return None
		except:
			pass
		locate_command=self.find_command(init[0])
		if(not locate_command): return print('Command not found.')
		command_source=self.load_command(locate_command)
		exe=self.execute(command_source,init[1])

krait=PyLine()
krait.prompt()