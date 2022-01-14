"""SceneSwitch_1"""
def main():
    """Docstring"""
    warm = 0
    switch = 0
    cool = 0
    dayligth = 0
    while 1:
        sec = input()
        if sec == "End":
            print(warm)
            break
        else:
            sec = float(sec)
            if switch == 0:
                switch = 1
                if sec-dayligth <= 6 and cool == 1:
                    cool = 0
                    warm += 1
                else:
                    cool = 1
            elif switch == 1:
                switch = 0
                dayligth = float(sec)
main()
