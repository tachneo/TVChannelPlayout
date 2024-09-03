import os
import json

class PlaylistBackupManager:
    def __init__(self, backup_directory="backups"):
        self.backup_directory = backup_directory
        if not os.path.exists(self.backup_directory):
            os.makedirs(self.backup_directory)

    def backup_playlist(self, playlist, backup_name):
        backup_path = os.path.join(self.backup_directory, f"{backup_name}.json")
        try:
            with open(backup_path, 'w') as f:
                json.dump(playlist, f)
            print(f"Playlist backed up to {backup_path}")
        except Exception as e:
            print(f"Error backing up playlist: {e}")

    def list_backups(self):
        try:
            backups = os.listdir(self.backup_directory)
            print("Available backups:")
            for backup in backups:
                print(f"- {backup}")
            return backups
        except Exception as e:
            print(f"Error listing backups: {e}")
            return []
