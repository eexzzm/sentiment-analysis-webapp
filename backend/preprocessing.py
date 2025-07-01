import re
import json
import os
import unicodedata

SLANG_DICT_PATH = os.path.join(os.path.dirname(__file__), '../model/alay_dict.json')

with open(SLANG_DICT_PATH, 'r', encoding='utf-8') as f:
    SLANG_DICT = json.load(f)

def remove_emoji(text):
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags
        "]+", flags=re.UNICODE
    )
    text = emoji_pattern.sub(r'', text)
    text = re.sub(r'<.*?>', '', text) # Hapus tag seperti <FACE WITH STUCK-OUT TOUNGES>
    return text
    

def case_folding(text):
    return text.lower()

def normalize_alay(text):
    words = text.split()
    normalized_words = [SLANG_DICT.get(word, word) for word in words]
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
    text = re.sub(r'[^\w\s]', ' ', text)          # Ganti simbol/punctuation jadi spasi
    text = re.sub(r'\d+', '', text)               # Hapus angka
    text = reduce_repeated_chars(text)            # Normalisasi huruf berulang
    text = re.sub(r'\s+', ' ', text)              # Ganti banyak spasi jadi satu spasi
    text = text.strip()                           # Hapus spasi depan-belakang
    return text



def clean_text(text):
    text = str(text)
    text = remove_emoji(text)
    text = case_folding(text)
    text = nontext_clean(text)
    text = reduce_repeated_chars(text)
    text = normalize_alay(text)
    return text.strip()
