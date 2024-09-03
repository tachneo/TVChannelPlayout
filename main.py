from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTabWidget, QLabel, QListWidget, QFileDialog, QMessageBox, QLineEdit, QInputDialog
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtCore import QUrl

import threading

# Importing modules from various packages
from video_management.playlist import PlaylistManager
from video_management.video_preview import VideoPreviewer
from video_management.video_trimming import VideoTrimmer

from ad_scheduling.ad_management import AdManager
from ad_scheduling.ad_scheduling import AdScheduler
from ad_scheduling.ad_insertion import AdInserter

from channel_branding.logo_overlay import LogoOverlay
from channel_branding.ticker import TickerManager
from channel_branding.watermark import WatermarkManager

from playout_control.playback_controls import PlaybackController
from playout_control.preview import VideoPreviewer as PlayoutPreviewer
from playout_control.bitrate_control import BitrateController

from scheduling.movie_scheduling import MovieScheduler
from scheduling.automated_execution import AutomatedExecutor

from output_settings.udp_streaming import UDPStreamer
from output_settings.file_output import FileOutputManager
from output_settings.resolution_settings import ResolutionManager

from resource_management.cpu_monitor import CPUMonitor
from resource_management.memory_monitor import MemoryMonitor
from resource_management.alert_system import AlertSystem

from customization.theme_customization import ThemeCustomizer
from customization.settings_panel import SettingsPanel
from customization.user_profiles import UserProfileManager

from logging_reporting.activity_logs import ActivityLogger
from logging_reporting.error_reporting import ErrorReporter
from logging_reporting.playout_history import PlayoutHistoryManager

from security.authentication import AuthenticationManager
from security.access_control import AccessControlManager

from backup_restore.playlist_backup import PlaylistBackupManager
from backup_restore.restore_functionality import RestoreManager

from integration.external_tools import ExternalToolsIntegration
from integration.api_support import APISupport

