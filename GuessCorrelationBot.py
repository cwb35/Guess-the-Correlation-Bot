# -*- coding: utf-8 -*-
import pyautogui, time
from scipy import stats
import sys
import argparse

def get_mouse_coordinates():
    """
    Simple script for getting mouse coordinates.
    """
    print('Returning Mouse Coordinates. Press Ctrl-C to quit.')
    try:
        while True:
            # Get and print the mouse coordinates.
            x, y = pyautogui.position()
            positionStr = 'X: {} Y: {}'.format(str(x).rjust(4), str(y).rjust(4))
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    
    except KeyboardInterrupt:
        print('\nDone')

def run(num, topleft, botright):
    """
    Scans the pixels in the coordinate box given, then plots a line that goes
    through the black pixels, and then types in the rvalue.
    
    Arguments:
    num -- Number of loops the program runs
    topleft -- x,y coordinates for the top left corner of the gamebox
    botright -- x,y coordinates for the botttom right corner of gamebox
    """
    x_frame = topleft[0] #Top left corner x-coordinate for gamebox
    y_frame = topleft[1] #Top Left corner y-coordinate for gamebox
    
    x_range = botright[0] - x_frame #X length of gamebox
    y_range = botright[1] - y_frame #Y Length of gamebox
    
    time.sleep(5)
    
    for i in range(num):
        im = pyautogui.screenshot()
        my_x_points = []
        my_y_points = []
        for c in range(int(x_range/4)):
            for r in range(int(y_range/4)):
                
                #Checking color of pixel
                if im.getpixel((x_frame+(4*c), y_frame+(4*r)))[0] < 128:
                    my_x_points.append(x_range-(4*c))
                    my_y_points.append((4*r))
        
        #Running a line through the points
        my_line = stats.linregress(my_x_points, my_y_points)
        
        if str(round(my_line.rvalue,2))[2:] == '0':
            pyautogui.typewrite(['backspace', 'backspace', '1'], interval=.05)
        else:
            pyautogui.typewrite(str(round(my_line.rvalue,2))[2:], interval=.05)
            
        pyautogui.typewrite(['enter'], interval=.05)
        pyautogui.typewrite(['enter'], interval=.05)
        time.sleep(1)

def main():
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('program', metavar='PROG', type=str)
    parser.add_argument('n', metavar='NUM', type=int)
    parser.add_argument('topleft', metavar='TL', type=int, nargs=2)
    parser.add_argument('botright', metavar='BR', type=int, nargs=2)
    parser.add_argument('-get_coords', metavar='gc', type=str)
    
    arg_dict = vars(parser.parse_args(sys.argv))
    
    params = {
        'num': arg_dict['n'],
        'topleft':(arg_dict['topleft']),
        'botright':(arg_dict['botright'])
        }
    if arg_dict['get_coords'] == "True":
        get_mouse_coordinates()
    else:
        run(**params)
    
if __name__ == '__main__':
    main()
