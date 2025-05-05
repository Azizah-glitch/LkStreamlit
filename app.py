import streamlit as st

#Menambahkan judul
st.title("Welcome to Azizah Glitch's")

#menambahkan header
st.header('Introducing')
st.write('Halo! Nama saya Azizah. Ini adalah aplikasi Streamlit pertama saya. Saya berasal dari Selayar dan sedang belajar membuat aplikasi web dengan Python. Dalam apliaksi ini saya memposisikan diri sebagai boss dalam suatu usaha yang bergerak dibidang fashion. Dan berikutnya saya akan menampilkan data-data karyawan bohongan saya. Semoga kalian suka!!')

#Menambahkan subheader (tulisannya lebih kecil dari header)
st.subheader('The Data')

#Menambahkan caption (tulisan kecil yang tidak terlalu mencolok)
st.caption('Sesuai yang saya tulis di atas bahwa data ini tidak real.')

#Mendemonstrasikan kode
st.code('import streamlit as st')
st.text('Ini adalah teks penting yang harus di ketik untuk mendapatkan tampilan seperti yang tertera di layar anda.')

#Menampilkan rumus
st.latex(r' y = mx + b ')
st.text("Code yang dipakai untuk menampilkan rumus seperti di atas adalah (r' y = mx + b ')")

#Mengubah tebal, miring, gambar, tautan, and other
st.markdown('**Link** dan _link_ serta [Tautan](https://streamlit.io)')

#membuat garis horizontal untuk memisahkan materi atau apapun itu
st.divider()

import streamlit as st
import requests
import pandas as pd


data = {
    'Nama': ['Azizah', 'Selpy', 'Nadien'],
    'Usia': ['19', '19', '23'],
    'Asal Daerah': ['Selayar', 'Selayar', 'Palopo City']
}

df = pd.DataFrame(data)

#Menampilkan file metric
st.metric(label="Total Penjualan", value=2500, delta="+300")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Omset", value="Rp 200 juta", delta="+5%")
with col2:
    st.metric(label="User Aktif", value="1.250", delta="+2%")
with col3:
    st.metric(label="Refund", value="15", delta="-1%")

col1, col2 = st.columns(2)
st.divider()

#Menampilkan grafik
import numpy as np
import streamlit as st

#Line Chart
data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(data)

#Bar Chart
data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)

st.bar_chart(data)

#altair chart
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)

chart = alt.Chart(data.reset_index()).mark_line().encode(
    x='index',
    y='a'
)

st.altair_chart(chart, use_container_width=True)

#map
data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)

st.map()

#contoh mini semua input
import streamlit as st

with st.form("form_input"):
    nama = st.text_input("Nama")
    alamat = st.text_area("Alamat")
    usia = st.number_input("Usia", min_value=0)
    tanggal_lahir = st.date_input("Tanggal lahir")
    waktu_janji = st.time_input("Waktu Janjian")
    jenis_kelamin = st.radio("Jenis Kelamin", ("Pria", "Wanita"))
    hobi = st.multiselect("Hobi", ["Mambaca", "Olahraga", "Musik", "Traveling"])
    warna_favorit = st.color_picker("Pilih warna favourite")
    file_foto = st.file_uploader("Upload foto")
    foto_kamera = st.camera_input("Ambil foto dari kamera")
    rating = st.slider("Rating kepuasan", 1, 10)

    submitted = st.form_submit_button("Done Bro")

if submitted:
    st.success(f"Data {nama} berhasil dikirim!")
    st.write("### Rincian Data:")
    st.write(f"**Alamat:** {alamat}")
    st.write(f"**Usia:** {usia}")
    st.write(f"**Tanggal Lahir:** {tanggal_lahir}")
    st.write(f"**Waktu Janjian:** {waktu_janji}")
    st.write(f"**Jenis Kelamin:** {jenis_kelamin}")
    st.write(f"**Hobi:** {', '.join(hobi)}")
    st.write(f"**Warna Favorit:** {warna_favorit}")
    st.write(f"**Rating Kepuasan:** {rating}")
    if file_foto:
        st.image(file_foto, caption="Foto yang diunggah")
    if foto_kamera:
        st.image(foto_kamera, caption="Foto dari kamera")
#Menampilkan Gambar
import streamlit as st
from PIL import Image

st.image(
    "https://maukuliah.ap-south-1.linodeobjects.com/gallery/001036/Gedung%204%20UNM-thumbnail.jpg",
    caption="Fyi saya berkuliah di UNM",
    use_container_width=True
)


#Menampilkan video dari file lokal
st.video('video febi.mp4')

st.title("Data Karyawan")
st.dataframe(df)
