import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class Kullanici:
    def __init__(self, ad, yas, cinsiyet):
        self.ad = ad
        self.yas = yas
        self.cinsiyet = cinsiyet
        self.saglik_kayitlari = []
        self.egzersizler = []

    def saglik_kaydi_ekle(self, kayit):
        self.saglik_kayitlari.append(kayit)

    def egzersiz_ekle(self, egzersiz):
        self.egzersizler.append(egzersiz)

class SaglikKaydi:
    def __init__(self, tarih, kilo, tansiyon):
        self.tarih = tarih
        self.kilo = kilo
        self.tansiyon = tansiyon

class Egzersiz:
    def __init__(self, ad, sure, tekrar):
        self.ad = ad
        self.sure = sure
        self.tekrar = tekrar

class SaglikTakipApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kişisel Sağlık Takip Uygulaması")

        self.kullanicilar = []

        tk.Label(root, text="Ad:").grid(row=0, column=0)
        self.entry_ad = tk.Entry(root)
        self.entry_ad.grid(row=0, column=1)

        tk.Label(root, text="Yaş:").grid(row=1, column=0)
        self.entry_yas = tk.Entry(root)
        self.entry_yas.grid(row=1, column=1)

        tk.Label(root, text="Cinsiyet:").grid(row=2, column=0)
        self.entry_cinsiyet = tk.Entry(root)
        self.entry_cinsiyet.grid(row=2, column=1)

        tk.Button(root, text="Kullanıcı Ekle", command=self.kullanici_ekle).grid(row=3, column=0, columnspan=2)

        self.listbox_kullanicilar = tk.Listbox(root, width=50)
        self.listbox_kullanicilar.grid(row=4, column=0, columnspan=2)

        tk.Label(root, text="Kilo:").grid(row=5, column=0)
        self.entry_kilo = tk.Entry(root)
        self.entry_kilo.grid(row=5, column=1)

        tk.Label(root, text="Tansiyon:").grid(row=6, column=0)
        self.entry_tansiyon = tk.Entry(root)
        self.entry_tansiyon.grid(row=6, column=1)

        tk.Button(root, text="Sağlık Kaydı Ekle", command=self.saglik_kaydi_ekle).grid(row=7, column=0, columnspan=2)

        tk.Label(root, text="Egzersiz Adı:").grid(row=8, column=0)
        self.entry_egzersiz_ad = tk.Entry(root)
        self.entry_egzersiz_ad.grid(row=8, column=1)

        tk.Label(root, text="Süre (dk):").grid(row=9, column=0)
        self.entry_sure = tk.Entry(root)
        self.entry_sure.grid(row=9, column=1)

        tk.Label(root, text="Tekrar:").grid(row=10, column=0)
        self.entry_tekrar = tk.Entry(root)
        self.entry_tekrar.grid(row=10, column=1)

        tk.Button(root, text="Egzersiz Ekle", command=self.egzersiz_ekle).grid(row=11, column=0, columnspan=2)

        tk.Button(root, text="Rapor Görüntüle", command=self.rapor_goster).grid(row=12, column=0, columnspan=2)

        self.listbox_rapor = tk.Listbox(root, width=80)
        self.listbox_rapor.grid(row=13, column=0, columnspan=2)

    def kullanici_ekle(self):
        ad = self.entry_ad.get()
        try:
            yas = int(self.entry_yas.get())
            cinsiyet = self.entry_cinsiyet.get()
            kullanici = Kullanici(ad, yas, cinsiyet)
            self.kullanicilar.append(kullanici)
            self.listbox_kullanicilar.insert(tk.END, f"{ad} - {yas} yaş - {cinsiyet}")
            messagebox.showinfo("Başarılı", "Kullanıcı eklendi.")
        except ValueError:
            messagebox.showerror("Hata", "Yaş bir sayı olmalıdır.")

    def saglik_kaydi_ekle(self):
        secili_index = self.listbox_kullanicilar.curselection()
        if not secili_index:
            messagebox.showerror("Hata", "Bir kullanıcı seçin.")
            return
        try:
            kilo = float(self.entry_kilo.get())
            tansiyon = self.entry_tansiyon.get()
            tarih = datetime.now()
            kayit = SaglikKaydi(tarih, kilo, tansiyon)
            kullanici = self.kullanicilar[secili_index[0]]
            kullanici.saglik_kaydi_ekle(kayit)
            messagebox.showinfo("Başarılı", "Sağlık kaydı eklendi.")
        except ValueError:
            messagebox.showerror("Hata", "Kilo bir sayı olmalıdır.")

    def egzersiz_ekle(self):
        secili_index = self.listbox_kullanicilar.curselection()
        if not secili_index:
            messagebox.showerror("Hata", "Bir kullanıcı seçin.")
            return
        try:
            ad = self.entry_egzersiz_ad.get()
            sure = int(self.entry_sure.get())
            tekrar = int(self.entry_tekrar.get())
            egzersiz = Egzersiz(ad, sure, tekrar)
            kullanici = self.kullanicilar[secili_index[0]]
            kullanici.egzersiz_ekle(egzersiz)
            messagebox.showinfo("Başarılı", "Egzersiz eklendi.")
        except ValueError:
            messagebox.showerror("Hata", "Süre ve tekrar sayıları sayı olmalıdır.")

    def rapor_goster(self):
        self.listbox_rapor.delete(0, tk.END)
        secili_index = self.listbox_kullanicilar.curselection()
        if not secili_index:
            messagebox.showerror("Hata", "Bir kullanıcı seçin.")
            return
        kullanici = self.kullanicilar[secili_index[0]]
        self.listbox_rapor.insert(tk.END, f"Kullanıcı: {kullanici.ad} ({kullanici.yas} yaş, {kullanici.cinsiyet})")
        self.listbox_rapor.insert(tk.END, "Sağlık Kayıtları:")
        for kayit in kullanici.saglik_kayitlari:
            self.listbox_rapor.insert(tk.END, f"{kayit.tarih.strftime('%d/%m/%Y %H:%M')} - Kilo: {kayit.kilo} kg - Tansiyon: {kayit.tansiyon}")
        self.listbox_rapor.insert(tk.END, "Egzersizler:")
        for egzersiz in kullanici.egzersizler:
            self.listbox_rapor.insert(tk.END, f"{egzersiz.ad} - Süre: {egzersiz.sure} dk - Tekrar: {egzersiz.tekrar}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SaglikTakipApp(root)
    root.mainloop()
