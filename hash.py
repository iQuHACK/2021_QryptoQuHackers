#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from math import log

from qiskit import Aer, execute

from qiskit_ionq_provider import IonQProvider 

#Call provider and set token value
provider = IonQProvider(token='BFmvdArkiCbsS12r4LZf5VgYDo4HngsS')


from qiskit import *
from qiskit.circuit.library.standard_gates import RYGate
import numpy as np

def bitstring(num, n):
    bstring = '0'*n + bin(num)[2:]
    return bstring[-n:]

def crypto_hash(M, K, verbose=False):
    """
    M: length n bit-string message to encode
    K: list of d integers from 0 to N-1
    """
    n = len(M) # num bits in message
    d = len(K) # num keys
    N = 2**n
    
    
    num_qubits = int(log(d, 2)) + 1 #?????
    qr = QuantumRegister(num_qubits)
    qc = QuantumCircuit(qr)
    
    qc.h(range(num_qubits-1))

    for j in range(len(M)):
        if M[j] == '1':
            for i in range(d):
                ctrl_state = bitstring(i, num_qubits-1)

                theta = 4*np.pi * int(K[i],2) * 2**j / N
                
                Y_Rotate_Gate = RYGate(theta).control(num_qubits-1, ctrl_state=ctrl_state)
                qc.compose(Y_Rotate_Gate, qr, inplace=True)
    
    if verbose:
        print(qc.draw())
    
    backend = Aer.get_backend('statevector_simulator')
    state = execute(qc,backend).result().get_statevector()
    return(state)



