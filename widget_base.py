class Widget:
    def __init__(self, x=0, y=0, **kwargs):
        self.x = x
        self.y = y
    def render(self):
        return 'widget'
