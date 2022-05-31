import re
import Parent_Class
import py_starter as ps


class PhoneNumber( Parent_Class.Parent_Class ):

    DEFAULT_ATT_VALUES = {
    'country_code': '1',
    'area_code': None,
    'phone_number': None,
    'digits': None,
    'formatted': None,
    }

    def __init__( self, long_phone_number = '', **kwargs ):

        Parent_Class.Parent_Class.__init__( self )

        kwargs = ps.replace_default_kwargs( PhoneNumber.DEFAULT_ATT_VALUES, **kwargs )
        self.set_atts( kwargs )

        self.valid = False
        self.check_validity( long_phone_number )

    def print_one_line_atts( self, **kwargs ):

        return self._print_one_line_atts_helper( atts = [ 'type','formatted' ], **kwargs )

    def print_imp_atts( self, **kwargs ):

        return self._print_imp_atts_helper( atts = ['country_code','area_code','phone_number','digits','formatted','valid'], **kwargs )

    def __eq__( self, PhoneNumber_inst ):

        return self.digits == PhoneNumber_inst.digits

    def check_validity( self, long_phone_number ):

        digits_only = filter_digits_from_str( long_phone_number )

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


def filter_digits_from_str( number_str ):

    '''given a str, take only characters which are numbers, returns a string type'''

    return re.sub( '[^0-9]', '', str(number_str) )


def do_PhoneNumbers_match( *PhoneNumbers ):

    if len(PhoneNumbers) >= 2:

        PhoneNumber1 = PhoneNumbers[0]
        for i in range( 1, len(PhoneNumbers)):
            PhoneNumber2 = PhoneNumbers[i]

            if PhoneNumber1 != PhoneNumber2:
                return False

    return True
