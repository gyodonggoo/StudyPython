import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.start_preview()
    camera.exposure_compensation = 2
    camera.exposure_mode = 'spotlight'
    camera.meter_mode = 'matrix'
    camera.image_effect = 'gpen'
    time.sleep(2)
    camera.exif_tags['IFD0.Artist'] = 'Kim'
    camera.exif_tags['IFD0.Copyright'] = 'Copyleft Kim'
    camera.capture('foo.jpg')
    camera.stop_preview()