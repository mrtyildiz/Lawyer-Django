import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gmail SMTP sunucusu ve giriş bilgileri
smtp_server = 'smtp.gmail.com'
port = 587  # TLS için port numarası
username = 'kendimcehikayeler@gmail.com'
password = 'EvqvhvVK9u593WK7'  # Uygulama şifresi

# Gönderen ve alıcı bilgileri
sender_email = 'kendimcehikayeler@gmail.com'
receiver_email = 'muratasnb@hotmail.com'

# MIME Mesajını oluşturma
message = MIMEMultipart("alternative")
message["Subject"] = "Test Email from Python"
message["From"] = sender_email
message["To"] = receiver_email

# E-posta gövdesi: Düz metin ve HTML versiyonları
text = """\
Hi,
This is a test email from Python."""
html = """\
<html>
  <body>
    <p>Hi,<br>
       This is a <b>test</b> email from Python.</p>
  </body>
</html>
"""

# MIMEText nesnelerini oluştur ve MIMEMultipart mesajına ekle
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)

# E-posta gönderimi için SMTP bağlantısını kur
try:
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()  # TLS (güvenlik) başlat
        server.login(username, password)  # Gmail kullanıcı adı ve uygulama şifresi ile giriş yap
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email successfully sent!")
except Exception as e:
    print(f"An error occurred: {e}")
