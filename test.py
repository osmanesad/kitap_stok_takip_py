try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    print("Kütüphaneler başarıyla yüklendi.")
except ImportError as e:
    print(f"Hata: {e}")
