# Obsidian Image Extractor

This script extracts and downloads images from a markdown file to a specified output folder.

## Requirements

Make sure you have the required Python packages installed. You can install them using the following command:

```shell
pip install -r requirements.txt
```

Usage
To use the script, run the following command:
<markdown_file>: Path to the markdown file from which images will be extracted.
<output_folder>: Path to the folder where images will be saved.

Example

```shell
python img_extractor.py path_to_your_file.md path_to_folder 
```

This command will download all images from the `path_to_your_file.md` and save them in the `path_to_folder` folder.

Notes
The script supports both markdown image links (!alt) and HTML image tags (<img src="url">).
Ensure that the output folder exists or will be created by the script.
The script will print messages indicating the success or failure of each image download.
