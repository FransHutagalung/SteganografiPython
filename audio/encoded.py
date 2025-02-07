import wave
import numpy as np

def encode_audio(input_audio, output_audio, message):
    # Buka file audio
    audio = wave.open(input_audio, mode="rb")
    frames = audio.readframes(audio.getnframes())
    samples = np.frombuffer(frames, dtype=np.int16).copy()  # Buat salinan yang dapat dimodifikasi
    
    # Tambahkan penanda akhir pesan
    message += '\x00'
    
    # Konversi pesan ke binary
    binary_message = ''.join(format(ord(c), '08b') for c in message)
    message_length = len(binary_message)
    
    # Sisipkan pesan ke LSB sampel audio
    if message_length > len(samples):
        raise ValueError("Pesan terlalu panjang untuk disisipkan.")
    
    for i in range(message_length):
        samples[i] = (samples[i] & ~1) | int(binary_message[i])
    
    # Simpan audio yang telah dimodifikasi
    with wave.open(output_audio, 'wb') as output:
        output.setparams(audio.getparams())
        output.writeframes(samples.tobytes())
    
    audio.close()

# Contoh penggunaan
encode_audio('input.wav', 'output.wav', 'Ini pesan rahasia')