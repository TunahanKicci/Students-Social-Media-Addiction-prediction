import streamlit as st
import pandas as pd
import numpy as np
import joblib

# === 1. MODEL YÜKLEME ===
@st.cache_resource
def load_model():
    model = joblib.load('social_media_addiction_model.pkl')
    return model

model = load_model()

expected_columns = [
    'Age', 'Avg_Daily_Usage_Hours', 'Sleep_Hours_Per_Night', 'Mental_Health_Score',
    'Conflicts_Over_Social_Media', 'Awake_Usage_Rate', 'Conflict_Per_Hour',
    'Gender_Female', 'Academic_Level_encoded', 'Affects_Academic_Performance_No',
    'Relationship_Status_Single', 'Most_Used_Platform_Facebook',
    'Most_Used_Platform_Instagram', 'Most_Used_Platform_KakaoTalk',
    'Most_Used_Platform_LINE', 'Most_Used_Platform_LinkedIn',
    'Most_Used_Platform_Snapchat', 'Most_Used_Platform_TikTok',
    'Most_Used_Platform_Twitter', 'Most_Used_Platform_VKontakte',
    'Most_Used_Platform_WeChat', 'Most_Used_Platform_WhatsApp',
    'Most_Used_Platform_YouTube', 'Country_Denmark', 'Country_France',
    'Country_India', 'Country_Ireland', 'Country_Mexico', 'Country_Other',
    'Country_Spain', 'Country_Switzerland', 'Country_Turkey', 'Country_USA'
]

# === 2. ARAYÜZ AYARLARI ===
st.set_page_config(page_title="Sosyal Medya Bağımlılık Testi", page_icon="📱")
st.title("📱 Sosyal Medya Bağımlılık Analizi")
st.markdown("Veri setine dayalı yapay zeka tahmini (Skala: 2-9)")

st.sidebar.header("Profil Bilgileri")

def get_user_input():
    age = st.sidebar.slider("Yaş", 15, 45, 21)
    
    daily_usage = st.sidebar.slider("Günlük Kullanım (Saat)", 1.0, 10.0, 4.5)
    
    sleep = st.sidebar.slider("Uyku Süresi (Saat)", 3.0, 10.0, 7.0)
    
    mental_health = st.sidebar.slider("Ruh Hali Puanı (4-9)", 4, 9, 6, help="Yüksek puan = İyi Ruh Hali")
    
    conflicts = st.sidebar.selectbox("Sosyal Medya Yüzünden Kaç Kere Tartıştınız?", [0, 1, 2, 3, 4, 5])
    
    # Kategorik Değişkenler
    gender = st.sidebar.radio("Cinsiyet", ["Erkek", "Kadın"])
    
    # Veri setindeki dağılıma göre: 0=High School, 1=Undergraduate, 2=Graduate
    academic = st.sidebar.selectbox("Akademik Seviye", 
                                    ["High School", "Undergraduate", "Graduate"])
    
    affects_academic = st.sidebar.radio("Derslerini Olumsuz Etkiliyor mu?", ["Evet", "Hayır"])
    
    relationship = st.sidebar.radio("İlişki Durumu", ["İlişkisi Var/Evli", "Bekar (Single)"])
    
    # Veri setindeki tam platform listesi
    platform = st.sidebar.selectbox("En Çok Kullanılan Platform", 
                                    ["Facebook", "Instagram", "KakaoTalk", "LINE", "LinkedIn", 
                                     "Snapchat", "TikTok", "Twitter", "VKontakte", "WeChat", 
                                     "WhatsApp", "YouTube"])
    
    # Veri setindeki tam ülke listesi
    country = st.sidebar.selectbox("Ülke", 
                                   ["Denmark", "France", "India", "Ireland", "Mexico", 
                                    "Other", "Spain", "Switzerland", "Turkey", "USA"])

    return {
        "age": age, "usage": daily_usage, "sleep": sleep, "mental": mental_health,
        "conflicts": conflicts, "gender": gender, "academic": academic,
        "affects": affects_academic, "relation": relationship,
        "platform": platform, "country": country
    }

