import json
import numpy as np

class CustomEncoder(json.JSONEncoder):
    """
    Custom JSON encoder for any non-native classes used in the scripts.
    """
    def default(self, obj):
        # if isinstance(obj, (Box, Checkbox, Cell)):
        #     return obj._to_json()
        # For instance, we had classes Box, Checkbox, and Cell in our project.
        # In each of those classes, we had function _to_json() which converted
        # and returned the instance data to JSON format
        if isinstance(obj, np.integer):
            return int(obj)
        else:
            return json.JSONEncoder.default(self, obj)