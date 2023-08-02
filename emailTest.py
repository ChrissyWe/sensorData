#!/usr/bin/env python3
import smtplib
import mimetypes
from email.message import EmailMessage
import datetime as dt
from datetime import datetime, timedelta

# E-Mail-Objekt initialisieren und Nachrichtentext setzen:
msg = EmailMessage()
msg['Subject'] = 'Diese E-mail enthält einen Anhang'
msg['From'] = 'buga-sensor@gmx.de'
msg['To'] = 'buga-sensor@gmx.de'
# Set text content
msg.set_content(f'Hallo,\nIm Anhang befindet sich die Mail für die Temperaturen von {datetime.today()}.')

filename = r"C:\Users\Chris\Documents\Semester_8\Bundesgartenschau\2023-07-01_Temperatures.csv"

with open(filename, 'rb') as fp:
    file_data = fp.read()
    maintype, _, subtype = (mimetypes.guess_type(filename)[0] or 'application/octet-stream').partition("/")
    msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=filename)


# def attach_file_to_email(email, filename):
#     with open(filename, 'rb') as fp:
#         file_data = fp.read()
#         maintype, _, subtype = (mimetypes.guess_type(filename)[0] or 'application/octet-stream').partition("/")
#         email.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=filename)
#
# # Anhang anhängen
# attach_file_to_email(msg, r"C:\Users\Chris\Documents\Semester_8\Bundesgartenschau\2023-07-01_Temperatures.csv")

s = smtplib.SMTP('mail.gmx.net', 587)
s.starttls()
s.login('buga-sensor@gmx.de', 'qgQ35g94nQmbig')
s.send_message(msg)
s.quit()

# def send_mail_smtp(mail, host, username, password):
#     s = smtplib.SMTP(host, 587)
#     s.starttls()
#     s.login(username, password)
#     s.send_message(mail)
#     s.quit()
#
# # E-Mail per SMTP senden
# send_mail_smtp(msg, 'mail.gmx.net', 'buga-sensor@gmx.de', 'qgQ35g94nQmbig')