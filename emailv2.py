import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email_with_attachment(sender_email, sender_password, recipient_email, subject, body, filename):
    try:
        # Membuat pesan email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Menambahkan isi pesan
        msg.attach(MIMEText(body, 'plain'))
        
        # Membaca dan menambahkan file lampiran
        with open(filename, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(filename)}')
            msg.attach(part)
        
        # Menghubungkan ke server SMTP (contoh: Gmail)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Mengamankan koneksi
        server.login(sender_email, sender_password)
        
        # Mengirim email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email berhasil dikirim dengan lampiran!")
        
        # Menutup koneksi ke server SMTP
        server.quit()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Contoh penggunaan
sender_email = ""
sender_password = ""
recipient_email = "recipient@email.com"
subject = "script email dengan lampiran email"
body = "UAS: uji coba dengan lampiran file dari script. 2155202073"
filename = "Partition:/../../filename.extension"  # Ganti dengan path yang benar sesuai dengan sistem Anda

send_email_with_attachment(sender_email, sender_password, recipient_email, subject, body, filename)
