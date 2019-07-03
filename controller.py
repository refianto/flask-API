from flask import Flask, jsonify, request
import jwt

from model import *

app = Flask(__name__)
# app.config["APPLICATION_ROOT"] = "/api/v1"

@app.route('/login', methods=['POST'])
def hello_world():
	data = request.json
	# for user() in x:
	# 	if data['username'] == x[1] and data['password'] == x[2] :
	# 		result = {
	# 		"message" : "success",
	# 		"url" : "api/v1/login",
	# 		"data" : "token"
	# 		}
	# 	else:
	# 		result = {
	# 		"message" : "data not found"
	# 		}
	try:
		password = user(data['username'])
		if data['password'] == password[0][0] :
			sec = {
			"username" : data['username'],
			"password" : data['password']
			}

			token = jwt.encode(sec, 'secret', algorithm='HS256')
			
			response = {
			"message" : "success",
			"status" : "200",
			"data" : str(token)
			}
		else:
			response = {
			"message" : "data not found",
			"status" : "404"
			}
	except:
		response = {
		"message" : "data not found",
		"status" : "404"
		}

	return jsonify(response)



################### peminjam ############ 

@app.route('/peminjam', methods=['GET'])
def peminjam():

	dt = []
	for x in showPeminjam():
		dt.append({"id" : x[0], "nama_peminjam" : x[1]})

	response = {
	"message" : "successw",
	"status" : "200",
	"data" : dt
	}
	return jsonify(response)

@app.route('/peminjam/add', methods=['POST'])
def peminjamTambah():

	dt = request.json
	addPeminjam(dt['nama_peminjam'])

	response = {
	"message" : "success",
	"status" : "200",
	}

	return jsonify(response)

@app.route('/peminjam/edit', methods=['POST'])
def peminjamEdit():

	dt = request.json
	editPeminjam(dt['id'], dt['nama_peminjam'])

	response = {
	"message" : "success",
	"status" : "200",
	}
	return jsonify(response)
		
@app.route('/peminjam/delete/<id_peminjam>', methods=['GET'])
def peminjamDelete(id_peminjam):

	try:
		cekPeminjam(id_peminjam)			
	except:
		return jsonify({"message" : "ID not found"})

	deletePeminjam(id_peminjam)
	response = {
	"message" : "peminjam was deleted",
	"id peminjam" : id_peminjam
	}
	return jsonify(response)



############## buku ##################

@app.route('/buku', methods=['GET'])
def buku():

	dt = []
	for x in showBuku():
		dt.append({"id" : str(x[0]), "judul" : x[1]})
		
	result = {
	"message" : "success",
	"status" : "200",
	"data" : dt
	}
	return jsonify(result)

@app.route('/buku/add', methods=["POST"])
def bukuTambah():

	dt = request.json
	# q.execute("INSERT INTO buku (judul) VALUES (%s)", dt['namaBuku'])
	# mydb.commit()

	addBuku(dt['judul'])

	response = {
	"message" : "success",
	"status" : "200",
	"url" : "/api/v1/buku" 
	}

	return jsonify(response)

@app.route('/buku/edit', methods=["POST"])
def bukuEdit():

	dt = request.json
	editBuku(dt['id'], dt['judul'])

	response = {
	"message" : "success",
	"status" : "200"
	}

	return jsonify(response)

@app.route('/buku/delete/<id_buku>', methods=['GET'])
def bukuHapus(id_buku):

	try:
		cekBuku(id_buku)
	except:
		return jsonify({"message" : "ID not found"})

	deleteBuku(id_buku)
	response = {
	"message" : "buku was deleted",
	"id buku" : id_buku
	}

	return jsonify(response)

################ Peminjaman ################

@app.route('/peminjaman', methods=['GET'])
def peminjaman():

	# if not in cekPeminjam():
	# 	return jsonify({"message" : "ID peminjam not found"})
	# if not in cekBuku():
	# 	return jsonify({"message" : "ID buku not found"})

	dt = []
	for x in showPeminjaman():
		dt.append({"id" : x[0], "id_peminjam" : x[1], "id_peminjaman" : x[2]})

	response = {
	"message" : "success2",
	"status" : 200,
	"data" : dt
	}

	return jsonify(response)

@app.route('/peminjaman/add', methods=['POST'])
def peminjamanAdd():
	dt = request.json

	addPeminjaman(dt['id_peminjam'], dt['id_buku'])

	response = {
	"message" : "Peminjaman was added",
	"status" : 200,
	}
	return jsonify(response)

@app.route('/peminjaman/edit', methods=['POST'])
def peminjamanEdit():

	dt = request.json

	editPeminjaman(dt['id'], dt['id_peminjam'], dt['id_buku'])

	response = {
	"message" : "Peminjaman was edited",
	"status" : 200
	}
	return jsonify(response)

@app.route('/peminjaman/delete/<id_peminjaman>', methods=['GET'])
def peminjamanDelete(id_peminjaman):
	
	try:
		cekPeminjaman(id_peminjaman)
	except:
		return jsonify({"message" : "ID not found"})

	deletePeminjaman(id_peminjaman)

	response = {
	"message" : "Peminjaman was deleted",
	"status" : 200
	}
	return jsonify(response)

# -------------- Dbug Mode = ON ------------------
if __name__ == '__main__':
	app.run()