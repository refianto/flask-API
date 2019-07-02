import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="pos_perpus"
)
q = mydb.cursor()

def user(usr):
	q.execute("SELECT password FROM users where username = '"+usr+"'")
	result = q.fetchall()

	return result

#------------------- Buku ---------------------

def cekBuku(id):
	q.execute("SELECT `id_buku` FROM `buku`")
	id_buku = q.fetchall()

	return id_buku

def showBuku():
	q.execute("SELECT * FROM buku")
	result = q.fetchall()

	# d = []
	# for x in result:
	# 	d.append({"nama" : x[1]})

	# print(d)
	return result

def addBuku(judul):
	q.execute("INSERT INTO `buku` VALUES (NULL, '"+judul+"')")

	mydb.commit()

	return

def editBuku(id,judul):
	q.execute("UPDATE `buku` SET `judul` = '"+judul+"' WHERE `buku`.`id_buku` = "+id+";")
	mydb.commit()

	return

def deleteBuku(id):
	q.execute("DELETE FROM `buku` WHERE `buku`.`id_buku` = "+id+"")
	mydb.commit()

	return

#---------------------- Peminjaman --------------------

def cekBuku(id):
	q.execute("SELECT `id_peminjam` FROM `peminjam`")
	id_peminjam = q.fetchall()

	return id_peminjam

def showPeminjam():
	q.execute("SELECT * FROM `peminjam`")
	res = q.fetchall()

	return res

def addPeminjam(nama):
	q.execute("INSERT INTO `peminjam` VALUES (NULL, '"+nama+"');")
	mydb.commit()

	return

def editPeminjam(id, nama):
	q.execute("UPDATE `peminjam` SET `nama` = '"+nama+"' WHERE `peminjam`.`id_peminjam` = "+id+";")
	mydb.commit()
	return

def deletePeminjam(id):
	q.execute("DELETE FROM `peminjam` WHERE `peminjam`.`id_peminjam` = "+id+"")
	mydb.commit()
	return
# addBuku('komik')

# ------------------- Peminjaman --------------

def showPeminjaman():
	q.execute("SELECT * FROM `peminjaman`")
	res = q.fetchall()
	return res

def addPeminjaman(peminjam, peminjaman):
	q.execute("INSERT INTO `peminjaman` VALUES (NULL, '"+peminjam+"', '"+peminjaman+"');")
	mydb.commit()
	return

def editPeminjaman(id, peminjam, peminjaman):
	q.execute("UPDATE `peminjaman` SET `peminjam` = '"+peminjam+"', `di_pinjam` = '"+peminjaman+"' WHERE `peminjaman`.`id_peminjaman` = "+id+";")
	mydb.commit()
	return

def deletePeminjaman(id):
	q.execute("DELETE FROM `peminjaman` WHERE `peminjaman`.`id_peminjaman` = "+id+"")
	mydb.commit()
	return