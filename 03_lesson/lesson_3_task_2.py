from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "S 25 Ultra", "+7-235-863-11-34"),
    Smartphone("Siemens", "c65", "+7-904-454-32-74"),
    Smartphone("Motorola", "S50 Neo", "+7-657-789-47-36"),
    Smartphone("LG", "h324", "+7-235-673-53-68"),
    Smartphone("Redmi", "Note 10 Pro", "+7-454-574-23-46"),
]
for smartphone in catalog:
    print(
        f"{smartphone.phone_brand}-{smartphone.phone_model}. {smartphone.phone_number}"
    )
