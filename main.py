import os
import shutil
import argparse

DEFAULT_RESOURCE_DIR = os.path.join(os.path.expanduser("~"), "Pictures", "icon")

def sync_files(resource_dir, destination_dir):
    if not os.path.exists(resource_dir):
        print(f"Error: The resource directory '{resource_dir}' does not exist.")
        return
    
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    for item in os.listdir(resource_dir):
        resource_path = os.path.join(resource_dir, item)
        destination_path = os.path.join(destination_dir, item)
        
        if os.path.isdir(resource_path):
            sync_files(resource_path, destination_path)
        else:
            shutil.copy2(resource_path, destination_path)
            print(f"Copied: {resource_path} -> {destination_path}")

def main():
    parser = argparse.ArgumentParser(description="Sync files from ResourceDir to DestinationDir.")
    parser.add_argument("-r", "--resource", default=DEFAULT_RESOURCE_DIR, help="The source directory (default is '~/Pictures/icon/')")
    parser.add_argument("-d", "--destination", default=os.getcwd(), help="The destination directory (default is current directory)")
    
    args = parser.parse_args()
    
    sync_files(args.resource, args.destination)

if __name__ == "__main__":
    main()
