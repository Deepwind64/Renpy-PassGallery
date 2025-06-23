init python:
    import threading
    from time import sleep
    from datetime import datetime

    def unlock_all():
        c=0
        CG_key = []
        for key,value in persistent.__dict__.items():
            if type(value)==bool and key.startswith("CG_"):
                c+=1
                CG_key.append(key)
                persistent.__dict__[key] = True

        fprint("Changed variables count: {}\n".format(c))
        fprint("Changed variables is as follow.\n")
        fprint(CG_key)
        fprint("\n")

    def fprint(s):
        with open("unlock-log.txt","a+") as f:
            f.write(str(s))

    def log_time():
        fprint("Unlock logging time: {}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def unlock_cg():
        c=0
        while True:
            try:
                sleep(2)
                if len(persistent.__dict__)>0:
                    fprint("Detect persitent successfully.\n")
                    unlock_all()
                    fprint("Unlock CG successfully.\n\n")
                    break
                if c>5:
                    raise RuntimeError("Unlock Failed, exceeded the maximum retry count.")
                c+=1
            except Exception as e:
                fprint(e)

    t = threading.Thread(target=unlock_cg)
    t.start()
