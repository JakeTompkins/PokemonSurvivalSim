from threading import Timer


class Ticker:
    def __init__(self, interval, function):
        self.interval = interval
        self.running = False
        self.timer = None
        self.function = function

    def start(self):
        if not self.running:
            self.timer = Timer(self.interval, self.function)
            self.timer.start()
            self.running = True

    def stop(self):
        self.timer.cancel()
        self.running = False
