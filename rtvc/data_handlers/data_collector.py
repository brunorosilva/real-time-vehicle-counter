import time

import requests


class VideoFeedCollector:
    def __init__(self, cam_number, base_url="http://cameras.cetsp.com.br/Cams/"):
        self.base_url = base_url
        self.cam_number = cam_number
        self.frames = []

    def _make_cam_url_for_current_frame(self, unix_timestamp):
        """
        Example: http://cameras.cetsp.com.br/Cams/23/1.jpg?1652843223334
        """
        current_frame_url = f"{str(self.base_url)}{self.cam_number}/{str((len(self.frames) + 1))}.jpg?{unix_timestamp}"
        return current_frame_url

    def _download_frame_jpeg(self, frame, unix_timestamp):
        with open(
            f"rtvc/data/{self.cam_number}-{unix_timestamp}.jpg", "wb"
        ) as current_frame_file:
            current_frame_file.write(frame.content)

    def get_current_frame(self):
        unix_timestamp = int(time.time())
        cam_url = self._make_cam_url_for_current_frame(unix_timestamp=unix_timestamp)
        frame = requests.get(cam_url, allow_redirects=True)
        self._download_frame_jpeg(frame=frame, unix_timestamp=unix_timestamp)
        self.frames.append(frame)


vdc = VideoFeedCollector(23)
for _ in range(3):
    vdc.get_current_frame()
    time.sleep(2)
