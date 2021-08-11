##################### Hard Starting Project ######################
import pandas, datetime as dt, random, smtplib
data = pandas.read_csv("birthdays.csv")

my_email = "yazadzy@gmail.com"
my_pass = "Adz654@@@"

now = dt.datetime.now()
day = now.day
month = now.month
today = (month, day)
birthdays_dict = {(data_row['month'], data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    rnum = random.randint(1,3)
    file_path = f'letter_templates/letter_{rnum}.txt'
    with open(file_path) as letter:
        content = letter.read()
        content = content.replace('[NAME]', birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f'Subject:Happy Birthday {birthday_person["name"]}!\n\n{content}'
        )


# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



