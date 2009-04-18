class GithubCommand(object):

    def __init__(self, request):
        self.request = request

    def make_request(self, command, *args, **kwargs):
        filter = kwargs.get("filter")
        post_data = kwargs.get("post_data")
        if post_data:
            response = self.request.post(self.domain, command, *args,
                                         **post_data)
        else:
            response = self.request.get(self.domain, command, *args)
        if filter:
            return response[filter]
        return response

    def get_value(self, *args, **kwargs):
        datatype = kwargs.pop("datatype", None)
        value = self.make_request(*args, **kwargs)
        if datatype:
            return datatype(**value)
        return value

    def get_values(self, *args, **kwargs):
        datatype = kwargs.pop("datatype", None)
        values = self.make_request(*args, **kwargs)
        if datatype:
            return [datatype(**value) for value in values]
        return values


class BaseDataType(type):

    def __new__(cls, name, bases, attrs):
        super_new = super(BaseDataType, cls).__new__

        attributes = attrs.pop("attributes", tuple())
        attrs.update(dict([(attr_name, None)
                        for attr_name in attributes]))

        def constructor(self, **kwargs):
            for attr_name, attr_value in kwargs.items():
                if attr_name not in attributes:
                    raise TypeError("%s.__init__() doesn't support the "
                                    "%s argument." % ( cls_name, attr_name))
                setattr(self, attr_name, attr_value)
        attrs["__init__"] = constructor

        def to_dict(self):
            dict_ = {}
            for attr_name in self.attributes:
                attr_value = getattr(self, attr_name, None)
                if attr_value is not None:
                    dict_[attr_name] = attr_value
            return dict_
        attrs["to_dict"] = to_dict

        return super_new(cls, name, bases, attrs)


class BaseData(object):
    __metaclass__ = BaseDataType
