__author__ = 'reyoung'


class Singleton(object):
    """
    The Singleton class decorator.
    Like:
        from singleton.singleton import Singleton

        @Singleton
        class IntSingleton(object):
            def __init__(self):
                pass
    Use IntSingleton.instance() get the instance
    """
    def __init__(self, cls):
        """
        :param cls: decorator class type
        """
        self.__cls = cls
        self.__instance = None

    def initialize(self, *args, **kwargs):
        """
        Initialize singleton object if it has not been initialized
        :param args: class init parameters
        :param kwargs: class init parameters
        """
        if not self.is_initialized():
            self.__instance = self.__cls(*args, **kwargs)

    def is_initialized(self):
        """
        :return: true if instance is initialized
        """
        return self.__instance is not None

    def instance(self):
        """
        Get singleton instance
        :return: instance object
        """
        if not self.is_initialized():
            self.initialize()
        return self.__instance

    def __call__(self, *args, **kwargs):
        """
        Disable new instance of original class
        :raise TypeError:
        """
        raise TypeError("Singletons must be access by instance")

    def __instancecheck__(self, inst):
        """
        Helper for isinstance check
        """
        return isinstance(inst, self.__cls)