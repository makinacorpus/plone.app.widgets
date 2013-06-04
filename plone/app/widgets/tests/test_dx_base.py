# -*- coding: utf-8 -*-

try:
    import unittest2 as unittest
except ImportError:  # pragma: nocover
    import unittest  # pragma: nocover
    assert unittest  # pragma: nocover

from datetime import date
from datetime import datetime
from zope.schema import Date
from zope.schema import Datetime
from zope.schema import List
from zope.schema import TextLine
from zope.schema import Tuple
from plone.app.widgets.testing import TestRequest


class BaseWidgetTests(unittest.TestCase):

    def test_base(self):
        from plone.app.widgets.dx.base import BaseWidget
        request = TestRequest(environ={'HTTP_ACCEPT_LANGUAGE': 'en'})
        widget = BaseWidget(request)
        widget.name = 'example'
        self.assertEqual(
            widget._widget_args(),
            {
                'name': 'example',
                'pattern': None,
                'pattern_options': {},
            },
        )

    def test_input(self):
        from plone.app.widgets.dx.base import InputWidget
        request = TestRequest(environ={'HTTP_ACCEPT_LANGUAGE': 'en'},
                              example='example-value')
        widget = InputWidget(request)
        widget.name = 'example'
        self.assertEqual(
            widget._widget_args(),
            {
                'name': 'example',
                'pattern': None,
                'pattern_options': {},
                'value': 'example-value',
            },
        )

    def test_select(self):
        from plone.app.widgets.dx.base import SelectWidget
        request = TestRequest(environ={'HTTP_ACCEPT_LANGUAGE': 'en'},
                              example='example-value')
        widget = SelectWidget(request)
        widget.name = 'example'
        widget.options = ['option1', 'option2', 'option3']
        self.assertEqual(
            widget._widget_args(),
            {
                'name': 'example',
                'pattern': None,
                'pattern_options': {},
                'options': ['option1', 'option2', 'option3'],
                'pattern': 'select2x',

            },
        )


class DateWidgetTests(unittest.TestCase):

    def setUp(self):
        from plone.app.widgets.dx.base import DateWidget

        self.request = TestRequest(environ={'HTTP_ACCEPT_LANGUAGE': 'en'})
        self.field = Date(__name__='datefield')
        self.widget = DateWidget(self.request)

    def test_widget(self):
        self.assertEqual(
            self.widget._widget_args(),
            {
                'name': None,
                'pattern': None,
                'pattern_options': {},
                'request': self.request
            }
        )

    def test_data_converter(self):
        from plone.app.widgets.dx.base import DateWidgetConverter
        converter = DateWidgetConverter(self.field, self.widget)

        self.assertEqual(
            converter.toFieldValue(''),
            converter.field.missing_value,
        )

        self.assertEqual(
            converter.toFieldValue('2000-10-30'),
            date(2000, 10, 30),
        )

        self.assertEqual(
            converter.toFieldValue('21-10-30'),
            date(21, 10, 30),
        )

        self.assertEqual(
            converter.toWidgetValue(converter.field.missing_value),
            '',
        )

        self.assertEqual(
            converter.toWidgetValue(date(2000, 10, 30)),
            '2000-10-30',
        )

        self.assertEqual(
            converter.toWidgetValue(date(21, 10, 30)),
            '21-10-30',
        )


class DatetimeWidgetTests(unittest.TestCase):

    def setUp(self):
        from plone.app.widgets.dx.base import DatetimeWidget

        self.request = TestRequest(environ={'HTTP_ACCEPT_LANGUAGE': 'en'})
        self.field = Datetime(__name__='datetimefield')
        self.widget = DatetimeWidget(self.request)

    def test_widget(self):
        self.assertEqual(
            self.widget._widget_args(),
            {
                'name': None,
                'pattern': None,
                'pattern_options': {},
                'request': self.request
            }
        )

    def test_data_converter(self):
        from plone.app.widgets.dx.base import DatetimeWidgetConverter
        converter = DatetimeWidgetConverter(self.field, self.widget)

        self.assertEqual(
            converter.toFieldValue(''),
            converter.field.missing_value,
        )

        self.assertEqual(
            converter.toFieldValue('2000-10-30 15:40'),
            datetime(2000, 10, 30, 15, 40),
        )

        self.assertEqual(
            converter.toFieldValue('21-10-30 15:40'),
            datetime(21, 10, 30, 15, 40),
        )

        self.assertEqual(
            converter.toWidgetValue(converter.field.missing_value),
            '',
        )

        self.assertEqual(
            converter.toWidgetValue(datetime(2000, 10, 30, 15, 40)),
            '2000-10-30 15:40',
        )

        self.assertEqual(
            converter.toWidgetValue(datetime(21, 10, 30, 15, 40)),
            '21-10-30 15:40',
        )


class Select2WidgetTests(unittest.TestCase):

    def setUp(self):
        self.request = TestRequest(environ={'HTTP_ACCEPT_LANGUAGE': 'en'})

    def test_widget(self):
        from plone.app.widgets.dx.base import Select2Widget
        widget = Select2Widget(self.request)
        self.assertEqual(
            widget._widget_args(),
            {
                'name': None,
                'value': None,
                'pattern': None,
                'pattern_options': {},
            }
        )

        widget.ajax_vocabulary = 'example'
        self.assertEqual(
            widget._widget_args(),
            {
                'name': None,
                'value': None,
                'pattern': None,
                'pattern_options': {},
                'ajax_vocabulary': '/@@widgets/getVocabulary?name=example',
            }
        )

    def test_data_converter(self):
        from plone.app.widgets.dx.base import Select2Widget
        from plone.app.widgets.dx.base import Select2WidgetConverter

        field1 = List(__name__='listfield', value_type=TextLine())
        widget1 = Select2Widget(self.request)
        widget1.field = field1
        converter1 = Select2WidgetConverter(field1, widget1)

        self.assertEqual(
            converter1.toFieldValue(''),
            field1.missing_value,
        )

        self.assertEqual(
            converter1.toFieldValue('123;456;789'),
            ['123', '456', '789'],
        )

        self.assertEqual(
            converter1.toWidgetValue([]),
            '',
        )

        self.assertEqual(
            converter1.toWidgetValue(['123', '456', '789']),
            '123;456;789',
        )

        field2 = Tuple(__name__='tuplefield', value_type=TextLine())
        widget2 = Select2Widget(self.request)
        widget2.field = field2
        converter2 = Select2WidgetConverter(field2, widget2)

        self.assertEqual(
            converter2.toFieldValue(''),
            field2.missing_value,
        )

        self.assertEqual(
            converter2.toFieldValue('123;456;789'),
            ('123', '456', '789'),
        )

        self.assertEqual(
            converter2.toWidgetValue(tuple()),
            '',
        )

        self.assertEqual(
            converter2.toWidgetValue(('123', '456', '789')),
            '123;456;789',
        )
