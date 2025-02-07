import wave
import numpy as np

def decode_audio(audio_path):
    audio = wave.open(audio_path, mode="rb")
    frames = audio.readframes(audio.getnframes())
    samples = np.frombuffer(frames, dtype=np.int16)
    
    # Ekstrak LSB dari sampel audio
    binary_message = ''
    for sample in samples:
        binary_message += str(sample & 1)
        if len(binary_message) % 8 == 0:
            byte = binary_message[-8:]
            char = chr(int(byte, 2))
            if char == '\x00':  # Berhenti jika menemukan penanda akhir pesan
                break
    
    # Konversi binary ke teks
    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if len(byte) < 8:
            break
        char = chr(int(byte, 2))
        if char == '\x00':
            break
        message += char
    
    audio.close()
    return message

# Contoh penggunaan
decoded_message = decode_audio('output.wav')
print("Pesan yang diekstrak:", decoded_message)