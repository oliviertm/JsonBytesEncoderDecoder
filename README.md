# JsonBytesEncoderDecoder

Json is a format usually used to write in files or transfert in messages python variables, because it supports most of python types, but not all.

If we try to put bytes in a json file, we get the error : `TypeError: Object of type bytes is not JSON serializable`, because json encoder  didn't support bytes encoding natively.

Nevertheless, it is possible to put bytes in a json as strings, and read it back to bytes type, with a small limitation.

The code of this repository allows such operations.

Assume that we want to write b'\0\xff' in a json. The code provided here will replace the bytes `b'\0\xff'` which cannot be serialized in json by the structure `{ "r4DWEn1THVNbEoG1" : "AP8=" }`

This structure contains a key and a value. 

The key is an identifier which shall not appears anywhere else in the input data. As this data is unknown, a constant number of 29 decimal digit randomly choosen and coded in base64 is used (this identifier is an exemple, any other one as big and random can be used).

The value are the bytes coded in [base64](https://en.m.wikipedia.org/wiki/Base64).

Upon decoding, each time a structure with 2 elements will be read, and if the first element matches the specific identifier, the second will be decoded back to string for final output, and will replace this 2 element structure in returned data.
