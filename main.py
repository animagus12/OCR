from tkinter import *
from tkinter import PhotoImage, filedialog
from PIL import ImageTk, Image
import cv2
import pytesseract

# setting root window:
root = Tk()
root.title("OCR")
root.geometry("600x600")
root.iconbitmap("C:/Users/subhr/OneDrive/Documents/Programs/Python/OCR/convert.ico")
root.config(bg="#2B2B2B")


def information():
    info = Tk()
    info.title("Info!")
    info.iconbitmap("C:/Users/subhr/OneDrive/Documents/Programs/Python/OCR/info.ico")
    # info.geometry("450x600")
    info.config(bg="#2B2B2B")

    info_label = Message(info, text= "Scanning Considerations:\n1 .The recommended resolution for best scanning results for OCR accuracy is 300 dots per inch(dpi).\n2 .Brightness settings that are too high or too low can have negative effects on the accuracy of your image. A brightness of 50 % is recommended.\n3. The straightness of the initial scan can affect OCR quality. Skewed pages can lead to inaccurate recognition.\n4. Older and discolored documents must be scanned in RGB mode in order to capture all of the image data.\nTextual Considerations: \n1. Language: texts published before 1850 may not be the most compatible with OCR software. However, if the pages you are scanning are in different a different language, many OCR systems allow you to select the language of the document.\n2. Documents with low contrast can result in poor OCR.\n3. Typescript results in poorer OCR than printed type inconsistent use of font faces and sizes can lower OCR accuracy.\nOther Considerations: \n1. An OCR software's ability to accurately analyze your document is dependent on the condition of the original and / or quality of the digital file.\n2. If you do not have a digital document, or if what you have is poor quality, you are able to scan the original document using your OCR program as your scanning software.\n3. No special skills are required to use OCR software.\n4. You should be aware that if your goal is 100 % text accuracy, you will need to check and correct the text after it has completed the original recognition process. The system cannot do this check itself. The editing/correcting process may take a considerable amount of time for large amounts of text and / or poor quality original text.", font="FixedSys 17", bg="#2B2B2B", fg="green")
    info_label.pack()

# Open a image and printing the location on the root window

def open_file():
    global myimg
    root.filename = filedialog.askopenfilename(
        initialdir="C:/", title="Select a File", filetypes=((".png files", "*.png"), ("All files", "*.*")))
    myimg = ImageTk.PhotoImage(Image.open(root.filename).resize((100, 100), Image.ANTIALIAS))

    mylabel = Label(root, text=root.filename,
                    font="FixedSys 17", bg="#2B2B2B", fg="green")
    mylabel.place(relx=0.5, rely=0.2, anchor="center")

    myimglbl = Label(image=myimg)
    myimglbl.place(relx=0.5, rely=0.32, anchor="center")


# Extracting text from the image

def convert():
    # Pre-processing of the image
    img = cv2.imread(root.filename)
    img = cv2.resize(img, None, fx=0.9, fy=0.9)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 91, 11)
    # Extrcation using tesseract
    config = "--psm 3"
    text = pytesseract.image_to_string(img, config=config)

    # Clearing the Text Box before adding text
    my_text.delete(1.0, END)

    # Inserting the extracted text
    my_text.insert(1.0, text)


# Buttons
# Adding the import image
import_img = PhotoImage(
    file=r'C:\Users\subhr\OneDrive\Documents\Programs\Python\OCR\import.png')

button = Button(root, text="Open File", command=open_file)
button.config(image=import_img, bg="#2B2B2B", activebackground="#2B2B2B")
button.place(relx=0.5, rely=0.1, anchor="center")

# Adding the Convert Image
convert_img = PhotoImage(
    file=r'C:\Users\subhr\OneDrive\Documents\Programs\Python\OCR\convert.png')

convert_btn = Button(root, text="Convert", command=convert)
convert_btn.config(image=convert_img, bg="#2B2B2B", activebackground="#2B2B2B")
convert_btn.place(relx=0.5, rely=0.48, anchor="center")

info_img = PhotoImage(
    file=r'C:\Users\subhr\OneDrive\Documents\Programs\Python\OCR\info.png')
    # .resize((50, 50), Image.ANTIALIAS))

info_btn = Button(root, text="Convert", command= information)
info_btn.config(image=info_img, bg="#2B2B2B", activebackground="#2B2B2B")
info_btn.place(relx=0.96, rely=0.04, anchor="center")

# Creating a text Box
my_text = Text(root, width=60, height=12)
my_text.place(relx=0.5, rely=0.72, anchor="center")

# window in mainloop:
root.mainloop()
