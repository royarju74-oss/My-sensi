# ONLY REPLACE generate_best_sensi FUNCTION
# KEEP SAME INTERFACE

def generate_best_sensi(device, ram, style):

    device = device.lower().strip()

    # DEFAULT PRO SETTINGS

    general = 188
    red_dot = 192
    scope2x = 178
    scope4x = 166

    fire_button = 54
    dpi = 650

    ai_mode = "BALANCED AI"

    # DEVICE SYSTEM

    ultra_devices = [
        "iphone",
        "iqoo",
        "rog",
        "oneplus",
        "redmagic",
        "s24",
        "pixel",
        "realme gt",
        "poco f"
    ]

    low_devices = [
        "j2",
        "j5",
        "a03",
        "a10",
        "c11",
        "c21",
        "narzo c"
    ]

    # HIGH END DEVICES

    if any(x in device for x in ultra_devices):

        general = 198
        red_dot = 200
        scope2x = 190
        scope4x = 180

        fire_button = 47
        dpi = 720

        ai_mode = "ULTRA AI"

    # LOW END DEVICES

    elif any(x in device for x in low_devices):

        general = 172
        red_dot = 165
        scope2x = 154
        scope4x = 145

        fire_button = 63
        dpi = 540

        ai_mode = "LITE AI"

    # RAM OPTIMIZATION

    if ram == "4GB":

        general -= 4
        red_dot -= 4
        scope2x -= 2

        dpi -= 15

    elif ram == "6GB":

        general += 2
        red_dot += 2
        scope2x += 2

        dpi += 5

    elif ram == "8GB":

        general += 5
        red_dot += 6
        scope2x += 5

        dpi += 20

    # GAMEPLAY AI

    # ACCURACY MODE
    # BEST BALANCED HEADSHOT

    if style == "ACCURACY":

        general += 4
        red_dot += 8
        scope2x += 6
        scope4x += 3

        fire_button = 51

        ai_mode = "ACCURACY AI"

    # FREE STYLE
    # FAST MOVEMENT + HEADSHOT

    elif style == "FREE STYLE":

        general += 6
        red_dot += 10
        scope2x += 5

        fire_button = 56

        ai_mode = "FREESTYLE AI"

    # SMOOTH AIM
    # EASY DRAG + STABLE AIM

    elif style == "SMOOTH AIM":

        general += 5
        red_dot += 9
        scope2x += 7
        scope4x += 4

        fire_button = 49

        ai_mode = "SMOOTH AIM AI"

    # SAFE LIMIT SYSTEM
    # NEVER OVER 200

    general = max(100, min(general, 200))
    red_dot = max(100, min(red_dot, 200))
    scope2x = max(100, min(scope2x, 200))
    scope4x = max(100, min(scope4x, 200))

    fire_button = max(35, min(fire_button, 70))
    dpi = max(400, min(dpi, 800))

    return {

        "general": general,
        "red_dot": red_dot,
        "scope2x": scope2x,
        "scope4x": scope4x,

        "fire_button": fire_button,
        "dpi": dpi,

        "ai_mode": ai_mode

    }
