import cv2
import datetime

cap = cv2.VideoCapture(0)

if not cap:
    print('camera not found')
    exit()

video_type = 'normal'
print('1 - original')
print('2 - b/w')
print('3 - blur')
print('4 - contour')
print('q - exit')





frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_fps = int(cap.get(cv2.CAP_PROP_FPS))


if frame_fps == 0:
    frame_fps = 30.0

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('test_video.mp4', fourcc, frame_fps, (frame_width, frame_height))

while True:
    ret, frame = cap.read()
    if not ret:
        print('frame not found')
        break

    text = datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S')
    cv2.putText(frame, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (255,255,255), 2 )
    if video_type == 2:
        filter_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif video_type == 3:
        filter_frame = cv2.GaussianBlur(frame, (25, 25), 0)
    elif video_type == 4:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        filter_frame = cv2.Canny(gray, 100, 100, )
    else:
        filter_frame = frame


    cv2.imshow('test video', filter_frame)

    out.write(frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('1'):
        video_type = 1
    elif key == ord('2'):
        video_type = 2
    elif key == ord('3'):
        video_type = 3
    elif key == ord('4'):
        video_type = 4
    elif key == ord('q'):
        break


    if cv2.waitKey(1) & ord('q') == 0xFF:
        break


cap.release()
out.release()
cv2.destroyAllWindows()