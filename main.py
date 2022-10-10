def on_gesture_shake():
    basic.show_icon(IconNames.HEART)
    basic.show_icon(IconNames.SMALL_HEART)
    basic.show_icon(IconNames.HEART)
    basic.show_string("" + (respuestas._pick_random()))

input.on_gesture(Gesture.SHAKE, on_gesture_shake)

respuestas: List[str] = []
respuestas = ["Sí", "No", "Tal vez", "Buenos días", "Buenas tardes"]