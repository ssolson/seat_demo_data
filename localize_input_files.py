import os


def replace_path_in_file(file_path, input_folder, style_files_folder):
    with open(file_path, 'r') as f:
        contents = f.read()

    # Replace the placeholders with the actual paths
    contents = contents.replace("<input_folder>", input_folder)
    contents = contents.replace("<style_folder>", style_files_folder)

    # Determine the output filename (change extension from .default to .ini)
    output_file_path = os.path.splitext(file_path)[0] + ".ini"

    # Write the modified contents to the new .ini file
    with open(output_file_path, 'w') as f:
        f.write(contents)


def main():
    # Ask user for input
    input_folder = input("Where are your input files? ").strip()
    style_files_folder = input("Where is your style_files folder? ").strip()

    # Search for all .default files in the input folder
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".default"):
                replace_path_in_file(os.path.join(
                    root, file), input_folder, style_files_folder)


if __name__ == "__main__":
    main()
