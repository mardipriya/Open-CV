import cv2
import handy
import vlc
player = vlc.MediaPlayer('Videos/.mp4')
player.play()
cap = cv2.VideoCapture(0)
hist = handy.capture_histogram(source=0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    handy.detect_face(frame, block=True)
    hand = handy.detect_hand(frame, hist)
    custom_outline = hand.draw_outline(min_area=10000, color=(0, 255, 255), thickness=2)
    quick_outline = hand.outline
    for fingertip in hand.fingertips:cv2.circle(quick_outline, fingertip, 5, (0, 0, 255), -1)
    com = hand.get_center_of_mass()
    #print(hand.fingertips)
    print(com)
    if com != None:
        if com[0]<100:
            print('left')
            player.set_time(player.get_time() - 2000)
        if com[0]>500:
            print('right')
            player.set_time(player.get_time() + 2000)
        if com[1]<100:
            print('up')
            player.audio_set_volume(200)
        if 100< com[1] < 200:
            print('up')
            player.audio_set_volume(150)
        if 300< com[1] < 400:
            print('up')
            player.audio_set_volume(70)
        if com[1] > 500:
            print('up')
            player.audio_set_volume(0)
        if com[1]>500:
            print('down')
            player.set_time(player.get_time() + 2000)
    else:
        player.pause()
    if com:
        cv2.circle(quick_outline, com, 10, (255, 0, 0), -1)
    quick_outline = cv2.resize(quick_outline, (300,200), interpolation = cv2.INTER_AREA)
    cv2.imshow("Handy", quick_outline)
    k = cv2.waitKey(5)

    # Press 'q' to exit
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()