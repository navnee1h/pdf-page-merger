import os
from pdf2image import convert_from_path
from PIL import Image

def pdf_to_images(pdf_paths):
    all_images = []
    for pdf_path in pdf_paths:
        images = convert_from_path(pdf_path)
        all_images.extend(images)
    return all_images

def combine_images(images):
    combined_images = []
    for i in range(0, len(images), 2):
        if i + 1 < len(images):
            new_image = Image.new('RGB', (images[i].width + images[i + 1].width, max(images[i].height, images[i + 1].height)), (255, 255, 255))
            new_image.paste(images[i], (0, 0))
            new_image.paste(images[i + 1], (images[i].width, 0))
            combined_images.append(new_image)
        else:
            new_image = Image.new('RGB', (images[i].width, images[i].height), (255, 255, 255))
            new_image.paste(images[i], (0, 0))
            combined_images.append(new_image)
    return combined_images

def save_combined_images_as_pdf(combined_images, output_pdf_path):
    combined_images[0].save(output_pdf_path, save_all=True, append_images=combined_images[1:], quality=100)

def main(pdf_paths, output_pdf_path):
    images = pdf_to_images(pdf_paths)
    combined_images = combine_images(images)
    save_combined_images_as_pdf(combined_images, output_pdf_path)
    print(f"Combined PDF saved as: {output_pdf_path}")

# Example usage
pdf_files = ['1.pdf']
output_pdf = 'combined_output.pdf'
main(pdf_files, output_pdf)
