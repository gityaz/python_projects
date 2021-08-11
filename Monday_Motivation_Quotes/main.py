import smtplib, random, datetime as dt


def send_mail():
    my_email = "yazadzy@gmail.com"
    my_pass = "Adz654@@@"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='yazdan2905@outlook.com',
            msg=f'Subject:Monday Motivation\n\n{choice}'
        )


now = dt.datetime.now()
day = (now.weekday())

if day == 0:  # Monday
    with open("quotes.txt") as q_file:
        quotes = q_file.readlines()
        choice = random.choice(quotes)
        send_mail()



