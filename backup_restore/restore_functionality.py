import os
import json

class RestoreManager:
    def __init__(self, backup_directory="backups"):
        self.backup_directory = backup_directory

    def restore_playlist(self, backup_name):
        backup_path = os.path.join(self.backup_directory, f"{backup_name}.json")
        try:
            with open(backup_path, 'r') as f:
                playlist = json.load(f)
            print(f"Playlist restored from {backup_path}")
            return playlist
        except FileNotFoundError:
            print(f"Backup {backup_name} not found.")
            return None
        except Exception as e:
            print(f"Error restoring playlist: {e}")
            return None
