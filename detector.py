import cv2


def detect_cards(image, bbox):
    base_left, base_top, base_right, base_bottom = bbox

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(
        blurred,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY_INV,
        11,
        3
    )

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    card_regions = []
    fixed_w = fixed_h = -1

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = w / h
        if 50 < w < 200 and 0.7 < aspect_ratio < 0.9:
            if fixed_w < 0:
                fixed_w = w
                fixed_h = h
            card_regions.append((x, y, fixed_w, fixed_h))

    print(f'{len(card_regions)} cards detected.')

    def get_cropped_image(region):
        x, y, w, h = region
        center = (base_left + x + w // 2, base_top + y + h // 2)
        cropped = image[y:y + h, x:x + w]
        return {'img': cropped, 'pos': center}

    card_images = [get_cropped_image(region) for region in card_regions]

    return card_images
