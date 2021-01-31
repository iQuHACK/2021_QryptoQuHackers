from qutip import *
import numpy as np
import matplotlib.pyplot as plt


from qiskit import Aer, execute

from qiskit_ionq_provider import IonQProvider 

#Call provider and set token value
provider = IonQProvider(token='BFmvdArkiCbsS12r4LZf5VgYDo4HngsS')

provider.backends()

from qiskit import QuantumCircuit
from random import randint

from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library.standard_gates import RYGate

def dec_to_bin(x,d):
    output = str(int(bin(x)[2:]))
    if len(output) < d-1:
        zeros = ("0" * (d-1-len(output)))
        return zeros + output
    elif len(output) > d-1:
        print("input number needed to be cut to fit parameters")
        return output[len(output)-d-1:len(output)]
    else:
        return output

def crypto_hash_init(input_num, K):


    d = len(K)
    bitstring = dec_to_bin(input_num,d)
    n = len(bitstring)
    big_N = 2**n



    qr = QuantumRegister(d)
    qc_hash = QuantumCircuit(qr)

    return (qc_hash, qr, d, bitstring, n, big_N)

def crypto_hash_add_H(qc_hash, qr, d, bitstring, n, big_N):
    for i in range(d-1):
        qc_hash.h(i)
    
    return qc_hash

def crypto_hash_final(qc_hash, qr, d, bitstring, n, big_N, K):
    for n_index in range(1,n+1):
        control_states = "0" * (d-1)
        if int(bitstring[n_index-1]) == 1:
            for perm in range(0,2**(d-1)):
                control_states = dec_to_bin(perm,d)
                i = sum(int(c) for c in control_states.strip())
                Y_Rotate_Gate = RYGate(np.pi*K[i-1]*2**n_index/big_N).control(d-1, ctrl_state=control_states)
                qc_hash.compose(Y_Rotate_Gate, qr, inplace=True)

    return qc_hash

def crypto_hash(input_num, K):
    (qc_hash, qr, d, bitstring, n, big_N) = crypto_hash_init(input_num, K)
    qc = crypto_hash_add_H(qc_hash, qr, d, bitstring, n, big_N)
    qc_hash = crypto_hash_final(qc, qr, d, bitstring, n, big_N, K)

    backend = Aer.get_backend('statevector_simulator')
    state = execute(qc,backend).result().get_statevector()
    return(state)
