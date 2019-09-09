#
def powerResidue(N, seed=None, a=273673163155, c=13, M=2**48):
    """ Calculate a series of random numbers
    """
    import datetime
    if seed == None:
        print("Seed value set to NONE, defaulting to system time.")
        seed=int(datetime.datetime.now().strftime("%Y%m%d%H%M%s"))
    else:
        pass

    r = seed
    rand = []
    for i in range(N):
        rand.append(((a*r + c) % M)/M)
        r = (a*r + c) % M
    return rand[0:N]
