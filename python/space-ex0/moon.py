class Moon(object):
    RADIUS = 3475*1000
    ACC = 1.622
    EQ_SPEED = 1700

    @classmethod
    def getAcc(cls, speed):
        n = abs(speed)/cls.EQ_SPEED
        return (1.0-n)*cls.ACC