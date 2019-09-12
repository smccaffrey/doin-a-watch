### sam
### video streaming
from flask import Flask, render_template, Response

from cameras.camera import Camera

app = Flask(__name__)

@app.route('/')
def index():
    while True:
        return render_template('index.html')

def gen(camera):
    while True:
        # rval, frame = vc.read()
        frame = camera.get_frame()
        # cv2.imwrite('pic.jpg', frame)
        yield (b'--frame\r\n' 
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
               
@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    #app.run(host='0.0.0.0', debug=True, threaded=True)
    app.run(port=5001, threaded=True)
    