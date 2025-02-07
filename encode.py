from PIL import Image

def encode_message(image_path, message, output_path):
    img = Image.open(image_path)
    message += '\x00'
    # print(' '.join(format(ord(char), '08b') for char in message))
    for char in message:
        print(char, '->', format(ord(char), '08b'))
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    print(binary_message)
    message_length = len(binary_message)
    print(f'message length {message_length}')
    
    
    if message_length > img.width * img.height * 3:
        raise ValueError("Pesan terlalu panjang untuk gambar ini.")
    
    pixels = img.load()
    index = 0
    
    for i in range(img.width):
        for j in range(img.height):
            # print(f'index {index}')
            r, g, b = pixels[i, j]
            # print(binary_message[index])
            if index < message_length:
                print('R' , end = ' => ')
                print(format(r, '08b') , end=" => ")
                print(binary_message[index] , end=' =>  ')
                # print(r & ~1)
                
                r = (r & ~1) | int(binary_message[index])
                print(format(r, '08b') , end='     ')
                index += 1
            if index < message_length:
                print('G' , end = ' => ')
                print(format(g, '08b') , end=" => ")
                print(binary_message[index] , end=' =>  ')
                g = (g & ~1) | int(binary_message[index])
                print(format(g, '08b') , end='     ')
                index += 1
            if index < message_length:
                print('B' , end = ' => ')
                print(format(b, '08b') , end=" => ")
                print(binary_message[index] , end=' =>  ')
                b = (b & ~1) | int(binary_message[index])
                print(format(b, '08b'))
                index += 1
            
            pixels[i, j] = (r, g, b)
    
    img.save(output_path)
    # print('')
    # print("Pesan berhasil disembunyikan dalam gambar.")


# encode_message('input3.jpg', 'jam 3 berkumpul', 'output_image.png')

print('\n')
try : 
    print('masukkan pesan yang ingin disisipkan ')
    a = input('=> ')
    # print(len(a))
    print('masukkan path image yang akan di encode ')
    file = input('=> ')
    output = f'output_image.png'
    encode_message(file, a, f'{output}')
    print(f'Berhasil Steganografi di file {output}')
except :
    print('file tidak ditemukan')