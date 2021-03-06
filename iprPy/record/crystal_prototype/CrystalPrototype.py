# Standard Python libraries
from __future__ import (absolute_import, print_function,
                        division, unicode_literals)
import os

# iprPy imports
from .. import Record

class CrystalPrototype(Record):
    
    @property
    def contentroot(self):
        """str: The root element of the content"""
        return 'crystal-prototype'
    
    @property
    def schema(self):
        """
        str: The absolute directory path to the .xsd file associated with the
             record style.
        """
        return os.path.join(self.directory, 'record-crystal-prototype.xsd')
    
    def todict(self, full=True, flat=False):
        """
        Converts the structured content to a simpler dictionary.
        
        Parameters
        ----------
        full : bool, optional
            Flag used by the calculation records.  A True value will include
            terms for both the calculation's input and results, while a value
            of False will only include input terms (Default is True).
        flat : bool, optional
            Flag affecting the format of the dictionary terms.  If True, the
            dictionary terms are limited to having only str, int, and float
            values, which is useful for comparisons.  If False, the term
            values can be of any data type, which is convenient for analysis.
            (Default is False).
            
        Returns
        -------
        dict
            A dictionary representation of the record's content.
        """
        
        proto = self.content[self.contentroot]
        params = {}
        params['key'] = proto['key']
        params['id'] = proto['id']
        params['name'] = proto['name']
        params['prototype'] = proto['prototype']
        params['Pearson_symbol'] = proto['Pearson-symbol']
        params['Strukturbericht'] = proto['Strukturbericht']
        
        params['sg_number'] = proto['space-group']['number']
        params['sg_HG'] = proto['space-group']['Hermann-Maguin']
        params['sg_Schoen'] = proto['space-group']['Schoenflies']
        
        cell = proto['atomic-system']['cell']
        params['crystal_family'] = list(cell.keys())[0]
        params['a'] = cell.find('a')['value']
        try:
            params['b'] = cell.find('b')['value']
        except:
            params['b'] = params['a']
        try:
            params['c'] = cell.find('c')['value']
        except:
            params['c'] = params['a']
        params['natypes'] = max(proto['atomic-system'].finds('component'))
        
        return params