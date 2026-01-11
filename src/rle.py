# RLE (Run-Length Encoding) sikistirma algoritmasi

def encode(text):
    # Bu fonksiyon metni RLE ile sikistirir
    result = ""
    count = 1

    for i in range(len(text)):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
        else:
            result = result + str(count) + text[i]
            count = 1

    return result


def decode(text):
    # Bu fonksiyon sikistirilmis veriyi geri acar
    result = ""
    number = ""

    for c in text:
        if c >= '0' and c <= '9':
            number = number + c
        else:
            result = result + c * int(number)
            number = ""

    return result


def ratio(original, compressed):
    # Sikistirma oranini hesaplar
    return (len(original) - len(compressed)) / len(original) * 100


text = "AAAAABBBCCDAA"

compressed = encode(text)
decoded = decode(compressed)

print("Original:", text)
print("Compressed:", compressed)
print("Decoded:", decoded)
print("Ratio:", round(ratio(text, compressed), 2), "%")
