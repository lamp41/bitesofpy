from datetime import datetime
from datetime import timedelta

NOW = datetime.now()


class Promo:
    @property
    def expired(self):
        global NOW
        if self._expired == True:
            return True
        else:
            print('NOW: ' + str(NOW))
            print('datetime: ' + str(self.expired_time))
            if NOW < self.expired_time:
                return False
            else:
                self._expired == True
                return True

    def __init__(self, name, expired_time):
        self.name = name
        self.expired_time = expired_time
        self._expired = None
    
expired_time = NOW + timedelta(seconds=5)
twitter_promo = Promo('twitter', expired_time)
print(twitter_promo.expired)