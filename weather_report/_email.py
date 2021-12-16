# Import all of your extensions first
from tempfile import TemporaryDirectory
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import mimetypes
from pathlib import Path
from matplotlib.backends.backend_pdf import PdfPages
import os
import smtplib

# Define your signature. It will be attached to the email.
SIGNATURE = (
    '<div style="font-family: agency fb; font-size:130%;"><b>Preston Pope</b></div>\n'
    "<div>EOG Resources, Inc.</div>\n"

    "<div>Cell: (832) 465-0621</div>\n"
    "<div>preston_pope@eogresources.com</div>\n"
)


class EmailMsg:
    def __init__(self, recipient_list, sender, subject, signature=SIGNATURE):
        self.sender = sender
        self.subject = subject
        self.recipient_list = recipient_list
        self.signature = signature
        self.attachments = []
        self.images = []
        self.text = []

    def send(self):
        msg = self._construct_msg()
        with smtplib.SMTP("smtp.eogresources.com") as mailer:
            server_response = smtplib.SMTP.ehlo(mailer)
            mailer.sendmail(msg["From"], self.recipient_list, msg.as_string())

    def _construct_msg(self):
        """This constructs the email"""
        msg = MIMEMultipart()
        msg["Subject"] = self.subject
        msg["From"] = self.sender
        for attachment in self.attachments:
            msg.attach(attachment)
        for display in self.images:
            msg.attach(display)
        all_text = "<br></br>".join(self.text)
        all_text += "<br></br>" + self.signature
        msg.attach(MIMEText(all_text, "html"))
        return msg

    def convert_plots_to_attachment(self, figure_name, figures):
        """This function is used when you want to add multiple (or list of) plots to an email"""
        with TemporaryDirectory() as temp_dir:
            dir_path = Path(str(temp_dir))
            file = dir_path / "plots.pdf"
            with PdfPages(file) as pdf_file:
                for figure in figures:
                    pdf_file.savefig(figure, dpi=300, bbox_inches="tight")
            self.attach_file(figure_name, file, "pdf")

    def convert_summary_plots_to_attachment(self, figure_name, figures):
        """This function is used when you only want to add one plot to an email"""
        with TemporaryDirectory() as temp_dir:
            dir_path = Path(str(temp_dir))
            file = dir_path / "plots.pdf"
            with PdfPages(file) as pdf_file:
                pdf_file.savefig(figures, dpi=300, bbox_inches="tight")
            self.attach_file(figure_name, file, "pdf")

    def attach_file(self, attachment_name, file, file_type):
        """Attaches the file to the email"""
        with open(file, "rb") as f:
            attachment = MIMEApplication(f.read(), _subtype=file_type)
        attachment.add_header(
            "Content-Disposition", "attachment", filename=attachment_name
        )
        self.attachments.append(attachment)

    def add_image(self, image_name, image):
        """Use this to add the plot image to the body of the email"""
        c_type, encoding = mimetypes.guess_type(image)
        main_type, sub_type = c_type.split("/", 1)
        attachment = MIMEImage(image, _subtype=sub_type)
        attachment.add_header(
            "Content-Disposition", "attachment", image_name=image_name
        )
        self.images.append(attachment)
        self.add_text(f'<p><img src="cid:{len(self.images)-1}"></p>')

    def add_text(self, text):
        """This will allow you to add text in the body of the email you send."""
        self.text.append(text)
