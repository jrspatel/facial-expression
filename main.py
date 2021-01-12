from flask import Flask ,render_template, Response
from camera import VideoCamera
app = Flask(__name__)

@app.route('/') #home page html file
def home():
    return render_template('homepage.html')

def gen(camera):
    while True:
        # get_frame is actually doing our prediction and detecting the faces and expression.
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame
               + b'\r\n\r\n')

@app.route('/video_feed')
# from homepage.html with the given url we are going to video_feed browser
# in video_feed we have videocamera function which is responsible for opening the webcam and closing.
def video_feed():
    return Response(gen(VideoCamera()),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)