import os
def save_content(name, html_content,format):
    project_folder = os.path.dirname(os.path.abspath(__file__)).replace('/src', '/')
    folder_path = os.path.join(project_folder, f"output/{format}")

    os.makedirs(folder_path, exist_ok=True)
    filename = name + '.'+ format
    file_path = os.path.join(folder_path, filename)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html_content)

