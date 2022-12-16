import re
from parent_class import ParentClass
import py_starter as ps

class PhoneNumber( ParentClass ):

    DEFAULT_ATT_VALUES = {
    'country_code': '1',
    'area_code': None,
    'phone_number': None,
    'digits': None,
    'formatted': None,
    'medium': 'iMessage'
    }

    _IMP_ATTS = ['country_code','area_code','phone_number','digits','formatted','valid','medium']
    _ONE_LINE_ATTS = ['type','formatted']

    def __init__( self, long_phone_number = '', **kwargs ):

        ParentClass.__init__( self )

        kwargs = ps.replace_default_kwargs( PhoneNumber.DEFAULT_ATT_VALUES, **kwargs )
        self.set_atts( kwargs )

        self.valid = False
        self.check_validity( long_phone_number )

    def __eq__( self, PhoneNumber_inst ):

        return self.digits == PhoneNumber_inst.digits

    def check_validity( self, long_phone_number ):

        digits_only = self.filter_digits_from_str( long_phone_number )

        if len(digits_only) >= 10:
            self.valid = True

            self.phone_number = digits_only[ -7 :]
            self.area_code = digits_only[ -10:-7 ]

            if len(digits_only) > 10:
                self.country_code = digits_only[ : -10 ]

            self.digits = self.country_code + self.area_code + self.phone_number
            self.make_formatted()

    def make_formatted( self ):

        self.formatted = '+' + self.digits

    @staticmethod
    def filter_digits_from_str( number_str ):

        '''given a str, take only characters which are numbers, returns a string type'''

        return re.sub( '[^0-9]', '', str(number_str) )


