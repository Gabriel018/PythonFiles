import sqlite3

#
# connec = sqlite3.connect("banco.db")
#
# curs = connec.cursor()
#
#
# sql =  """
# CREATE TABLE usuario ( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#                        name TEXT NOT NULL,
#                        fone TEXT NOT NULL,
#                        email TEXT UNIQUE NOT NULL)
# """
# curs.execute(sql)
# connec.commit()
# curs.close()

# INSERIR DADOS

# connec = sqlite3.connect("banco.db")
#
# curs = connec.cursor()
#
# sql = """
#    INSERT INTO usuario(name,fone,email)
#    VALUES('Gabriel','11982983','duke@gmailcom')
# """
# curs.execute(sql)
# connec.commit()
# connec.close()

# def banco_insert(name,fone,email):
#  return """
#     INSERT INTO usuario(name,fone,email)
#     VALUES('{}','{}','{}')
#  """ .format(name, fone, email)

# def banco_updade(name,email):
#  return """
#     UPDATE usuario SET  name = '{}' WHERE email = '{}'
# """.format(name,email)

# def banco_delete(name):
#  return """
#      DELETE FROM usuario WHERE name='{}'
#  """.format(name)

def banco_info(date,field):
 return """
 SELECT name,fone,email FROM usuario WHERE '{}'='{}'
 
 """.format(field,date)

con = sqlite3.connect("banco.db")

curs = con.cursor()

curs.execute(banco_info('1','id'))
#con.commit()
date = curs.fetchall()
con.close()
