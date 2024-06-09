#!/usr/bin/env python3

import unittest

try:
    from .abstract import AbstractTest
except ImportError:
    from abstract import AbstractTest

class TurnstileTest(AbstractTest):
    

    def test_all_params(self):
        
        
        params = {
                'sitekey' : '0x4AAAAAAAC3DHQFLr1GavRN',
                'url'     : 'https://www.site.com/page/',
                'userAgent'  : 'foo',
                }
        
        sends = {
                'method'  : 'jandex',
                'sitekey' : '0x4AAAAAAAC3DHQFLr1GavRN',
                'userAgent'  : 'foo',
                'pageurl' : 'https://www.site.com/page/',
                }

        return self.send_return(sends, self.solver.jandex, **params)


if __name__ == '__main__':

    unittest.main()
