from flask import Flask, render_template, request, redirect, url_for
import pymysql

application = Flask(__name__)

conn = cursor = None

# Fungsi koneksi database
def openDb():
    global conn, cursor
    conn = pymysql.connect(host="localhost", user="root", passwd="", database="perpus_1122102060")
    cursor = conn.cursor()

# Fungsi untuk menutup koneksi
def closeDb():
    global conn, cursor
    cursor.close()
    conn.close()

# Fungsi view index() untuk menampilkan data dari database
@application.route('/')
def index():
    openDb()
    container = []
    sql = "SELECT * FROM buku_1122102060"
    cursor.execute(sql)
    results = cursor.fetchall()
    for data in results:
        container.append(data)
    closeDb()
    return render_template('index.html', container=container)

# Fungsi view tambah() untuk membuat form tambah
@application.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        kode = request.form['Kode_Buku']
        nama_buku = request.form['Nama_Buku']
        penerbit = request.form['Penerbit']
        pengarang = request.form['Pengarang']
        jumlah = request.form['Jumlah_Buku']
        openDb()
        sql = "INSERT INTO buku_1122102060 (Kode_Buku, Nama_Buku, Penerbit, Pengarang, Jumlah_Buku) VALUES (%s, %s, %s, %s, %s)"
        val = (kode, nama_buku, penerbit, pengarang, jumlah)
        cursor.execute(sql, val)
        conn.commit()
        closeDb()
        return redirect(url_for('index'))
    else:
        return render_template('tambah.html')

# Fungsi view edit() untuk form edit
@application.route('/edit/<kode_buku>', methods=['GET', 'POST'])
def edit(kode_buku):
    openDb()
    cursor.execute('SELECT * FROM buku_1122102060 WHERE Kode_Buku=%s', (kode_buku))
    data = cursor.fetchone()
    if request.method == 'POST':
        kode = request.form['Kode_Buku']
        nama_buku = request.form['Nama_Buku']
        penerbit = request.form['Penerbit']
        pengarang = request.form['Pengarang']
        jumlah = request.form['Jumlah_Buku']
        sql = "UPDATE buku_1122102060 SET Kode_Buku=%s, Nama_Buku=%s, Penerbit=%s, Pengarang=%s, Jumlah_Buku=%s WHERE Kode_Buku=%s"
        val = (kode, nama_buku, penerbit, pengarang, jumlah, kode)
        cursor.execute(sql, val)
        conn.commit()
        closeDb()
        return redirect(url_for('index'))
    else:
        closeDb()
        return render_template('edit.html', data=data)

# Fungsi untuk menghapus data
@application.route('/hapus/<kode_buku>', methods=['GET', 'POST'])
def hapus(kode_buku):
    openDb()
    cursor.execute('DELETE FROM buku_1122102060 WHERE Kode_Buku=%s', (kode_buku,))
    conn.commit()
    closeDb()
    return redirect(url_for('index'))

if __name__ == '__main__':
    application.run(debug=True)
