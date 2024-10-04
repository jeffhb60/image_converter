import os
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox
from image_converter import ImageConverter  # Import your ImageConverter class

class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Converter")

        # Input file label and entry
        self.input_label = Label(root, text="Select input file:")
        self.input_label.pack(pady=5)

        self.input_entry = Entry(root, width=50)
        self.input_entry.pack(pady=5)

        self.input_button = Button(root, text="Browse", command=self.browse_input_file)
        self.input_button.pack(pady=5)

        # Destination folder label and entry
        self.dest_label = Label(root, text="Select destination folder:")
        self.dest_label.pack(pady=5)

        self.dest_entry = Entry(root, width=50)
        self.dest_entry.pack(pady=5)

        self.dest_button = Button(root, text="Browse", command=self.browse_destination_folder)
        self.dest_button.pack(pady=5)

        # Output filename label and entry
        self.output_filename_label = Label(root, text="Enter output filename (with extension):")
        self.output_filename_label.pack(pady=5)

        self.output_filename_entry = Entry(root, width=50)
        self.output_filename_entry.pack(pady=5)

        # Convert button
        self.convert_button = Button(root, text="Convert", command=self.convert_image)
        self.convert_button.pack(pady=20)

    def browse_input_file(self):
        file_path = filedialog.askopenfilename(title="Select Input File",
                                               filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp;*.tiff;*.pdf;*.webp")])
        if file_path:
            self.input_entry.delete(0, 'end')
            self.input_entry.insert(0, file_path)

    def browse_destination_folder(self):
        folder_path = filedialog.askdirectory(title="Select Destination Folder")
        if folder_path:
            self.dest_entry.delete(0, 'end')
            self.dest_entry.insert(0, folder_path)

    def convert_image(self):
        input_file = self.input_entry.get()
        output_folder = self.dest_entry.get()
        output_filename = self.output_filename_entry.get()

        if not input_file or not output_folder or not output_filename:
            messagebox.showerror("Error", "Please make sure all fields are filled out.")
            return

        output_file = os.path.join(output_folder, output_filename)

        try:
            converter = ImageConverter(input_file, output_file)
            messagebox.showinfo("Success", f"Image converted and saved as '{output_file}'")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def run_app():
    root = Tk()
    app = ImageConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()
