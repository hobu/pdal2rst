# coding: utf-8

import sys
try:
    import pypandoc
except ImportError:
    WITH_PANDOC = False
else:
    WITH_PANDOC = True

from pdal2rst.pdal.object import BasePDALObject
from json import dumps

HEADERS = {1: '=', 2: '~', 3: '-', 4: '+', 5: '^'}


class InfoObject(BasePDALObject):


    def get_regular_properties(self, _type, *args, **kwargs):
        """Make table with properties by schema_id
        :param str _type:
        :rtype: str
        """
        head = """.. csv-table::
    :delim: |
    :header: "Name", "Required", "Type", "Format", "Properties", "Description"
    :widths: 20, 10, 15, 15, 30, 25

"""
        body = []
        if schema.properties:
            for p in schema.properties:
                body.append('        {} | {} | {} | {} | {} | {}'.format(
                    p.get('name') or '',
                    'Yes' if p.get('required') else 'No',
                    self.get_type_description(p['type'], *args, **kwargs),
                    p.get('type_format') or '',
                    '{}'.format(p.get('type_properties') or ''),
                    p.get('description') or '')
                )
            body.sort()
        return (head + '\n'.join(body))


def header(value, header_value):
    return u'{}\n{}'.format(value, HEADERS[header_value] * len(value))


def md2rst(obj):
    if WITH_PANDOC:
        return pypandoc.convert(obj, to='rst', format='markdown')
    else:
        return obj.replace('```', '\n')


def json_dumps(obj, **kwargs):
    return dumps(obj, sort_keys=True, indent=kwargs.get('indent'))
