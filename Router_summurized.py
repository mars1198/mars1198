def checkio(data):
    lst = ["".join(bin(int(octet))[2:].zfill(8) for octet in addr.split(".")) for addr in data]
    bDiffFound = False
    sIp = ""
    iSum = 0
    for i in range(32):
        if not bDiffFound and all(addr[i] == lst[0][i] for addr in lst):
            sIp += lst[0][i]
        else:
            if not bDiffFound:
                iSum = i
            sIp += "0"
            bDiffFound = True
    return "{}.{}.{}.{}/{}".format(int(sIp[:8], 2), int(sIp[8:16], 2), int(sIp[16:24], 2), int(sIp[24:], 2), iSum)
