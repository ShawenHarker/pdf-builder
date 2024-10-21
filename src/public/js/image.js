const findDotPlacement = () => {
    let d = 51;
    let i = 80;
    let s = 35;
    let c = 69;
    let size = c;
    let subtractedValue = 100 - size;
    let angleDeg;
    let pointY
    let pointX

    const centerX = 250;
    const centerY = 250;
    const r = 165;

    switch (size) {
        case d:
            angleDeg = 315;
            break;
        case i:
            angleDeg = 45;
            break;
        case s:
            angleDeg = 135;
            break;
        case c:
            angleDeg = 225;
            break;
        default:
            angleDeg = 0;
    }

    const radians = angleDeg * (Math.PI / 180);

    switch (size) {
        case d:
        case i:
            pointY = centerY - (Math.cos(radians) * r) + subtractedValue;
            break;
        case s:
        case c:
            pointY = centerY - (Math.cos(radians) * r) - subtractedValue;
            break;

        default:
            pointY = 0;
    }

    switch (size) {
        case d:
        case c:
            pointX = centerX + (Math.sin(radians) * r) + subtractedValue;
            break;
        case s:
        case i:
            pointX = centerX + (Math.sin(radians) * r) - subtractedValue;
            break;

        default:
            pointX = 0;
    }

    const dot = document.getElementById("dot");
    dot.style.top = `${Math.floor(Math.round(pointY))}px`;
    dot.style.left = `${Math.floor(Math.round(pointX))}px`;
};

findDotPlacement();