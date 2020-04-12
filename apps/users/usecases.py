from django.core import mail


class SendEmail:

    @staticmethod
    def send(user_email, title, message):
        connection = mail.get_connection()

        try:
            connection.open()
        except:
            return False

        email_settings = user_email
        email = mail.EmailMessage(
            title, message,
            email_settings,
            [email_settings],
            connection=connection,
        )

        email.send()
        connection.close()

        return True

