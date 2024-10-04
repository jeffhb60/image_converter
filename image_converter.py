from PIL import Image
import os

class ImageConverter:
    SUPPORTED_FORMATS = [
        'JPEG', 'JPG', 'PNG', 'GIF', 'TIFF', 'TIF',
        'BMP', 'ICO', 'PDF', 'WEBP'
    ]

    def __init__(self, input_file, output_file):
        """
        Initializes the ImageConverter with the given input file.
        """
        self.input_file = input_file
        self.output_file = output_file

        if not os.path.exists(input_file):
            raise FileNotFoundError(f"The file '{input_file}' does not exist.")

        try:
            self.image = Image.open(input_file)
            self.convert(output_file)
        except IOError as e:
            raise IOError(f"Cannot open image file '{input_file}': {e}")

    def convert(self, output_file, format=None):
        """
        Converts and saves the image to the specified output file and format.
        If format is not specified, it is inferred from the output file extension.
        """
        if not format:
            # Infer format from the output file extension
            format = os.path.splitext(output_file)[1].lower()
            format = format.lstrip('.')
            format = format.upper()
        else:
            format = format.upper()

        # Map common file extensions to Pillow format names
        format_mappings = {
            'JPG': 'JPEG',
            'TIF': 'TIFF'
        }
        format = format_mappings.get(format, format)

        if format not in self.SUPPORTED_FORMATS:
            raise ValueError(
                f"Unsupported format '{format}'. Supported formats are: {', '.join(self.SUPPORTED_FORMATS)}."
            )

        try:
            # For saving to PDF, the image must be in RGB mode
            if format == 'PDF' and self.image.mode != 'RGB':
                self.image = self.image.convert('RGB')

            self.image.save(output_file, format=format)
            print(f"Image saved as '{output_file}' in {format} format.")
        except IOError as e:
            raise IOError(f"Cannot save image to '{output_file}': {e}")

    @classmethod
    def get_supported_formats(cls):
        return cls.SUPPORTED_FORMATS
