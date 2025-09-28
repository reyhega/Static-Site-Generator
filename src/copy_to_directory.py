import os
import shutil


def copy_contents_to_directory(source_dir, dest_dir):

    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"The specified path does not exist: {source_dir}")
    
    if os.path.exists(dest_dir):
        ls_dest = os.listdir(dest_dir)
        print(f"Deleting '{dest_dir}' with items: {ls_dest}")
        shutil.rmtree(dest_dir)
        print(f"'{dest_dir}' deleted successfully")
    
    print(f"Copying files from: '{source_dir}' to: '{dest_dir}'")
    copy_files(source_dir, dest_dir)
    print(f"Copied '{source_dir}' to '{dest_dir}' succesfully")


def copy_files(source_dir, dest_dir):

    if not os.path.exists(dest_dir):
        print(f"'{dest_dir}' does not exist, creating directory...")
        os.mkdir(dest_dir)
        print(f"'{dest_dir}' created succesfully, ready to copy files.")

    ls_source = os.listdir(source_dir)

    for item in ls_source:
        src_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_dir)
            print(f"Copied successfully:  '{item}' -> '{dest_dir}'")

        else:
            copy_files(src_path, dest_path)
    



