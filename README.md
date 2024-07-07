# JsonBytesEncoderDecoder

Json is a format usually used to write in q file or transfert in messagzs python variables, because it support most of python types, but not all.

If we try to put bytes in a json file, we get the error : ’TypeError: Object of type bytes is not JSON serializable'

Nevertheless, it is possible to put bytes in a json as a string, and read it back to bytes type.

The code of this repository allow such operation.
