# PiWars2023
## Ultrasonik_S
UltrasonikSensor sınıfı GPIO modu olarak BCM kullanır

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
while True:
	k.onizlemeyi_baslat()
	k.resize(640, 480)

```
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

En başta 2 motoru daha sonrasında sol motoru belirlenen hızda çalıştırır.

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

```
