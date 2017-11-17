import pysftp
import os

with pysftp.Connection(os.environ["SFTP_HOSTNAME"], username=os.environ["SFTP_USERNAME"], password=os.environ["SFTP_PASSWORD"]) as sftp:
    print(sftp.pwd)
