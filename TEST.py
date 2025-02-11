import paho.mqtt.client as mqtt
import time

# 🛰 MQTT Sunucu Bilgileri
BROKER = "176.96........."  # Sunucu IP adresini buraya yaz
TOPIC = "tracker/location"

#  Yarış Pisti Koordinatları (Sırayla Hareket Ettirilecek)
track_coordinates = [
    [40.787436, 29.451071],  
    [40.787434, 29.451315],
    [40.787355, 29.451512],
    [40.787256, 29.451922],
    [40.787143, 29.452188],
    [40.786857, 29.452356],  
    [40.786741, 29.452439],
    [40.786635, 29.452624],
    [40.786427, 29.452713],
    [40.786055, 29.452777],
    [40.785964, 29.452873],  

    [40.785872, 29.453364],  
    [40.785780, 29.453862],
    [40.786002, 29.454353],
    [40.786355, 29.454831],
    [40.786818, 29.455163],
    [40.787065, 29.455571], 
    [40.787171, 29.456133],
    [40.787287, 29.457090],
    [40.787321, 29.457791],
    [40.787601, 29.457677],
    [40.788156, 29.457338],  

    [40.788504, 29.457128],  
    [40.788311, 29.456260],
    [40.788036, 29.454487],
    [40.787654, 29.452197],
    [40.787567, 29.451348]
]

#  MQTT İstemcisini oluştur ve bağlan
client = mqtt.Client()
client.connect(BROKER, 1883, 60)

#  Yarışçı hareketini simüle eden fonksiyon
def publish_location():
    while True:
        for lat, lon in track_coordinates:
            message = f"LAT:{lat}LON:{lon}" 
            client.publish(TOPIC, message)
            print(f"📡 Gönderilen: {message}")

            # 2 saniye bekleyerek gerçek zamanlı hareketi simüle et
            time.sleep(2)

# 🏁 Yarışçı konumunu göndermeye başla
publish_location()
