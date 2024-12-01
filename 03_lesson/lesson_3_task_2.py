from smartphone import Smartphone

catalog = [
    Smartphone("Apple","iphone 5S","+79025529465"),
    Smartphone("Samsung","Galaxy A32","+79236547899"),
    Smartphone("Nokia","Pixel 5","+79102347654"),
    Smartphone("Redmi","9C NFC","+79136723456"),
    Smartphone("Xiaomi","141 Pro","+79254673997")
]

for Smartphone in catalog:
    print(f"{Smartphone.brand} - {Smartphone.model} - {Smartphone.number}")