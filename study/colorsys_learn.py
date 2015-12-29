#!/usr/bin/env python


import colorsys

def get_dominant_color(image):
    
    image = image.convert("RGBA")
    
    image.thumbnail((200,200))

    max_score = None

    dominant_color = None

    for count,(r,g,b,a) in image.getcolors(image.size[0]*image.size[1]):
        if a == 0:
            continue

        saturation = colorsys.rgb_to_hsv(r/255.0,g/255.0,b/255.0)[1]
        
        y = min(abs(r*2104 + g*4130 + b*802 + 4096 + 131072 ) >> 13,235)
    
        y = (y-16.0)/(235-16)

        if y > 0.9:
            continue


        score = (saturation + 0.1)* count

        if score > max_score:
            max_score = score
            dominant_color=(r,g,b)
    return dominant_color


if __name__ == "__main__":
    from PIL import Image

    print get_dominant_color(Image.open("image.jpg"))