user_data = get_user_input()

# === 3. VERİ İŞLEME VE TAHMİN ===
if st.button("Analiz Et 🚀"):
    
    # Beklenen tüm sütunları 0 (veya False) olarak başlat
    input_data = {col: 0 for col in expected_columns}
    
    # --- A. Temel Değişkenler ---
    input_data['Age'] = user_data['age']
    input_data['Avg_Daily_Usage_Hours'] = user_data['usage']
    input_data['Sleep_Hours_Per_Night'] = user_data['sleep']
    input_data['Mental_Health_Score'] = user_data['mental']
    input_data['Conflicts_Over_Social_Media'] = user_data['conflicts']
    
    # --- B. Feature Engineering (Türetilmiş Özellikler) ---
    # 1. Awake_Usage_Rate (Uyanık kalınan sürenin ne kadarı ekran?)
    awake_hours = 24 - user_data['sleep']
    if awake_hours > 0:
        input_data['Awake_Usage_Rate'] = user_data['usage'] / awake_hours
    
    # 2. Conflict_Per_Hour (Saat başına düşen tartışma)
    if user_data['usage'] > 0:
        input_data['Conflict_Per_Hour'] = user_data['conflicts'] / user_data['usage']
    
    # --- C. Boolean/Binary Değişkenler ---
    # Cinsiyet (Kadınsa 1, Erkekse 0)
    input_data['Gender_Female'] = 1 if user_data['gender'] == "Kadın" else 0
    
    # Akademik Etki (Hayır dediyse 1 - Sütun adı Affects..._No)
    input_data['Affects_Academic_Performance_No'] = 1 if user_data['affects'] == "Hayır" else 0
    
    # İlişki (Bekar dediyse 1)
    input_data['Relationship_Status_Single'] = 1 if user_data['relation'] == "Bekar (Single)" else 0
    
    # --- D. Label Encoding (Akademik Seviye) ---
    # Veri setindeki dağılıma göre eşleştirme
    academic_map = {
        "High School": 0,
        "Undergraduate": 1,
        "Graduate": 2
    }
    input_data['Academic_Level_encoded'] = academic_map[user_data['academic']]
    
    # --- E. One-Hot Encoding (Platform ve Ülke) ---
    # Platformu bul ve 1 yap
    plat_col = f"Most_Used_Platform_{user_data['platform']}"
    if plat_col in input_data:
        input_data[plat_col] = 1
        
    # Ülkeyi bul ve 1 yap
    country_col = f"Country_{user_data['country']}"
    if country_col in input_data:
        input_data[country_col] = 1

    # === 4. SONUÇ GÖSTERİMİ ===
    # DataFrame oluştur ve sütun sırasını garantiye al
    df_input = pd.DataFrame([input_data])
    df_input = df_input.reindex(columns=expected_columns, fill_value=0)
    
    try:
        prediction = model.predict(df_input)[0]
        score = round(prediction, 2)
        
        st.divider()
        # Skoru olduğu gibi göster (2-9 Arası)
        st.metric(label="Bağımlılık Skoru (2-9 Arası)", value=f"{score}")
        
        # Yorumlama (Veri setindeki dağılıma göre)
        # 2-5: Düşük/Orta
        # 5-7: Yüksek
        # 7-9: Kritik/Bağımlı
        
        if score <= 5:
            st.success("✅ **Düşük/Orta Risk:** Durumunuz kontrol altında görünüyor.")
        elif score <= 7:
            st.warning("⚠️ **Yüksek Risk:** Sosyal medya hayatınızı etkilemeye başlamış.")
        else:
            st.error("🚨 **KRİTİK SEVİYE:** Bağımlılık belirtileri çok güçlü. (Skor: 7+)")
            st.write("Veri setimizde 7 ve üzeri puan alanlar, en bağımlı grubu oluşturmaktadır.")
            
    except Exception as e:
        st.error(f"Hata: {e}")