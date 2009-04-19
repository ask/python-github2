from datetime import datetime

GITHUB_TIMEZONE = "-0700"
GITHUB_DATE_FORMAT = "%Y/%m/%d %H:%M:%S"


def ghdate_to_datetime(github_date):
    date_without_tz = github_date.rsplit("-")[0].strip()
    return datetime.strptime(date_without_tz, GITHUB_DATE_FORMAT)


def datetime_to_ghdate(datetime_):
    date_without_tz = datetime_.strftime(GITHUB_DATE_FORMAT)
    return " ".join([date_without_tz, GITHUB_TIMEZONE])


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


def doc_generator(docstring, attributes):
    docstring = docstring or ""
    def section(title):
        return "\n".join([title, "-" * len(title)])

    def bullet(title, text):
        return """    *``%s``*\n      %s\n""" % (title, text)

    a = section("Attributes")
    b = "\n".join([bullet(attr_name, attr.help)
                    for attr_name, attr in attributes.items()])
    return "\n".join([docstring, a, b])


class Attribute(object):

    def __init__(self, help):
        self.help = help

    def to_python(self, value):
        return value

    from_python = to_python


class DateAttribute(Attribute):

    def to_python(self, value):
        if value and not isinstance(value, datetime):
            return ghdate_to_datetime(value)
        return value

    def from_python(self, value):
        if value and isinstance(value, datetime):
            return datetime_to_ghdate(value)
        return value


class BaseDataType(type):

    def __new__(cls, name, bases, attrs):
        super_new = super(BaseDataType, cls).__new__

        _meta = dict([(attr_name, attr_value)
                        for attr_name, attr_value in attrs.items()
                            if isinstance(attr_value, Attribute)])
        attrs["_meta"] = _meta
        attributes = _meta.keys()
        attrs.update(dict([(attr_name, None)
                        for attr_name in attributes]))

        def _contribute_method(name, func):
            func.func_name = name
            attrs[name] = func

        def constructor(self, **kwargs):
            for attr_name, attr_value in kwargs.items():
                if attr_name not in self._meta:
                    raise TypeError("%s.__init__() doesn't support the "
                                    "%s argument." % (cls_name, attr_name))
                attr = self._meta[attr_name]
                setattr(self, attr_name, attr.to_python(attr_value))

        _contribute_method("__init__", constructor)

        def to_dict(self):
            _meta = self.meta
            dict_ = vars(self)
            return dict([(attr_name, _meta[attr_name].from_python(attr_value))
                            for attr_name, attr_value in dict_.items()])
        _contribute_method("__dict__", to_dict)

        def iterate(self):
            not_empty = lambda e: e is not None
            return iter(filter(not_empty, vars(self).items()))
        _contribute_method("__iter__", iterate)

        result_cls = super_new(cls, name, bases, attrs)
        result_cls.__doc__ = doc_generator(result_cls.__doc__, _meta)
        return result_cls

    def contribute_method_to_cls(cls, name, func):
        func.func_name = name
        return func


class BaseData(object):
    __metaclass__ = BaseDataType
