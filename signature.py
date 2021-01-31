#!/usr/bin/env python
# coding: utf-8

from qiskit import *
from qiskit_ionq_provider import IonQProvider 
from qiskit.providers.jobstatus import JobStatus
#Call provider and set token value
provider = IonQProvider(token='BFmvdArkiCbsS12r4LZf5VgYDo4HngsS')
from random import randrange
import numpy as np

from swap_test import swap_test
from hash import crypto_hash, bitstring


# given a message, produces a Quantum Digital Signature
class Signed_Transaction():
    def __init__(self, message):
        self.message = message
        self.bitstring = self.string_to_bitstring(message)
        self.signed_transaction = self.sign_transaction()
        
    def string_to_bitstring(self, m):
        bs = ""
        for i in bytes(m, encoding='utf-8'):
            bs += bin(i)[2:]
        return bs
    
        
    # make M pairs of private keys
    def generate_priv_keys(self):
        n = 4
        d = 3
        
        return {
            'k0': [bitstring(randrange(2**n - 1),n) for i in range(d)],
            'k1': [bitstring(randrange(2**n - 1),n) for i in range(d)]
        }
    
    # make M pairs of public keys (Quantum States)
    def generate_pub_keys(self, priv_keys):
        return {
            "f_k0":[crypto_hash(ki, priv_keys["k0"]).astype(np.float) for ki in priv_keys["k0"]], 
            "f_k1":[crypto_hash(kj, priv_keys["k1"]).astype(np.float) for kj in priv_keys["k1"]]
        }
    
    def sign_bit(self, b, priv_keys, pub_keys):
        
        return {
            "m_bit" : b,
            "priv_keys" : priv_keys['k0'] if b == '0' else priv_keys['k1'],
            "pub_keys" : pub_keys
        }
    
    def sign_transaction(self):
        signed_transaction = []
        
        for b in self.bitstring:
            priv_keys = self.generate_priv_keys()
            pub_keys = self.generate_pub_keys(priv_keys)
            
            signed_transaction.append(self.sign_bit(b, priv_keys, pub_keys))
            
        return signed_transaction
        
    def get_signature(self):
        return self.signed_transaction


class Validation():
    
    BIT_THRESHOLD = .3 #???
    MESSAGE_THRESHOLD = .1 #??????
    
    def __init__(self, transaction):
        self.signature = transaction
        #self.validations = self.validate_transaction()

    def key_tests(self, signed_bit):
        priv_keys = signed_bit["priv_keys"]
        
        # select list of public keys corresponding to bit value
        pub_keys = signed_bit["pub_keys"]['f_k0'] if signed_bit["m_bit"] == '0' else signed_bit["pub_keys"]['f_k1']
        
        # hash private keys
        hashed_keys = [crypto_hash(ki, priv_keys).astype(np.float) for ki in priv_keys]
        
        # perform swap test on public and hashed private keys
        tests = [swap_test(pki, pkj) for pki, pkj in zip(pub_keys, hashed_keys)]
        
        return tests
    
    def validate_bit(self, signed_bit):
        
        tests = self.key_tests(signed_bit)
        #print(tests)
        
        M = len(tests)
        threshold  = M * self.BIT_THRESHOLD
        
        r = sum(tests)
        if r < threshold:
            passed = True
        else:
            passed = False
            
            
        return int(passed)
    
#         return {
#             "passed": passed,
#             "r": r,
#             "threshold": threshold,
#             "tests": tests,
#         }
    
    def validate(self):
        validations = []
        
        for signed_bit in self.signature:
            validations.append(self.validate_bit(signed_bit))
                    
        failures = len(validations) - sum(validations)
        failure_rate = failures / len(validations)
        
        return {
            "pass": failure_rate < self.MESSAGE_THRESHOLD,
            "bits_failure": str(round(failure_rate * 100, 4)) + '%'
        }


class Forgery(Signed_Transaction):
    def __init__(self, message):
        self.message = message
        self.bitstring = self.string_to_bitstring(message)
        self.forged_transaction = self.forge_transaction()
        
    def forge_transaction(self):
        signed_transaction = []
        
        for b in self.bitstring:
            # generate a set of public keys and forget corresponding private
            pub_keys = self.generate_pub_keys(self.generate_priv_keys())
            # forge a new set of private keys
            priv_keys = self.generate_priv_keys()
            
            signed_transaction.append(self.sign_bit(b, priv_keys, pub_keys))
            
        return signed_transaction
        
    def get_signature(self):
        return self.forged_transaction




