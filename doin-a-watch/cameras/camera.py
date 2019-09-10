import time

# import picamera
import camera as picamera

from cameras.base import BaseCamera


class Camera(BaseCamera):
    @staticmethod
    def frames():
        with picamera.PiCamera() as camera:
            # let camera warm up
            time.sleep(2)
            stream = io.BytesIO()
            for _ in camera.capture_continuous(output=stream,
                                               format='jpeg',
                                               use_video_port=True,
                                               resize=(480, 280)):
                # return current frame
                stream.seek(0)
                yield stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()
