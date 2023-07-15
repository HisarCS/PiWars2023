from picamera import PiCamera
from picamera.array import PiRGBArray
from threading import Thread
from time import sleep


class HizlandirilmisPiKamera:

    def __init__(self, cozunurluk=(640, 480)):
        self.kamera = PiCamera()
        self.kamera.resolution = cozunurluk
        self.ham_kare = PiRGBArray(self.kamera, size=cozunurluk)
        self.suanki_kare = None
        self.onizleme_aktif = False

    def veri_okumaya_basla(self):
        Thread(target=self._kare_guncelle_, args=()).start()
        return self

    def _kare_guncelle_(self):
        for kare in self.kamera.capture_continuous(self.ham_kare, format="bgr", use_video_port=True):
            self.suanki_kare = kare.array
            self.ham_kare.truncate(0)

    def kareyi_oku(self):
        return self.suanki_kare

    def onizlemeyi_baslat(self):
        self.onizleme_aktif = True
        self.kamera.start_preview()

    def onizlemeyi_durdur(self):
        self.onizleme_aktif = False
        self.kamera.stop_preview()

    def kareyi_goster(self):
        if self.onizleme_aktif:
            self.kamera.preview(self.suanki_kare)

    def kapat(self):
        self.kamera.close()


k = HizlandirilmisPiKamera()
k.veri_okumaya_basla()
k.onizlemeyi_baslat()
sleep(15)
k.kapat()
