# PiWars2023
Bu python kütüphanesi, HisarCS tarafınndan hazırlanan PiWars Türkiye 2023 robot kitlerindeki ultrasonik mesafe sensörü, pololu-drv8835 ve kamera gibi parçaların kullanımlarını kolaylaştırmak amacıyla yapılmıştır.

## Library'yi İndirme
Github'dan Pi23 library'sini indirmek de mümkün.
```bash git clone https://github.com/HisarCS/Pi20.git
$ git clone https://github.com/HisarCS/PiWars2023.git
$ cd Pi23
$ sudo python setup.py install
```
Burada komutları terminale kopyalayarak Pi23 kütüphanesini kullanmak mümkğn
git clone kütüphaneyi Raspi 4'ünüze indirirken
cd Pi23 bu dosyaya erişip içinde dosyaları import etmeniz ve kullanmanızı sağlar
sudo python setup.py install ise kütüphanenin setup kısmını halleden komuttur

## Ultrasonik_S
Ultrasonik_S sınıfı GPIO modu olarak BCM kullanır

**Fonksiyonlar**

```python

OlcmeyeBasla()

```

Arka planda ultrasonik sensörü aktif hale getirir.

```python

Oku()

```
Arka planda aktif hale getirilen sensörün ölçtüğü mesafeyi geri verir.

**Ultrasonik Örnek Kullanım**
```python
from time import sleep


sensor = Ultrasonik_S(20,21)
sensor.OlcmeyeBasla()

while True:
    anlikDeger = sensor.Oku()
    print(anlikDeger)
    sleep(0.1)

```
```sensor``` nesnesini oluştururken kullandığımız ```Ultrasonik_S(20,21)```, nesenenin ultrasonik sensör olduğunu belirtir ve parantez içindeki kısım (constructor) ise ultrasonik sensörun hangi GPIO numaralı pine takılı olduğununu gösterir. Daha sonrasında ise ```OlcmeyeBasla()``` komutu ile arka planda aktif hale getirdiğimiz sensör ```whlie True``` loopu ile ölçtüğü mesafeyi 0.1 saniye aralıklarla ekrana basar.


## HizlandirilmisPiKamera

**Fonksiyonlar**

```python

veri_okumaya_basla()

```
Ayrı bir thread oluşturarak kamera ile veri okumaya başlar.


```python

onizlemeyi_baslat()

```
Kameranın ön izlemesini başlatır.
```python

onizlemeyi_durdur()

```
Kameranın ön izlemesini durdurur.

```python

kapat()

```
Kamerayı kapatır.



**HizlandirilmisPiKamera Örnek Kullanım**
```python
from time import sleep

k = HizlandirilmisPiKamera()
k.veri_okumaya_basla()
k.onizlemeyi_baslat()
k.resize(240, 240)
while True:
	k.kareyi_goster()
	

```
Bu kod Picamera'nın preview'ını gösterir ve bu imageları boyutunu küçülterek ekran boyutuna uygun hale getirir.

## Motor
**Fonksiyonlar**
```python

hiz(hizsag,hizSol)

```
Pololu-drv8835'in kütüphanesini kullanarak her iki motorun da hızını ayarlar. Hız -480 ile 480 arasında atanabilir. Pozitif değerler ileriyi, negatif değerler de geriyi temsil eder. ```sagHiz``` pololu üzerinde birinci motora, ```solHiz``` ise ikinci motora denk gelir.

```python

sagHiz()
solHiz()
```
```hiz``` fonksiyonu gibi Pololu-drv8835'in kütüphanesini kullanır. ```hiz``` fonksiyonundan farklı olarak bu iki fonksiyon sadece tek bir motora (sağ veya sol) hız değeri atanmasına olanak sunar.
```python
ktm()
```

**Değer Vererek Motor Döndürme**
```python
from time import sleep


m = Motor()

while True:
  
    m.hiz(200,200)
    sleep(3)
    m.solHiz(200)
    sleep(5)
    m.solHiz(-247)
    sleep(5)
```
**Kumanda Verisiyle Motor Döndürme**
```python
motorlar = Motor()

joystik = Kumanda()
joystik.dinlemeyeBasla()

while True:
	lx, ly = joystik.sol()
	sagHiz, solHiz = motorlar.ktm(lx, ly)

	motorlar.hiz(sagHiz, solHiz)
```

Kumanda'nın sol joystick axis'lerinden veri alarak bu verileri motorr verisine çevirir ve motorlar kumanda verisine göre güçte gider

## Servo
Servo sınıfı GPIO modu olarak BCM kullanır

**Fonksiyonlar**
```python
surekliDonme()
```
Servoyu sürekli dönmeye ayarlar.
```python
secilenAci()
```
Servoyu tek bir açıya dönmeye ayarlar.
```python
aciAyarla(aci)
```
İstenilen açı değerini belirtir.
```python
uyu()
```
Tüm aktiviteyi durdurur.

**Açı Değeri Vererek Servo Döndürme**
```python
from time import sleep

servo = Servo()
servo.secilenAci()
while True:
	secilenAci(0)
	sleep(1)
	secilenAci(180)
	sleep(1)
```
Bu kod servonun set edilen iki açı arasında sürekli gidip gelmesini sağlar.

**Sürekli Servo Döndürme**
```python
from time import sleep

servo = Servo()
servo.surekliDonme()

aci = 0
ekle = 0

while True:
	servo.aciAyarla(aci)

	if(aci == 180):
		ekle = -1
	elif(aci == 0):
		ekle = 1
	aci += ekle
	sleep(0.05)

```
Bu kod servonun sürekli dönmesini sağlar.

## Kumanda


**Fonksiyonlar**
```python
dinlemeyeBasla()
```
Kumanda'dan arkada veri almaya başlamasını sağlar.
```python
sol()
```
Sol joystick verilerini okur.
```python
sağ()
```
Sağ joystick verilerini okur.
```python
butonlar()
```
Buton verilerini okur.
```python
oku()
```
Tüm verileri okur.

**Kumanda Örnek Kullanım**
```python
joystik = Kumanda()
joystik.dinlemeyeBasla()

while True:
	lx, ly = joystik.sol()
	rx, ry = joystik.sag()
	buttons = joystik.butonlar()

	print("Sağ joystik değerleri: ", lx, ly)
	print("Sol joystik değerleri: ", rx, ry)

	if(1 in buttons):
		print("1'inci Butona basıldı!")

```
Bu kod kumanda verilerini okur ve bu verileri console'a print fonkisyonun kullanarak gösterir
