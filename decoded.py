from PIL import Image, ImageTk

def decode_message(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    binary_message = ''
    
    # ambil 
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            binary_message += str(r & 1)    
            binary_message += str(g & 1)
            binary_message += str(b & 1)
    
    # Konversi binary ke teks
    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        char = chr(int(byte, 2))
        if char == '\x00':  # Berhenti jika menemukan penanda akhir pesan
            break
        message += char
    
    return message


try :
    print('masukkan path file')
    a = input('=> ')
    message = decode_message(a)
    print(f'isi pesan rahasia => {message}')
except:
    print('file tidak ditemukan')