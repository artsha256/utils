import re
import os
import requests
from urllib.parse import unquote
from pathlib import Path

def download_markdown_images(markdown_file, output_folder):
    """
    Read a markdown file, find all image links, and download the images to the specified folder.
    
    Args:
        markdown_file (str): Path to the markdown file
        output_folder (str): Path to the folder where images will be saved
    """
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Read markdown file
    try:
        with open(markdown_file, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        print(f"Error reading markdown file: {e}")
        return

    # Regular expression to find image links
    # Matches both ![alt](url) and <img src="url"> formats
    image_pattern = r'!\[.*?\]\((.*?)\)|<img.*?src=[\'\"](.*?)[\'\"]'
    
    # Find all image links
    matches = re.finditer(image_pattern, content)
    
    for match in matches:
        # Get the URL from either the markdown or HTML format
        image_url = match.group(1) or match.group(2)
        
        if not image_url:
            continue
            
        try:
            # Get original filename from URL
            filename = os.path.basename(unquote(image_url))
            
            # Remove query parameters if any
            filename = filename.split('?')[0]
            
            # Create full output path
            output_path = os.path.join(output_folder, filename)
            
            # Download the image
            response = requests.get(image_url, stream=True)
            response.raise_for_status()
            
            # Save the image
            with open(output_path, 'wb') as img_file:
                for chunk in response.iter_content(chunk_size=8192):
                    img_file.write(chunk)
                    
            print(f"Successfully downloaded: {filename}")
            
        except Exception as e:
            print(f"Error downloading {image_url}: {e}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Download images from a markdown file')
    parser.add_argument('markdown_file', help='Path to the markdown file')
    parser.add_argument('output_folder', help='Path to the output folder')
    
    args = parser.parse_args()
    
    download_markdown_images(args.markdown_file, args.output_folder)