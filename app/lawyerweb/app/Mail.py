import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def MailSend(name, subject, email, user_message):
    # Gmail SMTP sunucusu ve giriş bilgileri
    smtp_server = 'smtp.gmail.com'
    port = 587  # TLS için port numarası
    username = 'kendimcehikayeler@gmail.com'
    password = 'kcuv rhkj fgwm hjjz'  # Uygulama şifresi

    # Gönderen ve alıcı bilgileri
    sender_email = 'kendimcehikayeler@gmail.com'
    receiver_email = 'muratasnb@hotmail.com'

    # MIME Mesajını oluşturma
    mime_message = MIMEMultipart("alternative")
    mime_message["Subject"] = f"{subject} {name}"
    mime_message["From"] = sender_email
    mime_message["To"] = receiver_email

    # E-posta gövdesi: Düz metin ve HTML versiyonları
    text = f"Merhabalar {name},\nHere is your message: {user_message}"
    html = f"""\
    <html>
      <body>
        <p>Merhabalar,
        <br>
        <p>{name} adlı müşterinin mesajı
        <br>
         Here is your message:<br><b>{user_message}</b></p>
      </body>
    </html>
    """
    # MIMEText nesnelerini oluştur ve MIMEMultipart mesajına ekle
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    mime_message.attach(part1)
    mime_message.attach(part2)

    # E-posta gönderimi için SMTP bağlantısını kur
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # TLS (güvenlik) başlat
            server.login(username, password)  # Gmail kullanıcı adı ve uygulama şifresi ile giriş yap
            server.sendmail(sender_email, receiver_email, mime_message.as_string())
            print("Email successfully sent!")
    except Exception as e:
        print(f"An error occurred: {e}")
