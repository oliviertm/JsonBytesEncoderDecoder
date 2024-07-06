#!/usr/bin/python3
import base64
import json

"""
Generation of the UniqueKey:

import base64
import secrets
# binary number of 96 bits so a decimal number of 29 digits
r=b''.join([secrets.randbits(96).to_bytes(12,byteorder='big') ])
print(base64.b64encode(r).decode('ascii'))
"""

class BytesInJson(json.JSONEncoder):
    """
    Class of json encoder which allow bytes encoding in json as string, and decoding of this string back to bytes.
    To be used for "cls" argument of json.dumps()
    """
    
    # This string shall not appear in any dict we may have to process, hence its length and randomness
    UniqueKey = "r4DWEn1THVNbEoG1"
    # If this string appear as key in the dict we convert to json, the decoding of this json will lead to the decoding of its value as it was encoded bytes

    def default(self, o):
        """
        Method which will be used by json encoder for bytes type encoding
        """
        if isinstance(o, bytes):
            return {BytesInJson.UniqueKey : base64.b64encode(o).decode('ascii') }
        else:
            return super().default(o)

    def decode(jsonDict):
        """
        Object pairs hook for json decoding of bytes encoded into strings.
        To be used in object_pairs_hook argument of json.loads()
        """
        if len(jsonDict) == 1  and len(jsonDict[0]) == 2 and jsonDict[0][0] == BytesInJson.UniqueKey :
            return base64.b64decode(jsonDict[0][1].encode('ascii'))
        else:
            return dict(jsonDict)


if __name__ == "__main__":

    otherData = {"myint": 1, "astring" : "abced"}
    level2Imbrication = {"myint2": 2, "astring2" : "abcedefgh"}
    otherDataMoreThan2 = {"myfloat": 1.9999, "bstring" : "efghij", "mybool" : False, "level2": level2Imbrication}
    data = {"bytes": (65535).to_bytes(2, byteorder='big'),"string":"Hello world", "int":1, "float": 2.1, "boolean": True, "imbricated": otherData, "imbricated2": otherDataMoreThan2}

    print("Data = {}\n".format(data))
    
    dumped = json.dumps(data, cls=BytesInJson)

    print("Serialized data : {}\n".format(dumped))

    loaded = dict(json.loads(dumped, object_pairs_hook=BytesInJson.decode))
    
    print("Deserialized data = {}\n".format(loaded))
    print("Deserisalized data are the same as serialized input data={}".format(data==loaded))
