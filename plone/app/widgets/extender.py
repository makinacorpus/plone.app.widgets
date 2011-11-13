from plone.widgets.archetypes import ChosenWidget
from archetypes.schemaextender.interfaces import ISchemaModifier
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender
from zope.component import adapts
from zope.interface import implements
from Products.ATContentTypes.interface import IATContentType
from plone.app.widgets.interfaces import ILayer


class WidgetsModifier(object):
    """
    change any content...
    """
    implements(ISchemaModifier, IBrowserLayerAwareExtender)
    adapts(IATContentType)
    layer = ILayer

    def __init__(self, context):
        self.context = context

    def fiddle(self, schema):
        if 'subject' in schema:
            subject = schema['subject']
            subject_widget = subject.widget
            subject.widget = ChosenWidget(
                label=subject_widget.label,
                description=subject_widget.description,
                js_options={
                    'allow_add_new': True,
                    'no_results_text': 'No results. Press enter to add',
                    'allow_sortable': True
                })
            subject.vocabulary_factory = 'plone.app.vocabularies.Keywords'

        if 'contributors' in schema:
            contributors_field = schema['contributors']
            contributors_widget = contributors_field.widget
            contributors_field.widget = ChosenWidget(
                label=contributors_widget.label,
                description=contributors_widget.description,
                queryView='widget-user-query',
                js_options={
                    'allow_sortable': True
                }
            )
