# Name: Spencer Lawry     
# Course: CPE 101  
# Instructor: Daniel Kauffman
# Assignment: Pixel Magic 
# Term: Fall 2016        

def main():
    import sys
    arg_list = sys.argv
    if len(arg_list) < 3 or len(arg_list) > 6 or\
       len(arg_list) >= 3 and ('-d' not in arg_list and\
                              '-f' not in arg_list):
            
        print 'Usage: python pixel_magic.py <image> <flag>'
        print 'flags:\n-d for decode\n-f for fade'
        return

    if '-d' in arg_list:
        we_are_decoding = True
        arg_list.remove('-d')
    else: 
        we_are_decoding = False

    if '-f' in arg_list:
        we_are_fading = True
        arg_list.remove('-f')
        if not len(arg_list) == 5:
            print 'Usage: python pixel_magic.py <image> <row> <column> '\
                   '<radius> -f' 
            return 

        for thing in arg_list[2:]:
            if not thing.isdigit():
                print 'Usage: python pixel_magic.py <image> <row> <column> '\
                   '<radius> -f' 
                print 'Error: Image, row and column values must be integers'
                return 
    else:
        we_are_fading = False

    try:
        pixels = read_image(arg_list[1])
        header_stuff = pixels[0:3] 
        del pixels[0:3]
        grouped_pixels = groups_of_3(pixels)
        if we_are_decoding:
            decoded_puzzle = decode_puzzle(grouped_pixels)
            write_image('decoded.ppm',decoded_puzzle,header_stuff)
        if we_are_fading:
            faded_image = fade_image(grouped_pixels,int(arg_list[2]),\
                          int(arg_list[3]),int(arg_list[4]),header_stuff) 
            write_image('faded.ppm',faded_image,header_stuff)

    except:
        print 'Unable to open {0}'.format(arg_list[1])


def read_image(file_name):
    f = open(file_name, 'r')
    file_type = f.readline() #Taking out P3

    data_list = []
    while True:
        line = f.readline()
        if line == '':
            break
        line_list = line.split()
        for sub_comp in line_list:
            data_list.append(int(sub_comp))
    f.close()
    return data_list 



def write_image(file_name,grouped_pixels,header_stuff):
    f = open(file_name, 'w')
    f.write('P3\n')
    f.write('{0} {1}\n'.format(header_stuff[0],header_stuff[1]))
    f.write('{0}\n'.format(header_stuff[2]))
    for pixel_list in grouped_pixels:
        for pixel in pixel_list: 
            f.write('{0:d}\n'.format(pixel))
    f.close()

def groups_of_3(seq):
    i = 0                                                                       
    full_list = []                                                              
    sub_list = []                                                               
    for num in seq:                                                          
        i += 1                                                                  
        if i <= 3:                                                              
            sub_list.append(num)                                                
        else:                                                                   
            full_list.append(sub_list)                                          
            sub_list = []                                                       
            sub_list.append(num)                                                
            i = 1                                                               
    return full_list + [sub_list] 
    
def decode_puzzle(grouped_pixels):
   for pixels in grouped_pixels:
        pixels[0] = pixels[0]*10
        if pixels[0] > 255:
            pixels[0] = 255
        pixels[1] = pixels[0]
        pixels[2] = pixels[0]
   return grouped_pixels

def fade_image(grouped_pixels, fade_y, fade_x, fade_radius, header_stuff):
    picture_width = header_stuff[0] 
    for i, pixels in enumerate(grouped_pixels):
        pixel_y = i / picture_width
        pixel_x = i % picture_width 
        dist_x = pixel_x - fade_x
        dist_y = pixel_y - fade_y
        distance = ((dist_x)**2 + (dist_y)**2)**0.5   
        scale_value = (fade_radius - distance) / fade_radius
        if scale_value < 0.2:
            scale_value = 0.2

        pixels[0] = int(pixels[0]*scale_value)
        pixels[1] = int(pixels[1]*scale_value)
        pixels[2] = int(pixels[2]*scale_value)
    return grouped_pixels







if __name__== "__main__":
    main()
