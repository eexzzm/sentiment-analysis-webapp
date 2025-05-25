import re
import json
import unicodedata

with open('../model/alay_dict.json', 'r') as f:
    SLANG_DICT = json.load(f)

def case_folding(text):
    return text.lower()

def normalize_alay(text):
    words = text.split()
    normalized_words = [SLANG_DICT.get(w, w) for w in words]
    return ' '.join(normalized_words)

def reduce_repeated_chars(text):
    # Ubah huruf yang berulang lebih dari 2x menjadi maksimal 2 huruf
    return re.sub(r'(.)\1{2,}', r'\1', text)

def remove_non_ascii(text):
    # Menghapus karakter yang bukan ASCII
    return ''.join(c for c in text if ord(c) < 128)


def nontext_clean(text):

    text = remove_non_ascii(text)
    text = re.sub(r'http\S+', ' ', text)          # Ganti URL jadi spasi
    text = re.sub(r'@\w+', ' ', text)             # Ganti mention jadi spasi
    text = re.sub(r'#\w+', ' ', text)             # Ganti hashtag jadi spasi
    # text = re.sub(r'<.*?>', '', text)             # Hapus tag seperti <FACE WITH STUCK-OUT TOUNGES>
    text = re.sub(r'[^\w\s]', ' ', text)          # Ganti simbol/punctuation jadi spasi
    text = re.sub(r'\d+', '', text)               # Hapus angka
    text = reduce_repeated_chars(text)            # Normalisasi huruf berulang
    text = re.sub(r'\s+', ' ', text)              # Ganti banyak spasi jadi satu spasi
    text = text.strip()                           # Hapus spasi depan-belakang
    return text



def clean_text(text):
    text = case_folding(text)
    text = nontext_clean(text)
    text = normalize_alay(text)
    return text