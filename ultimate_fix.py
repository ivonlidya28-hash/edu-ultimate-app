import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time
from datetime import datetime
import pywhatkit as kit  # Library WA Asli
import webbrowser

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="EduSuper Ultimate Real", layout="wide", page_icon="🔮")

# --- 2. CSS EKSTREM (UNGU CERAH & TEKS PUTIH) ---
st.markdown("""
<style>
    /* BACKGROUND: Ungu Cerah Futuristik */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
    /* TEXT COLOR: Memaksa SEMUA teks jadi Putih */
    h1, h2, h3, h4, h5, h6, p, span, label, .stMarkdown, div {
        color: #ffffff !important;
        font-family: 'Roboto', sans-serif;
    }
    
    /* SIDEBAR: Gelap Transparan agar menu terlihat */
    section[data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.6);
        border-right: 1px solid rgba(255,255,255,0.3);
    }
    
    /* KARTU METRIC: Putih Transparan Kaca */
    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 15px;
        padding: 15px;
    }
    /* Angka di dalam Metric */
    div[data-testid="stMetricValue"] {
        text-shadow: 0px 0px 10px rgba(255,255,255,0.8);
        font-size: 30px !important;
    }
    
    /* TABEL (DATAFRAME): Agar tulisan tabel terbaca */
    div[data-testid="stDataFrame"] {
        background-color: rgba(255,255,255, 0.9); 
        border-radius: 10px;
        padding: 5px;
    }
    /* Teks dalam tabel kita biarkan hitam agar kontras dengan background putih tabel */
    div[data-testid="stDataFrame"] div, div[data-testid="stDataFrame"] span {
        color: #333 !important; 
    }

    /* TOMBOL */
    .stButton>button {
        background: linear-gradient(90deg, #00d2ff 0%, #3a7bd5 100%);
        color: white !important;
        border: none;
        border-radius: 25px;
        font-weight: bold;
        padding: 10px 20px;
        box-shadow: 0px 5px 15px rgba(0,0,0,0.3);
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0px 0px 20px #00d2ff;
    }
    
    /* INPUT FIELDS */
    .stTextInput input, .stNumberInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        background-color: rgba(255,255,255,0.2) !important;
        color: white !important;
        border: 1px solid rgba(255,255,255,0.5);
    }
    /* Dropdown options text fix */
    ul[data-testid="stSelectboxVirtualDropdown"] li {
        color: black !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. DATA DUMMY ---
if 'data_siswa' not in st.session_state:
    np.random.seed(42)
    df = pd.DataFrame({
        'Nama': [f'Siswa {i}' for i in range(1, 101)],
        'Kelas': np.random.choice(['X-A', 'X-B', 'XI-IPA', 'XI-IPS', 'XII-IPA'], 100),
        'XP_Level': np.random.randint(1000, 5000, 100), # Untuk Gamifikasi
        'Kesehatan': np.random.choice(['Sehat', 'Sakit Ringan', 'Perlu UKS'], 100, p=[0.8, 0.15, 0.05]),
        'Tugas_Pending': np.random.randint(0, 5, 100),
        # Default nomor dummy. Nanti diedit user ke nomor asli saat mau kirim
        'No_WA': [f'+628{np.random.randint(10000000, 99999999)}' for _ in range(100)]
    })
    st.session_state['data_siswa'] = df

# --- 4. SIDEBAR MENU CANGGIH (8 MENU) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=120)
    st.title("EDU-ULTIMATE")
    st.caption("System v5.0 | Real WA Engine")
    
    menu = st.radio(
        "NAVIGASI MODUL:",
        [
            "🏠 Dashboard Utama",
            "📱 WhatsApp Auto-Bot (Real)",  # FITUR YANG DIUPDATE
            "🎮 Gamifikasi Siswa",    
            "👁️ AI CCTV Monitor",     
            "📚 Smart Library",       
            "🏥 Pantauan Kesehatan",  
            "👥 Database Siswa",
            "⚙️ Pengaturan"
        ]
    )

# --- 5. LOGIKA MODUL ---

# === MODUL 1: DASHBOARD UTAMA ===
if menu == "🏠 Dashboard Utama":
    st.title("🔮 Command Center Sekolah")
    st.markdown("Pantauan real-time seluruh aktivitas akademik.")
    
    # Metrics
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Siswa", "100", "Online")
    c2.metric("Tugas Terkumpul", "85%", "+12%")
    c3.metric("Bot WA Terkirim", "12", "Pesan Asli")
    c4.metric("Status Server", "Aktif", "Ping: 12ms")
    
    st.markdown("---")
    
    # Grafik Canggih: Radar Chart & 3D
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("🕸️ Radar Kompetensi Siswa")
        categories = ['Sains', 'Matematika', 'Seni', 'Olahraga', 'Disiplin']
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
              r=[80, 75, 90, 85, 70], theta=categories, fill='toself', name='Kelas X', line_color='#00d2ff'
        ))
        fig.add_trace(go.Scatterpolar(
              r=[60, 90, 65, 95, 80], theta=categories, fill='toself', name='Kelas XI', line_color='#ff00cc'
        ))
        fig.update_layout(
          polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
          showlegend=True, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="white")
        )
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.subheader("🧊 Sebaran 3D Akademik")
        df = st.session_state['data_siswa']
        fig_3d = px.scatter_3d(df, x='XP_Level', y='Tugas_Pending', z=df.index,
                               color='Kelas', opacity=0.8, size_max=10,
                               color_discrete_sequence=px.colors.qualitative.Bold)
        fig_3d.update_layout(paper_bgcolor='rgba(0,0,0,0)', font=dict(color="white"), 
                             scene=dict(xaxis=dict(backgroundcolor="rgba(0,0,0,0)"),
                                        yaxis=dict(backgroundcolor="rgba(0,0,0,0)"),
                                        zaxis=dict(backgroundcolor="rgba(0,0,0,0)")))
        st.plotly_chart(fig_3d, use_container_width=True)

# === MODUL 2: WHATSAPP AUTO-BOT (REAL SEND) ===
elif menu == "📱 WhatsApp Auto-Bot (Real)":
    st.title("📱 WhatsApp Direct Sender")
    st.warning("⚠️ SYARAT: Pastikan WhatsApp Web sudah login di browser Anda. Jangan gerakkan mouse saat proses pengiriman.")
    
    st.markdown("### 1. Target Siswa")
    df = st.session_state['data_siswa']
    
    # Filter siswa yang punya tugas pending
    siswa_bermasalah = df[df['Tugas_Pending'] > 0]['Nama'].tolist()
    
    col_input, col_action = st.columns([1, 1])
    
    with col_input:
        # Dropdown memilih siswa
        siswa_terpilih = st.selectbox("Pilih Siswa Bermasalah:", siswa_bermasalah)
        
        # Ambil data siswa tersebut
        data_target = df[df['Nama'] == siswa_terpilih].iloc[0]
        jumlah_tugas = data_target['Tugas_Pending']
        
        st.markdown(f"**Info Siswa:** {siswa_terpilih} (Tunggakan: {jumlah_tugas} Tugas)")
        
        # Input Nomor WA (Bisa diedit user sebelum kirim untuk memastikan benar)
        no_target = st.text_input("Pastikan Nomor WA Siswa (+62):", value=data_target['No_WA'])
        
        # Template Pesan
        pesan_default = f"Halo {siswa_terpilih}, Sistem Sekolah mengingatkan ada {jumlah_tugas} tugas yang belum kamu selesaikan. Mohon segera dikerjakan minggu ini. Semangat!"
        isi_pesan = st.text_area("Isi Pesan Otomatis:", value=pesan_default, height=100)

    with col_action:
        st.markdown("### 2. Eksekusi")
        st.info("Sistem akan membuka browser dan mengirim pesan secara otomatis.")
        
        if st.button("🚀 KIRIM PESAN SEKARANG (NYATA)"):
            if len(no_target) < 10 or "+62" not in no_target:
                st.error("❌ Nomor WA tidak valid! Harus diawali +62")
            else:
                with st.spinner("⏳ Sedang menghubungkan ke WhatsApp Server..."):
                    try:
                        # LOGIC NYATA MENGGUNAKAN PYWHATKIT
                        # wait_time = waktu loading WA Web (detik)
                        kit.sendwhatmsg_instantly(no_target, isi_pesan, wait_time=15, tab_close=True)
                        st.success(f"✅ Pesan berhasil dikirim ke {siswa_terpilih}!")
                        st.balloons()
                    except Exception as e:
                        st.error(f"Gagal mengirim: {e}")
                        st.markdown("Tips: Pastikan koneksi internet stabil dan WA Web terbuka.")

# === MODUL 3: GAMIFIKASI SISWA ===
elif menu == "🎮 Gamifikasi Siswa":
    st.title("🎮 Student Leaderboard (XP System)")
    st.markdown("Siswa mendapatkan **XP (Experience Points)** jika mengerjakan tugas.")
    
    df = st.session_state['data_siswa'].sort_values(by='XP_Level', ascending=False).head(10)
    
    # Top 3 Podium
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/179/179249.png", width=80)
        st.markdown(f"<h3 style='text-align: center; color: gold !important'>JUARA 1<br>{df.iloc[0]['Nama']}</h3>", unsafe_allow_html=True)
        st.metric("XP Tertinggi", f"{df.iloc[0]['XP_Level']} XP")
        
    with col1:
        st.markdown(f"<h4 style='text-align: center; color: silver !important'>Juara 2<br>{df.iloc[1]['Nama']}</h4>", unsafe_allow_html=True)
        st.metric("XP", f"{df.iloc[1]['XP_Level']}")
        
    with col3:
        st.markdown(f"<h4 style='text-align: center; color: #cd7f32 !important'>Juara 3<br>{df.iloc[2]['Nama']}</h4>", unsafe_allow_html=True)
        st.metric("XP", f"{df.iloc[2]['XP_Level']}")

    st.markdown("### 🏆 Peringkat 10 Besar")
    fig = px.bar(df, x='XP_Level', y='Nama', orientation='h', color='XP_Level', 
                 color_continuous_scale='Viridis')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="white"))
    st.plotly_chart(fig, use_container_width=True)

# === MODUL 4: AI CCTV MONITOR ===
elif menu == "👁️ AI CCTV Monitor":
    st.title("👁️ AI Computer Vision Monitor")
    st.warning("Sistem mendeteksi aktivitas mencurigakan di area sekolah.")
    
    c1, c2, c3 = st.columns(3)
    
    # Simulasi Kamera
    with c1:
        st.markdown("#### 📷 Gerbang Depan")
        st.image("https://media.istockphoto.com/id/1154943776/photo/pupils-walking-down-hallway-at-busy-break-time.jpg?s=612x612&w=0&k=20&c=yqXjD6rK_qYqJq0rJq0rJq0rJq0rJq0rJq0rJq0r", caption="Status: AMAN")
    with c2:
        st.markdown("#### 📷 Kantin")
        st.image("https://media.istockphoto.com/id/1326125872/photo/high-school-students-eating-lunch-in-cafeteria.jpg?s=612x612&w=0&k=20&c=Jq0rJq0rJq0rJq0rJq0rJq0rJq0rJq0rJq0rJq0r", caption="Status: RAMAI")
    with c3:
        st.markdown("#### 📊 AI Analysis")
        st.metric("Deteksi Wajah", "124 Orang")
        st.metric("Pelanggaran Seragam", "3 Terdeteksi", delta_color="inverse")

# === MODUL 5: SMART LIBRARY ===
elif menu == "📚 Smart Library":
    st.title("📚 Perpustakaan Digital")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Peminjaman Buku Populer")
        labels = ['Novel Fiksi', 'Buku Paket Sains', 'Komik Edukasi', 'Majalah', 'Ensiklopedia']
        values = [450, 250, 105, 50, 90]
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4)])
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font=dict(color="white"))
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.markdown("### Status Pengembalian")
        st.info("ℹ️ 5 Siswa terlambat mengembalikan buku.")
        st.button("Ingatkan via WA")

# === MODUL 6: PANTAUAN KESEHATAN ===
elif menu == "🏥 Pantauan Kesehatan":
    st.title("🏥 UKS & Kesehatan Siswa")
    
    df = st.session_state['data_siswa']
    sakit = df[df['Kesehatan'] != 'Sehat']
    
    st.markdown(f"### Hari ini ada {len(sakit)} siswa yang melapor sakit.")
    fig = px.histogram(df, x="Kesehatan", color="Kesehatan", 
                       color_discrete_map={"Sehat":"green", "Sakit Ringan":"orange", "Perlu UKS":"red"})
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="white"))
    st.plotly_chart(fig, use_container_width=True)

# === MODUL 7: DATABASE SISWA ===
elif menu == "👥 Database Siswa":
    st.title("👥 Database Induk Siswa")
    st.markdown("Edit Nomor WA Siswa di sini agar fitur otomatis berjalan lancar.")
    edited = st.data_editor(st.session_state['data_siswa'], num_rows="dynamic", use_container_width=True)
    st.session_state['data_siswa'] = edited

elif menu == "⚙️ Pengaturan":
    st.title("⚙️ System Settings")
    st.write("Versi Aplikasi: 5.0 Ultimate Real")
    st.toggle("Aktifkan Mode Hemat Daya")
    st.toggle("Notifikasi Suara")
