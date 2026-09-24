# Üstad Kenan Kuzucu — Kişisel Portfolyo Sitesi

Tek dosyalık (single-file) kişisel biyografi / portfolyo sitesi. `index.html` içinde CSS ve JS gömülüdür;
internet olmadan (Google Fonts dışında) açılır, sunucu/kurulum gerektirmez.

## Bölümler (12 panel)
Hakkında (biyografi) · İstatistikler · Beceriler · Teknoloji · Eserler · Sertifikalar · Eğitim ·
Zaman Çizelgesi · Sinema · Felsefe · Alıntı · İletişim

## Öne çıkanlar
- Hakkında panelinde portre fotoğrafı **tam boy** gösterilir (kırpma yok, `object-fit:contain`),
  konik gradyan çerçeve + simetrik köşe süsleri + isim plaketi + 5 simge şeridi.
- Canvas parçacık ağı, düşen yapraklar, yıldızlar, özel imleç (nokta + halka + ışıma), tıklama dalgası,
  kaydırma ilerleme çubuğu, 3D tel-kafes küp, kartlarda 3D eğilme, istatistik sayaçları.
- Yazılar WCAG kontrast eşiğinin üstünde (en düşük 5.16; hedef 4.5).
- Telefonda sol menü ☰ düğmesiyle açılır (`@media max-width:900px`).

## Dosyalar
- `index.html` — sitenin tamamı (766+ satır, gömülü CSS/JS)
- `profil.jpg` — portre fotoğrafı (928x1152)
- `ekran/` — teslim kanıtı ekran görüntüleri (12 panel + üst şerit, masaüstü/mobil)

## Açma
`index.html` dosyasına çift tıkla. Yayına almak için: klasörü bir web sunucusuna/alt klasöre kopyala.

---
Bu depo **özel (private)** tutulur; portre fotoğrafı ve kişisel bilgiler içerdiği için herkese açık değildir.
