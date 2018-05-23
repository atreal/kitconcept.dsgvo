# -*- coding: utf-8 -*-
from plone.app.users.browser.register import RegistrationForm
from plone.app.users.userdataschema import IUserDataSchema
from plone.app.users.userdataschema import IUserDataSchemaProvider

from zope import schema
from zope.interface import implements

from kitconcept.dsgvo import _


class InvalidAccept(schema.ValidationError):

    __doc__ = _(
            u'label_dsgvo_accept_invalid',
            default=(u'Bitte akzeptieren sie die Datenschutzerklärung und'
                     u'Widerrufhinweise.'))


def validateAccept(value):
    if value is not True:
        raise InvalidAccept()
    return True
    

class IDsgvoP4UserDataSchema(IUserDataSchema):
    '''
    Combined fields
    '''

    dsgvo_accept = schema.Bool(
        title=_(u'label_dsgvo_accept',
                default=(
                    u'Ich habe die <a href="${portal_url}/datenschutz">'
                    u'Datenschutzerklärung und Widerrufhinweise</a> '
                    u'gelesen und akzeptiere diese.')),
        description=_(
            u'help_dsgvo_accept',
            default=u''),
        required=True,
        constraint=validateAccept,
    )


class EnhancedUserDataSchemaProvider(object):
    implements(IUserDataSchemaProvider)

    def getSchema(self):
        """
        """
        return IDsgvoP4UserDataSchema


class EnhancedRegistrationForm(RegistrationForm):

    def __init__(self, context, request):
        super(EnhancedRegistrationForm, self).__init__(context, request)

