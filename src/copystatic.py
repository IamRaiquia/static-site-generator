import os, shutil

def copy_files_recursive(src, dst):
    paths = os.listdir(src)
    if not os.path.exists(dst):
        os.mkdir(dst)
    
    for path in paths:
        src_path = os.path.join(src, path)
        dst_path = os.path.join(dst, path)
        
        print(f"Source Path: {src_path}")
        print(f"Destination Path: {dst_path}")
    
        if os.path.isdir(src_path):
            copy_files_recursive(src_path, dst_path)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
