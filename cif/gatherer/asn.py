
from cif.utils import resolve_ns
import logging


class Asn(object):

    def __init__(self, *args, **kv):
        self.logger = logging.getLogger(__name__)

    def process(self, indicator):
        if indicator.itype == 'ipv4':
            i = '.'.join(reversed(indicator.indicator.split('.')))
            answers = resolve_ns('{}.{}'.format(i, 'origin.asn.cymru.com'))
            if len(answers) > 0:
                # Separate fields and order by netmask length
                # 23028 | 216.90.108.0/24 | US | arin | 1998-09-25
                # 701 1239 3549 3561 7132 | 216.90.108.0/24 | US | arin | 1998-09-25

                # i.asn_desc ????
                i.asn, i.prefix, i.cc, i.rir, _ = answers.split(' | ')

                # send back to router



Plugin = Asn