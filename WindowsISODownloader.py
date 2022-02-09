def iso10():
    isodw = int(input("Select version: 10, 8, 7: "))
    if isodw >= 10:
        def archiso():
            archint = int(input("32 bit or 64?: "))
            if archint == 32:
                print("Download from here: http://gg.gg/xrs0e ")
            elif archint == 64:
                print("Download from here: http://gg.gg/xrs08 ")
        archiso()
    if isodw == 8:
        def archiso8():
            archint8 = int(input("64 bit or 32?: "))
            if archint8 == 64:
                print("Download from here: http://gg.gg/xrs01 ")
            elif archint8 == 32:
                print("Download the iso from here: http://gg.gg/xrs00 ")
        archiso8()
    if isodw == 7:
        def archiso7():
            archint7 = int(input("64 or 32 bit?: "))
            if archint7 == 64:
                print("Download the iso image from here: http://gg.gg/xrrzl ")
            if archint7 == 32:
                print("Download from here: http://gg.gg/xrrzq ")
        archiso7()
iso10()