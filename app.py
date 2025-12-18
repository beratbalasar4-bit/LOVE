import streamlit as st
import time
import random
import os

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Sonsuz Aşkım ❤️", page_icon="🌹", layout="wide")

# --- TASARIM (CSS) ---
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(to top, #fad0c4 0%, #ffd1ff 100%);
    }
    h1 { color: #880E4F; font-family: 'Georgia', serif; text-align: center; }
    h2, h3 { color: #AD1457; font-family: 'Helvetica', sans-serif; text-align: center; }
    
    .ask-karti {
        background-color: rgba(255, 255, 255, 0.7);
        padding: 30px; border-radius: 20px;
        border: 2px solid #F8BBD0;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        font-size: 19px; color: #4A148C; font-family: 'Verdana', sans-serif;
    }
    img { border-radius: 15px; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# --- FOTOĞRAF KONTROL FONKSİYONU ---
def foto_goster(isim):
    uzantilar = [".jpg", ".png", ".jpeg"]
    for uzanti in uzantilar:
        yol = f"fotolar/{isim}{uzanti}"
        if os.path.exists(yol):
            st.image(yol, use_container_width=True)
            return True
    return False

# --- GİRİŞ EKRANI (DÜZELTİLDİ: FORM KULLANILDI) ---
SIFRE = "7 Aralık"

if 'giris' not in st.session_state:
    st.session_state['giris'] = False

if not st.session_state['giris']:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.title("🔒 Kalbimin Anahtarı")
    st.markdown("<center><h3>O gün hayatımın değiştiği gündü...</h3></center>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1,2,1])
    with c2:
        # BURASI DEĞİŞTİ: Artık form içindeyiz, yazı yazarken donmaz.
        with st.form("giris_formu"):
            sifre_giris = st.text_input("Şifre:", placeholder="Tarihimiz...", type="password")
            giris_butonu = st.form_submit_button("Giriş Yap ❤️")
            
            if giris_butonu:
                if sifre_giris.strip() == SIFRE:
                    st.session_state['giris'] = True
                    st.rerun()
                else:
                    st.error("Sadece ikimizin bildiği o tarih...")
    st.stop()

# --- ANA SAYFA ---

st.markdown('<iframe style="border-radius:12px" src="http://googleusercontent.com/spotify.com/2" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>', unsafe_allow_html=True)

if st.session_state['giris']: # Balonlar sadece giriş başarılı olunca ilk açılışta patlasın
    st.balloons()

st.title("❤️ İyi ki Varsın Sevgilim ❤️")
st.markdown("**Senin için hazırladığım bu küçük dünyaya hoş geldin...**")
st.divider()

tab1, tab2, tab3 = st.tabs(["📸 Bizim Hikayemiz", "💌 Sana Mektubum", "🎁 Aşk Çekleri"])

with tab1:
    st.header("Seninle Her Anım Mucize")
    col1, col2 = st.columns(2)
    with col1: foto_goster("biz1")
    with col2: foto_goster("biz2")
    st.markdown("<br>", unsafe_allow_html=True)
    col3, col4, col5 = st.columns(3)
    with col3: foto_goster("biz3")
    with col4: foto_goster("biz4")
    with col5: foto_goster("biz5")
    st.success("Birlikte daha nicelerine... 📸")

with tab2:
    st.header("💌 Kalbimden Gelenler...")
    mektup = """
    Canım Sevgilim, Hayatımın Anlamı...
    
    Seninle tanıştığımız o 7 Aralık günü, benim hayatım gerçekten başladı.
    Gülüşünle, bakışınla dünyamı aydınlattın. 
    
    Biliyorum, bazen seni istemeden de olsa kırabiliyorum, üzebiliyorum. 
    Belki sesim yükseliyor, belki düşüncesizlik ediyorum... 
    Bunlar için senden özür dilerim. Seni üzmek, dünyada isteyeceğim en son şey bile değil.
    
    Ama şunu bilmeni isterim ki; kalbimde, aklımda, ruhumda sadece SEN varsın.
    Seni o kadar çok seviyorum ki, bazen kelimeler yetersiz kalıyor.
    İyi ki hayatımdasın, iyi ki benimsin.
    
    Sonsuza kadar, sadece senin...
    - Berat
    """
    st.markdown(f'<div class="ask-karti">{mektup}</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Seni Seviyorum ❤️"):
        st.snow()
        time.sleep(1)
        st.success("Ben de seni her şeyden çok seviyorum! ❤️")

with tab3:
    st.header("🎁 Aşk Çekleri")
    st.write("Bu çeklerin son kullanma tarihi yok, istediğin zaman kullanabilirsin!")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("🎬 Film Gecesi (Seçim Senin)"):
            st.info("Kupon Onaylandı! Mısırları patlatıyorum, kumanda sende.")
    with c2:
        if st.button("💆‍♀️ Özel Masaj Hakkı"):
            st.success("Kupon Onaylandı! Günün tüm yorgunluğunu alacağım.")
    with c3:
        if st.button("🍔 Yemek Ismarlama"):
            st.warning("Kupon Onaylandı! Nereye dersen oraya gidiyoruz.")
