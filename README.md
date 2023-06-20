# HamSAT
Error detection and correction using Symmetric Hamming Code.
Encoding part: A bit stream of 100000 length is read from _input.txt_ and is encoded in groups of 4 bits in a (7,4) fashion. The resultant code is stored in _encoded.txt_.
Decoding part: First the encoded data is read from _encoded.txt_. Then we use the decoder matrix to identify the error bit locations(_error_indices_) and invert the bit at those erroneous locations. Finally, redundant bits are removed to get the reconciled message. Knowledge of the number of bit errors plus the length of the input gives the bit error rate. 
