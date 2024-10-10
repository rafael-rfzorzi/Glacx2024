import os
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from tkinter import Tk, messagebox
from PIL import Image

# Function to create a PDF report
def create_pdf(data, photos_folder, output_path):
    c = canvas.Canvas(output_path, pagesize=A4)

    # Set font and size for the report with support for Brazilian Portuguese characters
    c.setFont("Helvetica", 12)

    # Iterate through the data and add information to the PDF
    for index, row in data.iterrows():
        name = row['NAME']
        registration = row['REGISTRATION']
        photo_filename = row['PHOTO']

        # Draw information on the PDF with Brazilian Portuguese characters
        c.drawString(240, 700, f"Nome: {name}")
        c.drawString(240, 680, f"Registro: {registration}")

        # Load and draw the photo
        photo_path = os.path.join(photos_folder, photo_filename)
        if os.path.exists(photo_path):
            image = Image.open(photo_path)
            image_width, image_height = image.size
            c.drawInlineImage(photo_path, 100, 600, width=image_width / 4, height=image_height / 4)

        # Move to the next page for the next entry
        c.showPage()

    # Save the PDF
    c.save()

# Function to show an alert screen
def show_alert():
    root = Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("Success", "The process was completed successfully!")
    root.destroy()

# Main script

# Replace 'your_excel_file.xlsx' and 'output_report.pdf' with your actual file names
excel_file = 'MDPDF.xlsx'
output_pdf = 'output_report.pdf'
photos_folder = '.'  # Assuming images are in the root folder

# Read Excel file into a DataFrame with proper encoding for Brazilian Portuguese characters
#df = pd.read_excel(excel_file, encoding='utf-8')
df = pd.read_excel(excel_file)

# Generate the PDF report
create_pdf(df, photos_folder, output_pdf)

# Show the alert
show_alert()
