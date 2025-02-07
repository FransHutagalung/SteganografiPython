import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def decode_message(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    binary_message = ''
    
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

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.bmp")])
    if file_path:
        # Tampilkan gambar di panel kiri
        img = Image.open(file_path)
        img = img.resize((400, 400), Image.Resampling.LANCZOS)  # Resize gambar ke ukuran 400x400
        img_tk = ImageTk.PhotoImage(img)
        panel_left.config(image=img_tk)
        panel_left.image = img_tk  # Simpan referensi agar gambar tidak dihapus oleh garbage collector
        global current_image_path
        current_image_path = file_path  # Simpan path gambar yang dipilih

def decode_image():
    if current_image_path:
        decoded_message = decode_message(current_image_path)
        result_label.config(text=f"Pesan yang diekstrak: {decoded_message}")
    else:
        result_label.config(text="Pilih gambar terlebih dahulu!")

# Buat GUI
root = tk.Tk()
root.title("Steganografi Decoder")

# Panel untuk menampilkan gambar (ukuran 400x400 dengan latar belakang putih)
panel_left = tk.Label(root, bg="white", width=50, height=25)  # Ukuran panel lebih besar
panel_left.pack(side=tk.LEFT, padx=10, pady=10)

# Frame untuk tombol dan hasil
right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# Tombol untuk memilih gambar
open_button = tk.Button(right_frame, text="Pilih Gambar", command=open_image)
open_button.pack(pady=10)

# Tombol untuk decode
decode_button = tk.Button(right_frame, text="Decode", command=decode_image)
decode_button.pack(pady=10)

# Label untuk menampilkan hasil
result_label = tk.Label(right_frame, text="Pesan yang diekstrak: ")
result_label.pack(pady=10)

# Variabel untuk menyimpan path gambar yang dipilih
current_image_path = None

# Jalankan aplikasi
root.mainloop()