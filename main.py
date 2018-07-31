# -*- coding: utf-8 -*-
"""
    Subscriber Matching Service 
    ~~~~~
    Abstract interface for matching subscribers from arbitary payment 
    information providers, payment institutions, billing systems. 
    :copyright: © 2018 Karma Computing.
    :license: GPLv3, see LICENSE for more details.
"""

Partner = namedtuple('Partner', ['uid', 
                                 'created_at',
                                 'matched_source_gateways',
                                 'links_partner_uids',
                                 'language',
                                 'billing_email',
                                 'given_name',
                                 'family_name',
                                 'company_name',
                                 'billing_street_number',
                                 'billing_street',
                                 'billing_city',
                                 'billing_postal_code',
                                 'billing_state',
                                 'billing_state_code',
                                 'billing_country',
                                 'billing_country_code',
                                 'billing_latitude',
                                 'billing_longitude'
                                 'shipping_street_number',
                                 'shipping_street',
                                 'shipping_city',
                                 'shipping_country',
                                 'shipping_country_code',
                                 'shipping_latitude',
                                 'shipping_longitude',
                                 'shipping_postal_code',
                                 'shipping_state',
                                 'shipping_statecode',
                                 'active_mandates',
                                 'delinquent'
                                 ])
Partner.__new__.__defaults__ = (None,) * len(Partner._fields)

'''
 How to decide if a partner is already matched in matched_source_gateways.
 We use the word 'partner' instead of 'customer' to normalise these types of
 records, inspired by Odoo's data model, whereas Salesforce uses the word
 'account' for the same purpose.

 1) Take a customer object from a TransactionGatewayAbstract
 2) Extract the unique id which the TransactionGateway provides for the partner 
 3) Generate a look-up id (aka TransactionGatewayPartnerId) by concatenating the 
    TransactionGatewayAbstract.get_short_name with the unique partner id
    provided by the TransactionGateway being inspected. (We loosely take
    inspiration from MAC Organisationally Unique Identifier (OUI) concept to
    ensure uniqueness.
 4) Query the Partner object for the computed TransactionGatewayPartnerId
 5) If the TransactionGatewayPartnerId exists within a Partner's 
    matched_source_gateways attribute, then this record corresponds to that
    gateway. If not, then this is considered a new 'unseen' Partner records
    which MAY have data which can be used to update the Partner record.
'''


from SSOT import SSOT
from HSBCBusiness import HSBCBusiness
from GoCardless import GoCardless
from Gamma import Gamma

from webapp import app

if __name__ == "__main__":
    pass

