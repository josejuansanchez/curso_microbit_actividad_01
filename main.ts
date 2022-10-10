input.onGesture(Gesture.Shake, function () {
    basic.showIcon(IconNames.Heart)
    basic.showIcon(IconNames.SmallHeart)
    basic.showIcon(IconNames.Heart)
    basic.showString("" + (respuestas._pickRandom()))
})
let respuestas: string[] = []
respuestas = [
"Sí",
"No",
"Tal vez",
"Buenos días",
"Buenas tardes"
]
