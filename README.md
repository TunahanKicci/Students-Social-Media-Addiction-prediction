
# 📱 Öğrenciler İçin Sosyal Medya Bağımlılık Analizi

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Machine Learning](https://img.shields.io/badge/Model-XGBoost%2FSklearn-green)
![Status](https://img.shields.io/badge/Status-Active-success)

Bu proje, öğrencilerin sosyal medya kullanım alışkanlıklarını, uyku düzenlerini ve ruh hallerini analiz ederek **Sosyal Medya Bağımlılık Seviyesini (2-9 Skalası)** tahmin eden bir makine öğrenmesi uygulamasıdır.

## 🚀 Canlı Demo

Uygulamayı tarayıcınızda hemen deneyebilirsiniz:

👉 **[Uygulamaya Git: Social Media Addiction Predictor](https://students-social-media-addiction-prediction.streamlit.app)**

> **Not:** Uygulama ücretsiz sunucularda barındırıldığı için "Uyku Modu"na geçmiş olabilir. Linke tıkladığınızda açılması 20-30 saniye sürebilir, lütfen bekleyiniz. ⏳

---

##  Proje Hakkında

Günümüzde sosyal medya bağımlılığı, özellikle öğrenciler arasında akademik başarıyı ve ruh sağlığını etkileyen önemli bir faktördür. Bu proje, makine öğrenmesi algoritmalarını kullanarak bu riski ölçmeyi ve farkındalık yaratmayı amaçlar.


---

## 🛠️ Kurulum ve Yerel Çalıştırma (Local)

Bu projeyi kendi bilgisayarınızda çalıştırmak isterseniz aşağıdaki adımları izleyin:

### 1. Repoyu Klonlayın
```bash
git clone [https://github.com/TunahanKicci/Students-Social-Media-Addiction-prediction.git](https://github.com/TunahanKicci/Students-Social-Media-Addiction-prediction.git)
cd Students-Social-Media-Addiction-prediction

```

### 2. Gerekli Kütüphaneleri Yükleyin

```bash
pip install -r requirements.txt

```

### 3. Uygulamayı Başlatın

```bash
streamlit run app.py

```

Tarayıcınızda otomatik olarak `http://localhost:8501` adresi açılacaktır.

---

## 📂 Proje Yapısı

```
├── app.py                            # Ana uygulama dosyası (Streamlit arayüzü)
├── social_media_addiction_model.pkl  # Eğitilmiş Makine Öğrenmesi Modeli
├── requirements.txt                  # Gerekli Python kütüphaneleri
├── README.md                         # Proje dokümantasyonu
└── .gitignore                        # Gereksiz dosyaları gizleme

```

---

## 📊 Sonuçların Yorumlanması

Model, veri setindeki dağılıma dayanarak **2 ile 9 arasında** bir skor üretir:

| Skor | Risk Seviyesi | Açıklama |
| --- | --- | --- |
| **2 - 5** | ✅ **Düşük/Orta Risk** | Kullanım alışkanlıklarınız sağlıklı veya kontrol altında. |
| **5 - 7** | ⚠️ **Yüksek Risk** | Sosyal medya hayatınızı etkilemeye başlamış, dikkatli olunmalı. |
| **7 - 9** | 🚨 **KRİTİK SEVİYE** | Ciddi bağımlılık belirtileri. Dijital detoks önerilir. |

---

## 👨‍💻 Geliştirici

**Tunahan Kıççı**


---

⭐ *Bu projeyi beğendiyseniz sağ üstten "Star" vermeyi unutmayın!*

