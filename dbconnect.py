import MySQLdb

def connection():
	conn = MySQLdb.connect(host="localhost",
							user="root",
							passwd="365663",
							db="pythnflask") #you can connect remotely
	c = conn.cursor()

	return c, conn