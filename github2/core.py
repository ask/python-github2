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


class BaseDataType(type):

    def __new__(cls, name, bases, attrs):
        super_new = super(BaseDataType, cls).__new__

        attributes = attrs.pop("attributes", tuple())
        date_attributes = set(attrs.pop("date_attributes", tuple()))
        attrs.update(dict([(attr_name, None)
                        for attr_name in attributes]))

        def _contribute_method(name, func):
            func.func_name = name
            attrs[name] = func

        def constructor(self, **kwargs):
            for attr_name, attr_value in kwargs.items():
                if attr_name not in attributes:
                    raise TypeError("%s.__init__() doesn't support the "
                                    "%s argument." % ( cls_name, attr_name))
                setattr(self, attr_name, attr_value)

            # Convert dates to datetime objects.
            for date_attr_name in date_attributes:
                attr_value = getattr(self, date_attr_name)
                if attr_value and not isinstance(attr_value, datetime):
                    date_as_datetime = ghdate_to_datetime(attr_value)
                    setattr(self, date_attr_name, date_as_datetime)
        _contribute_method("__init__", constructor)

        def iterate(self):
            not_empty = lambda e: e is not None
            objdict = vars(self)
            for date_attr_name in date_attributes:
                date_value = objdict.get(date_attr_name)
                if date_value and isinstance(date_value, datetime):
                    objdict[date_attr_name] = datetime_to_ghdate(date_value)

            return iter(filter(not_empty, objdict.items()))
        _contribute_method("__iter__", iterate)

        return super_new(cls, name, bases, attrs)

    def contribute_method_to_cls(cls, name, func):
        func.func_name = name
        return func

class BaseData(object):
    __metaclass__ = BaseDataType
