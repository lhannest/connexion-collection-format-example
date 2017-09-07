import connexion
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from flask import jsonify

def example_get(multi=None, csv=None, pipes=None):
    """
    example_get
    An example of different collection formats for lists
    :param multi: A multi collection format list
    :type multi: List[str]
    :param csv: A csv collection format list
    :type csv: List[str]
    :param pipes: A pipes collection format list
    :type pipes: List[str]

    :rtype: str
    """
    return jsonify({'multi' : multi, 'csv' : csv, 'pipes' : pipes})
