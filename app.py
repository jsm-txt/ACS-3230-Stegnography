from PIL import Image, ImageDraw, ImageFont

def decode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    """
    # Open the image using PIL:
    encoded_image = Image.open(path_to_png)

    # Separate the red channel from the rest of the image:
    red_channel = encoded_image.split()[0]

    # Create a new PIL image with the same size as the encoded image:
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    x_size, y_size = encoded_image.size

    # TODO: Using the variables declared above, replace `print(red_channel)` with a complete implementation:
    #print(red_channel)  # Start coding here!
    # for i in red_channel:
    #     print(i)
    #print(decoded_image)
    pix_val = list(red_channel.getdata())
    print(x_size)
    print(y_size)
    new_arr = []
    for i in pix_val:
        new_arr.append(bin(i))
    #print(new_arr)
    counter = 0 
    y= 0
    x= 0
    
    while y < y_size-1:
        while x < x_size-1:
            if new_arr[counter][-1] == '0':
                pixels[x,y]=  (0, 0, 0)
                counter += 1
                x += 1
            else:
                pixels[x,y]= (255, 255, 255) 
                counter += 1
                x+=1
        y += 1
        x = 0


    # DO NOT MODIFY. Save the decoded image to disk:
    decoded_image.save("decoded_image.png")


def encode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    """
    pass


def write_text(text_to_write):
    """
    TODO: Add docstring and complete implementation.
    """


    image = Image.new("RGB", (400,351)) 

    draw = ImageDraw.Draw(image) 
    
    text = 'hellooo \n world'
    
    # drawing text size
    draw.text((5, 5), text, fill ="white", align ="right") 
    
    image.show()

    encoded_image = Image.open('./encoded_sample.png')

    red_channel = encoded_image.split()[0]

    pixels = image.load()
    x_size, y_size = encoded_image.size
    
    # pixels = image.load()
    # x_size, y_size = image.size
    # counter = 0 
    # y= 0
    # x= 0
    
    # while y < y_size-1:
    #     while x < x_size-1:
    #         if new_arr[counter][-1] == '0':
    #             pixels[x,y]=  (0, 0, 0)
    #             counter += 1
    #             x += 1
    #         else:
    #             pixels[x,y]= (255, 255, 255) 
    #             counter += 1
    #             x+=1
    #     y += 1
    #     x = 0

decode_image('./encoded_sample.png')
write_text('ll')