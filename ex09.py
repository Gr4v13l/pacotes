import qrcode 

#criar um código qr 

qr = qrcode.QRCode( version =1, box_size=10, border=5)

#Adicionar dados ao código QR 

data = "https://www.gooogle.com"
qr.add_data(data)
qr.make(fit=True)

#Criar imagem do código QR 

img = qr.make_image(fill_color='black', back_color = 'white')

#Salvar imagem em um arquivo 

img.save('qr_code.png')