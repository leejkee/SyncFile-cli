import os
import shutil
import argparse

DEFAULT_RESOURCE_DIR = os.path.join(os.path.expanduser("~"), "Pictures", "icon")
DEFAULT_DESTINATION_DIR = os.getcwd()

def sync_files(resource_dir, destination_dir, test_mode = False):
    if not os.path.exists(resource_dir):
        print(f"Error: The resource directory '{resource_dir}' does not exist.")
        return
    
    icon_dir = os.path.join(destination_dir, "icon")
    if not os.path.exists(icon_dir):
        os.makedirs(icon_dir)
        print(f"Created directory: {icon_dir}")
    
    for item in os.listdir(resource_dir):
        resource_path = os.path.join(resource_dir, item)
        destination_path = os.path.join(icon_dir, item)
        
        if os.path.isdir(resource_path):
            sync_files(resource_path, destination_path)
        else:
            if os.path.exists(destination_path):
                print(f"Skipped: {resource_path} (already exists at destination)")
            else:
                if test_mode:
                    print(f"Test mode: Would copy {resource_path} -> {destination_path}")
                else:
                    shutil.copy2(resource_path, destination_path)
                    print(f"Copied: {resource_path} -> {destination_path}")

def main():
    parser = argparse.ArgumentParser(description="Sync files from ResourceDir to DestinationDir.")
    parser.add_argument("-r", "--resource", default=DEFAULT_RESOURCE_DIR, help="The source directory (default is '~/Pictures/icon/')")
    parser.add_argument("-d", "--destination", default=os.getcwd(), help="The destination directory (default is current directory)")
    parser.add_argument("-t", "--test", action="store_true", help="Test mode: only print what would be done, without actually copying files.")

    
    args = parser.parse_args()
    
    sync_files(args.resource, args.destination, args.test)

if __name__ == "__main__":
    main()
