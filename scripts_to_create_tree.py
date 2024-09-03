import os

# Define the base directory (this should be the path to your main folder)
base_dir = "TVChannelPlayout"

# Define the folder structure and files
structure = {
    "video_management": ["__init__.py", "playlist.py", "video_preview.py", "video_trimming.py"],
    "ad_scheduling": ["__init__.py", "ad_management.py", "ad_scheduling.py", "ad_insertion.py"],
    "channel_branding": ["__init__.py", "logo_overlay.py", "ticker.py", "watermark.py"],
    "playout_control": ["__init__.py", "playback_controls.py", "preview.py", "bitrate_control.py"],
    "scheduling": ["__init__.py", "movie_scheduling.py", "automated_execution.py"],
    "output_settings": ["__init__.py", "udp_streaming.py", "file_output.py", "resolution_settings.py"],
    "resource_management": ["__init__.py", "cpu_monitor.py", "memory_monitor.py", "alert_system.py"],
    "customization": ["__init__.py", "theme_customization.py", "settings_panel.py", "user_profiles.py"],
    "logging_reporting": ["__init__.py", "activity_logs.py", "error_reporting.py", "playout_history.py"],
    "security": ["__init__.py", "authentication.py", "access_control.py"],
    "backup_restore": ["__init__.py", "playlist_backup.py", "restore_functionality.py"],
    "integration": ["__init__.py", "external_tools.py", "api_support.py"],
    "utilities": ["__init__.py", "clock_overlay.py", "subtitle_management.py", "aspect_ratio_control.py"],
    "assets": {
        "logos": [],
        "watermarks": [],
        "tickers": [],
        "videos": [],
    }
}

# Function to create the directory structure
def create_structure(base_path, structure):
    for folder, files in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        if isinstance(files, list):
            for file in files:
                open(os.path.join(folder_path, file), 'w').close()
        elif isinstance(files, dict):
            create_structure(folder_path, files)

# Create the base directory
os.makedirs(base_dir, exist_ok=True)

# Create the structure
create_structure(base_dir, structure)

# Create the main.py file
with open(os.path.join(base_dir, "main.py"), 'w') as f:
    f.write("# Main application script\n")

print("Directory structure created successfully!")