from utilities.clock_overlay import ClockOverlay
from utilities.subtitle_management import SubtitleManager
from utilities.aspect_ratio_control import AspectRatioController


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TV Channel Playout System")
        self.setGeometry(100, 100, 1000, 800)

        # Main Tab Widget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Video Management Tab
        self.video_management_tab = QWidget()
        self.video_management_layout = QVBoxLayout()
        self.video_management_tab.setLayout(self.video_management_layout)

        # Playlist Manager
        self.playlist_manager = PlaylistManager()
        self.video_management_layout.addWidget(QLabel("Playlist Manager"))
        self.load_playlist_button = QPushButton("Load Playlist")
        self.save_playlist_button = QPushButton("Save Playlist")
        self.add_video_button = QPushButton("Add Video")
        self.remove_video_button = QPushButton("Remove Video")
        self.video_management_layout.addWidget(self.load_playlist_button)
        self.video_management_layout.addWidget(self.save_playlist_button)
        self.video_management_layout.addWidget(self.add_video_button)
        self.video_management_layout.addWidget(self.remove_video_button)

        self.load_playlist_button.clicked.connect(self.load_playlist)
        self.save_playlist_button.clicked.connect(self.save_playlist)
        self.add_video_button.clicked.connect(self.add_video_to_playlist)
        self.remove_video_button.clicked.connect(self.remove_video_from_playlist)

        # Ad Scheduling Tab
        self.ad_scheduling_tab = QWidget()
        self.ad_scheduling_layout = QVBoxLayout()
        self.ad_scheduling_tab.setLayout(self.ad_scheduling_layout)

        self.ad_manager = AdManager()
        self.ad_scheduler = AdScheduler()
        self.ad_inserter = AdInserter()

        self.add_ad_button = QPushButton("Add Advertisement")
        self.schedule_ad_button = QPushButton("Schedule Advertisement")
        self.insert_ad_button = QPushButton("Insert Advertisement")
        self.ad_scheduling_layout.addWidget(self.add_ad_button)
        self.ad_scheduling_layout.addWidget(self.schedule_ad_button)
        self.ad_scheduling_layout.addWidget(self.insert_ad_button)

        self.add_ad_button.clicked.connect(self.add_ad)
        self.schedule_ad_button.clicked.connect(self.schedule_ad)
        self.insert_ad_button.clicked.connect(self.insert_ad)

        # Channel Branding Tab
        self.channel_branding_tab = QWidget()
        self.channel_branding_layout = QVBoxLayout()
        self.channel_branding_tab.setLayout(self.channel_branding_layout)

        self.logo_overlay = LogoOverlay()
        self.ticker_manager = TickerManager()
        self.watermark_manager = WatermarkManager()

        self.add_logo_button = QPushButton("Add Logo Overlay")
        self.add_ticker_button = QPushButton("Add Ticker")
        self.add_watermark_button = QPushButton("Add Watermark")
        self.channel_branding_layout.addWidget(self.add_logo_button)
        self.channel_branding_layout.addWidget(self.add_ticker_button)
        self.channel_branding_layout.addWidget(self.add_watermark_button)

        self.add_logo_button.clicked.connect(self.add_logo_overlay)
        self.add_ticker_button.clicked.connect(self.add_ticker)
        self.add_watermark_button.clicked.connect(self.add_watermark)

        # Playout Control Tab
        self.playout_control_tab = QWidget()
        self.playout_control_layout = QVBoxLayout()
        self.playout_control_tab.setLayout(self.playout_control_layout)

        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.playback_controller = PlaybackController(self.media_player)
        self.playout_previewer = PlayoutPreviewer()
        self.bitrate_controller = BitrateController()

        self.play_button = QPushButton("Play Video")
        self.pause_button = QPushButton("Pause Video")
        self.stop_button = QPushButton("Stop Video")
        self.fast_forward_button = QPushButton("Fast Forward")
        self.rewind_button = QPushButton("Rewind")
        self.playout_control_layout.addWidget(self.play_button)
        self.playout_control_layout.addWidget(self.pause_button)
        self.playout_control_layout.addWidget(self.stop_button)
        self.playout_control_layout.addWidget(self.fast_forward_button)
        self.playout_control_layout.addWidget(self.rewind_button)

        self.play_button.clicked.connect(self.playback_controller.play)
        self.pause_button.clicked.connect(self.playback_controller.pause)
        self.stop_button.clicked.connect(self.playback_controller.stop)
        self.fast_forward_button.clicked.connect(lambda: self.playback_controller.fast_forward(10))
        self.rewind_button.clicked.connect(lambda: self.playback_controller.rewind(10))

        # Scheduling Tab
        self.scheduling_tab = QWidget()
        self.scheduling_layout = QVBoxLayout()
        self.scheduling_tab.setLayout(self.scheduling_layout)

        self.movie_scheduler = MovieScheduler()
        self.automated_executor = AutomatedExecutor(self.media_player, self.movie_scheduler.schedule)

        self.schedule_movie_button = QPushButton("Schedule Movie")
        self.start_execution_button = QPushButton("Start Automated Execution")
        self.stop_execution_button = QPushButton("Stop Execution")
        self.scheduling_layout.addWidget(self.schedule_movie_button)
        self.scheduling_layout.addWidget(self.start_execution_button)
        self.scheduling_layout.addWidget(self.stop_execution_button)

        self.schedule_movie_button.clicked.connect(self.schedule_movie)
        self.start_execution_button.clicked.connect(self.start_execution)
        self.stop_execution_button.clicked.connect(self.stop_execution)

        # Output Settings Tab
        self.output_settings_tab = QWidget()
        self.output_settings_layout = QVBoxLayout()
        self.output_settings_tab.setLayout(self.output_settings_layout)

        self.udp_streamer = UDPStreamer()
        self.file_output_manager = FileOutputManager()
        self.resolution_manager = ResolutionManager()

        self.start_streaming_button = QPushButton("Start UDP Streaming")
        self.save_video_button = QPushButton("Save Video")
        self.change_resolution_button = QPushButton("Change Resolution")
        self.output_settings_layout.addWidget(self.start_streaming_button)
        self.output_settings_layout.addWidget(self.save_video_button)
        self.output_settings_layout.addWidget(self.change_resolution_button)

        self.start_streaming_button.clicked.connect(self.start_streaming)
        self.save_video_button.clicked.connect(self.save_video)
        self.change_resolution_button.clicked.connect(self.change_resolution)

        # Resource Management Tab
        self.resource_management_tab = QWidget()
        self.resource_management_layout = QVBoxLayout()
        self.resource_management_tab.setLayout(self.resource_management_layout)

        self.cpu_monitor = CPUMonitor()
        self.memory_monitor = MemoryMonitor()
        self.alert_system = AlertSystem(cpu_threshold=80, memory_threshold=80)

        self.cpu_label = QLabel("CPU Usage: 0%")
        self.memory_label = QLabel("Memory Usage: 0%")
        self.start_monitoring_button = QPushButton("Start Monitoring")
        self.resource_management_layout.addWidget(self.cpu_label)
        self.resource_management_layout.addWidget(self.memory_label)
        self.resource_management_layout.addWidget(self.start_monitoring_button)

        self.start_monitoring_button.clicked.connect(self.start_monitoring)

        # Customization Tab
        self.customization_tab = QWidget()
        self.customization_layout = QVBoxLayout()
        self.customization_tab.setLayout(self.customization_layout)

        self.settings_panel = SettingsPanel()
        self.user_profile_manager = UserProfileManager()

        self.save_profile_button = QPushButton("Save Profile")
        self.load_profile_button = QPushButton("Load Profile")
        self.delete_profile_button = QPushButton("Delete Profile")
        self.customization_layout.addWidget(self.settings_panel)
        self.customization_layout.addWidget(self.save_profile_button)
        self.customization_layout.addWidget(self.load_profile_button)
        self.customization_layout.addWidget(self.delete_profile_button)

        self.save_profile_button.clicked.connect(self.save_profile)
        self.load_profile_button.clicked.connect(self.load_profile)
        self.delete_profile_button.clicked.connect(self.delete_profile)

        # Logging and Reporting Tab
        self.logging_reporting_tab = QWidget()
        self.logging_reporting_layout = QVBoxLayout()
        self.logging_reporting_tab.setLayout(self.logging_reporting_layout)

        self.activity_logger = ActivityLogger()
        self.error_reporter = ErrorReporter()
        self.playout_history_manager = PlayoutHistoryManager()

        self.log_activity_button = QPushButton("Log Activity")
        self.report_error_button = QPushButton("Report Error")
        self.log_playout_button = QPushButton("Log Playout")
        self.logging_reporting_layout.addWidget(self.log_activity_button)
        self.logging_reporting_layout.addWidget(self.report_error_button)
        self.logging_reporting_layout.addWidget(self.log_playout_button)

        self.log_activity_button.clicked.connect(self.log_activity)
        self.report_error_button.clicked.connect(self.report_error)
        self.log_playout_button.clicked.connect(self.log_playout)

        # Security Tab
        self.security_tab = QWidget()
        self.security_layout = QVBoxLayout()
        self.security_tab.setLayout(self.security_layout)

        self.auth_manager = AuthenticationManager()
        self.access_control_manager = AccessControlManager()

        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.security_layout.addWidget(self.username_label)
        self.security_layout.addWidget(self.username_input)
        self.security_layout.addWidget(self.password_label)
        self.security_layout.addWidget(self.password_input)

        self.register_button = QPushButton("Register")
        self.login_button = QPushButton("Login")
        self.logout_button = QPushButton("Logout")
        self.security_layout.addWidget(self.register_button)
        self.security_layout.addWidget(self.login_button)
        self.security_layout.addWidget(self.logout_button)

        self.register_button.clicked.connect(self.register_user)
        self.login_button.clicked.connect(self.login_user)
        self.logout_button.clicked.connect(self.logout_user)

        # Backup and Restore Tab
        self.backup_restore_tab = QWidget()
        self.backup_restore_layout = QVBoxLayout()
        self.backup_restore_tab.setLayout(self.backup_restore_layout)

        self.playlist_backup_manager = PlaylistBackupManager()
        self.restore_manager = RestoreManager()

        self.backup_list = QListWidget()
        self.backup_restore_layout.addWidget(self.backup_list)

        self.backup_playlist_button = QPushButton("Backup Playlist")
        self.restore_playlist_button = QPushButton("Restore Selected Playlist")
        self.backup_restore_layout.addWidget(self.backup_playlist_button)
        self.backup_restore_layout.addWidget(self.restore_playlist_button)

        self.backup_playlist_button.clicked.connect(self.backup_playlist)
        self.restore_playlist_button.clicked.connect(self.restore_playlist)

        self.load_backups()

        # Integration Tab
        self.integration_tab = QWidget()
        self.integration_layout = QVBoxLayout()
        self.integration_tab.setLayout(self.integration_layout)

    
        self.ffmpeg_integration = ExternalToolsIntegration(tool_name="FFmpeg", tool_path="C:/Users/ASUS/TVChannelPlayout/TVChannelPlayout/ffmpeg/ffmpeg.exe")
        self.api_support = APISupport()

        self.tool_status_label = QLabel("Checking FFmpeg installation...")
        self.integration_layout.addWidget(self.tool_status_label)
        if self.ffmpeg_integration.check_tool_installed():
            self.tool_status_label.setText("FFmpeg is installed and ready to use.")
        else:
            self.tool_status_label.setText("FFmpeg is not installed or not found.")

        self.run_ffmpeg_button = QPushButton("Run FFmpeg Command")
        self.integration_layout.addWidget(self.run_ffmpeg_button)
        self.run_ffmpeg_button.clicked.connect(self.run_ffmpeg_command)

        self.start_api_button = QPushButton("Start API Server")
        self.stop_api_button = QPushButton("Stop API Server")
        self.integration_layout.addWidget(self.start_api_button)
        self.integration_layout.addWidget(self.stop_api_button)

        self.start_api_button.clicked.connect(self.start_api_server)
        self.stop_api_button.clicked.connect(self.stop_api_server)

        # Utilities Tab
        self.utilities_tab = QWidget()
        self.utilities_layout = QVBoxLayout()
        self.utilities_tab.setLayout(self.utilities_layout)

        self.clock_overlay = ClockOverlay()
        self.subtitle_manager = SubtitleManager()
        self.aspect_ratio_controller = AspectRatioController()

        self.add_clock_button = QPushButton("Add Clock Overlay")
        self.add_subtitles_button = QPushButton("Add Subtitles")
        self.change_aspect_ratio_button = QPushButton("Change Aspect Ratio")
        self.utilities_layout.addWidget(self.add_clock_button)
        self.utilities_layout.addWidget(self.add_subtitles_button)
        self.utilities_layout.addWidget(self.change_aspect_ratio_button)

        self.add_clock_button.clicked.connect(self.add_clock_overlay)
        self.add_subtitles_button.clicked.connect(self.add_subtitles)
        self.change_aspect_ratio_button.clicked.connect(self.change_aspect_ratio)

        # Adding all tabs to the main tab widget
        self.tabs.addTab(self.video_management_tab, "Video Management")
        self.tabs.addTab(self.ad_scheduling_tab, "Ad Scheduling")
        self.tabs.addTab(self.channel_branding_tab, "Channel Branding")
        self.tabs.addTab(self.playout_control_tab, "Playout Control")
        self.tabs.addTab(self.scheduling_tab, "Scheduling")
        self.tabs.addTab(self.output_settings_tab, "Output Settings")
        self.tabs.addTab(self.resource_management_tab, "Resource Management")
        self.tabs.addTab(self.customization_tab, "Customization")
        self.tabs.addTab(self.logging_reporting_tab, "Logging & Reporting")
        self.tabs.addTab(self.security_tab, "Security")
        self.tabs.addTab(self.backup_restore_tab, "Backup & Restore")
        self.tabs.addTab(self.integration_tab, "Integration")
        self.tabs.addTab(self.utilities_tab, "Utilities")

    # Video Management Functions
    def load_playlist(self):
        playlist = self.playlist_manager.load_playlist("playlist.json")
        if playlist:
            QMessageBox.information(self, "Playlist Loaded", f"Playlist loaded with {len(playlist)} videos.")

    def save_playlist(self):
        self.playlist_manager.save_playlist("playlist.json")
        QMessageBox.information(self, "Playlist Saved", "Playlist saved successfully.")

    def add_video_to_playlist(self):
        video_path, _ = QFileDialog.getOpenFileName(self, "Select Video", "", "Videos (*.mp4 *.avi *.mov *.mkv)")
        if video_path:
            self.playlist_manager.add_video(video_path)

    def remove_video_from_playlist(self):
        self.playlist_manager.remove_video()

    # Ad Scheduling Functions
    def add_ad(self):
        ad_path, _ = QFileDialog.getOpenFileName(self, "Select Advertisement", "", "Videos (*.mp4 *.avi *.mov *.mkv)")
        if ad_path:
            self.ad_manager.add_ad(ad_path)

    def schedule_ad(self):
        self.ad_scheduler.schedule_ad("ad.mp4", 10)

    def insert_ad(self):
        video_path, _ = QFileDialog.getOpenFileName(self, "Select Video", "", "Videos (*.mp4 *.avi *.mov *.mkv)")
        ad_path, _ = QFileDialog.getOpenFileName(self, "Select Ad", "", "Videos (*.mp4 *.avi *.mov *.mkv)")
        insertion_time, ok = QInputDialog.getInt(self, "Insert Ad", "Enter insertion time (seconds):")
        if ok:
            output_path, _ = QFileDialog.getSaveFileName(self, "Save Final Video", "", "Videos (*.mp4 *.avi *.mov *.mkv)")
            if video_path and ad_path and output_path:
                self.ad_inserter.insert_ad(video_path, ad_path, insertion_time, output_path)

    # Channel Branding Functions
    def add_logo_overlay(self):
        video_path, _ = QFileDialog.getOpenFileName(self, "Select Video", "", "Videos (*.mp4 *.avi *.mov *.mkv)")
        logo_path, _ = QFileDialog.getOpenFileName(self, "Select Logo", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if video_path and logo_path:
            output_path, _ = QFileDialog.getSaveFileName(self, "Save Video As", "", "Videos (*.mp4)")
            if output_path:
                self.logo_overlay.add_logo(video_path, logo_path, position=("right", "top"), output_path=output_path)

    def add_ticker(self):
        video_path, _ = QFileDialog.getOpenFileName(self, "Select Video", "", "Videos (*.mp4 *.avi *.mov *.mkv)")
        ticker_text, ok = QInputDialog.getText(self, "Add Ticker", "Enter ticker text:")
        if ok and video_path:
            output_path, _ = QFileDialog.getSaveFileName(self, "Save Video As", "", "Videos (*.mp4)")
            if output_path:
                self.ticker_manager.add_ticker(video_path, ticker_text, output_path=output_path)

    def add_watermark(self):
        video_path, _ = QFileDialog.getOpenFileName(self, "Select Video", "", "Videos (*.mp4 *.avi *.mov *.mkv)")
        watermark_path, _ = QFileDialog.getOpenFileName(self, "Select Watermark", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if video_path and watermark_path:
            output_path, _ = QFileDialog.getSaveFileName(self, "Save Video As", "", "Videos (*.mp4)")
            if output_path:
                self.watermark_manager.add_watermark(video_path, watermark_path, output_path=output_path)

    # Scheduling Functions
    def schedule_movie(self):
        movie_path, _ = QFileDialog.getOpenFileName(self, "Select Movie", "", "Videos (*.mp4 *.avi *.mov *.mkv)")
        start_time = datetime.now() + timedelta(seconds=30)  # Schedule to start in 30 seconds
        self.movie_scheduler.schedule_movie(movie_path, start_time)
        self.movie_scheduler.get_schedule()

    def start_execution(self):
        self.automated_executor.execute_schedule()

    def stop_execution(self):
        self.automated_executor.stop_execution()

    # Output Settings Functions
    def start_streaming(self):
        video_path, _ = QFileDialog.getOpenFileName(self, "Select Video", "", "Videos (*.mp4 *.avi *.mov *.mkv)")
        if video_path:
            udp_url = "udp://localhost:1234"  # Example UDP URL
            self.udp_streamer.start_streaming(video_path, udp_url)

    def save_video(self):
        video_path, _ = QFileDialog.getOpenFileName(self, "Select Video to Save", "", "Videos (*.mp4 *.avi *.mov *.mkv)")
        if video_path:
            output_path, _ = QFileDialog.getSaveFileName(self, "Save Video As", "", "Videos (*.mp4)")
            if output_path:
                self.file_output_manager.save_video(video_path, output_path)

    def change_resolution(self):
        video_path, _ = QFileDialog.getOpenFileName(self, "Select Video", "", "Videos (*.mp4 *.avi *.mov *.mkv)")
        if video_path:
            output_path, _ = QFileDialog.getSaveFileName(self, "Save Video As", "", "Videos (*.mp4)")
            if output_path:
                self.resolution_manager.change_resolution(video_path, output_path, width=1280, height=720)

    # Resource Management Functions
    def start_monitoring(self):
        cpu_usage = self.cpu_monitor.get_cpu_usage()
        memory_usage = self.memory_monitor.get_memory_usage()

        self.cpu_label.setText(f"CPU Usage: {cpu_usage}%")
        self.memory_label.setText(f"Memory Usage: {memory_usage}%")

        self.alert_system.check_resources(cpu_usage, memory_usage)

    # Customization Functions
    def save_profile(self):
        profile_name = "DefaultProfile"
        self.user_profile_manager.save_profile(profile_name)

    def load_profile(self):
        profile_name = "DefaultProfile"
        self.user_profile_manager.load_profile(profile_name)

    def delete_profile(self):
        profile_name = "DefaultProfile"
        self.user_profile_manager.delete_profile(profile_name)

    # Logging and Reporting Functions
    def log_activity(self):
        self.activity_logger.log_activity("User started video playback.")

    def report_error(self):
        try:
            # Simulate an error
            1 / 0
        except Exception as e:
            self.error_reporter.report_error(f"An error occurred: {e}")

    def log_playout(self):
        video_name = "example_video.mp4"
        self.playout_history_manager.log_playout(video_name)

    # Security Functions
    def register_user(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if self.auth_manager.register_user(username, password):
            self.access_control_manager.assign_role(username, "viewer")
            print(f"Assigned 'viewer' role to {username}.")

    def login_user(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if self.auth_manager.login(username, password):
            self.access_control_manager.check_permission(username, "play_video")

    def logout_user(self):
        self.auth_manager.logout()

    # Backup and Restore Functions
    def load_backups(self):
        backups = self.playlist_backup_manager.list_backups()
        self.backup_list.clear()
        self.backup_list.addItems(backups)

    def backup_playlist(self):
        playlist = ["video1.mp4", "video2.mp4", "video3.mp4"]  # Example playlist
        backup_name = "example_backup"
        self.playlist_backup_manager.backup_playlist(playlist, backup_name)
        self.load_backups()

    def restore_playlist(self):
        selected_backup = self.backup_list.currentItem()
        if selected_backup:
            backup_name = selected_backup.text().replace(".json", "")
            playlist = self.restore_manager.restore_playlist(backup_name)
            if playlist:
                QMessageBox.information(self, "Playlist Restored", f"Playlist restored: {playlist}")
        else:
            QMessageBox.warning(self, "No Selection", "Please select a backup to restore.")

    # Integration Functions
    def run_ffmpeg_command(self):
        command_args = ["-i", "input.mp4", "-vf", "scale=1280:720", "output.mp4"]
        self.ffmpeg_integration.execute_command(command_args)

    def start_api_server(self):
        api_thread = threading.Thread(target=self.api_support.start_api)
        api_thread.start()

    def stop_api_server(self):
        self.api_support.stop_api()

    # Utilities Functions
    def add_clock_overlay(self):
        video_path, _ = QFileDialog.getOpenFileName(self, "Select Video", "", "Videos (*.mp4 *.avi *.mov *.mkv)")
        if video_path:
            output_path, _ = QFileDialog.getSaveFileName(self, "Save Video As", "", "Videos (*.mp4)")
            if output_path:
                self.clock_overlay.add_clock_overlay(video_path, output_path)

    def add_subtitles(self):
        video_path, _ = QFileDialog.getOpenFileName(self, "Select Video", "", "Videos (*.mp4 *.avi *.mov *.mkv)")
        subtitle_path, _ = QFileDialog.getOpenFileName(self, "Select Subtitles", "", "Subtitles (*.srt)")
        if video_path and subtitle_path:
            output_path, _ = QFileDialog.getSaveFileName(self, "Save Video As", "", "Videos (*.mp4)")
            if output_path:
                self.subtitle_manager.add_subtitles(video_path, subtitle_path, output_path)

    def change_aspect_ratio(self):
        video_path, _ = QFileDialog.getOpenFileName(self, "Select Video", "", "Videos (*.mp4 *.avi *.mov *.mkv)")
        if video_path:
            output_path, _ = QFileDialog.getSaveFileName(self, "Save Video As", "", "Videos (*.mp4)")
            if output_path:
                self.aspect_ratio_controller.change_aspect_ratio(video_path, output_path, target_aspect_ratio=16/9)


if __name__ == '__main__':
    app = QApplication([])
    theme_customizer = ThemeCustomizer()
    theme_customizer.load_theme()  # Load the theme before showing the main window
    main_window = MainWindow()
    main_window.show()
    app.exec_()
