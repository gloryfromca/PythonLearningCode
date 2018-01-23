class WebFramework(object):
    def __init__(self, name='Flask'):
        self.name = name

    def __get__(self, instance, owner):
        return self.name

    def __set__(self, instance, value):
        self.name = value


class PythonSite(object):

    webframework = WebFramework()

pythonsite = PythonSite()
webframework = WebFramework()

print(webframework.__get__(webframework, WebFramework))
print(webframework.__get__(pythonsite, PythonSite))


