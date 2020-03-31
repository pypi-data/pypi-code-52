from astropy.io.fits import Header


class SourceBase:
    pass


class ImagePlaneBase:
    pass


class FieldOfViewBase:
    pass


class DetectorBase:
    pass


class PoorMansHeader:
    def __init__(self, dic=None):
        self.comments = {}
        self.dic = {}

        if dic is not None:
            self.update(dic)

    def update(self, obj):

        if isinstance(obj, PoorMansHeader):
            self.dic.update(obj.dic)
            self.comments.update(obj.comments)

        if isinstance(obj, Header):
            comments = {key: obj.comments[key] for key in obj
                        if obj.comments[key] != ""}
            self.comments.update(comments)
            self.dic.update(dict(obj))

        if isinstance(obj, dict):
            if any([isinstance(obj[key], (tuple, list)) for key in obj]):
                for key in obj:
                    if isinstance(obj[key], (tuple, list)):
                        self.comments[key] = obj[key][1]
                        self.dic[key] = obj[key][0]
                    else:
                        self.dic[key] = obj[key]
            else:
                self.dic.update(obj)

    def as_header(self):
        hdr = Header(self.dic)
        for key in self.comments:
            hdr.comments[key] = self.comments[key]

        return hdr

    def __setitem__(self, key, value):
        if isinstance(value, (tuple, list)):
            value, comment = value
            self.comments[key] = comment

        self.dic[key] = value

    def __getitem__(self, item):
        return self.dic[item]

    def __len__(self):
        return len(self.dic)

    def __iter__(self):
        return self.dic.__iter__()

    def __contains__(self, item):
        return self.dic.__contains__(item)

    def __repr__(self):
        msgs = ""
        for key in self.dic:
            cmt_msg = ""
            if key in self.comments:
                cmt_msg = " / {}".format(self.comments[key])

            msg = "{} = {}".format(key.upper().ljust(9),
                                   str(self.dic[key]).rjust(16))
            msgs += msg + cmt_msg + "\n"

        return msgs

    def items(self):
        items_dict = []
        for key in self.dic:
            if key in self.comments:
                items_dict += [(key, (self.dic[key], self.comments[key]))]
            else:
                items_dict += [(key, self.dic[key])]
        return items_dict

    def keys(self):
        return self.dic.__iter__()

    def values(self):
        """Like :meth:`dict.values`."""

        for _, v in self.items():
            yield v
