import datetime
def ctime(D,H,M):
    a = datetime.datetime(11, 11, 11, 11, 11, 0)
    b = datetime.datetime(11, 11, D, H, M, 0)

    c = a-b
    return c
