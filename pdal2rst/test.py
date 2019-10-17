import codecs
import functools
import os, re
import inspect
import importlib
from io import StringIO as File_obj
from jinja2 import Environment, PackageLoader
from unittest import TestCase, SkipTest, main

from pdal2rst.pdal.base_pdal_object import BasePDALObject
import json

SAMPLES_PATH = os.path.join(os.path.dirname(__file__), os.pardir, 'samples')


class BaseSwaggerTestCase(object):

    example_filename = None
    examples = None

    @classmethod
    def setUpClass(cls):

        pdal_file = os.path.join(SAMPLES_PATH, cls.pdal_filename)
        with codecs.open(pdal_file, 'r', encoding='utf-8') as _file:
            doc = json.load(_file)

        if doc is None:
            raise SkipTest('File is empty')

        if cls.example_filename:
            example_file = os.path.join(SAMPLES_PATH, cls.example_filename)
            with codecs.open(example_file, 'r', encoding='utf-8') as _file:
                cls.examples = json.load(_file)

            if not cls.examples:
                raise SkipTest('Example file is empty')

        cls.pdal_doc = BasePDALObject(doc)



if __name__ == '__main__':
    main()
