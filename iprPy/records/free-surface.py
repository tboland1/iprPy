import os

import numpy as np

from DataModelDict import DataModelDict as DM

def schema():
    dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(dir, 'record-free-surface.xsd')

def todict(record, full=True):

    model = DM(record)

    proto = model['free-surface']
    params = {}
    params['key'] =       proto['key']
    params['id'] =        proto['id']
    params['prototype'] = proto['system-family']
    
    asp = proto['atomman-surface-parameters']
    params['x_axis'] =       np.array(asp['crystallographic-axes']['x-axis'])
    params['y_axis'] =       np.array(asp['crystallographic-axes']['y-axis'])
    params['z_axis'] =       np.array(asp['crystallographic-axes']['z-axis'])
    params['cutboxvector'] = asp['cutboxvector']
    params['atomshift'] =    np.array(asp['atomshift'])
    
    return params 