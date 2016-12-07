import os
import os.path
import shutil
import time
from getImg import *


def call():
    os.unlink("aero.theme")
    os.system("aero_new.theme")
    time.sleep(0.4)
    os.rename("aero_new.theme", "aero.theme")


def change_theme(emotion):
    print("Applying to system...")

    current_working_dir = os.getcwd()
    sys_theme_path = os.environ["appdata"] + "/../Local/Microsoft/Windows/Themes/"
    if not os.path.exists(sys_theme_path + "aero.theme"):
        shutil.copy("aero.theme", sys_theme_path + "aero.theme")

    emotion_set = {"anger": 0, "contempt": 1, "disgust": 2, "fear": 3, "happiness": 4, "neutral": 5, "sadness": 6,
                   "surprise": 7}
    emotion_colors = {0: "0x008080", 1: "0x007A11", 2: "0x003355", 3: "0x660066", 4: "0x800000",
                      5: "0x997300",
                      6: "0xe65c00", 7: "0x829900"}

    # emotion = 'neutral'
    wallpaper_path = ''

    wallpaper_path = getImg(emotion_colors[emotion_set[emotion]])
    wallpaper_path = current_working_dir + "/" + wallpaper_path
    os.chdir(sys_theme_path)

    theme_path = ""
    desktop = "[Control Panel\Desktop]\n"
    wallpaper = "Wallpaper="
    style = "[VisualStyles]\n"
    stylecolor = "ColorizationColor="

    f = open(theme_path + "aero.theme", 'r+')
    w = open(theme_path + "aero_new.theme", "w")
    while True:
        line = f.readline()
        w.write(line)
        if line.startswith(';'):
            continue
        if len(line) == 0:
            break
        if line == desktop:
            flag = False
            while flag == False:
                inner_line = f.readline()
                if inner_line.startswith(';'):
                    w.write(inner_line)
                    continue
                if inner_line.startswith('\n'):
                    w.write(inner_line)
                    break
                if inner_line[0:len(wallpaper)] == wallpaper:
                    w.write(wallpaper)

                    w.write(wallpaper_path + "\n")
                    flag = True
                else:
                    w.write(inner_line)

        elif line == style:
            flag = False
            while flag == False:
                inner_line = f.readline()
                if inner_line.startswith(';'):
                    w.write(inner_line)
                    continue
                if inner_line.startswith('\n'):
                    w.write(inner_line)
                    break
                if inner_line[0:len(stylecolor)] == stylecolor:
                    w.write(stylecolor)
                    w.write(emotion_colors[emotion_set[emotion]] + "\n")
                    flag = True
                else:
                    w.write(inner_line)
        else:
            continue
    f.close()
    w.close()
    call()

    os.chdir(current_working_dir)
