from qiskit import *
from qiskit_ionq_provider import IonQProvider 
from qiskit.providers.jobstatus import JobStatus
#Call provider and set token value







def swaptest(size):
    q = QuantumRegister(2*size+1)
    c = ClassicalRegister(1)    
    swaptest = QuantumCircuit(q,c)
    swaptest.h(0)
    #swaptest.append(hashfunc, [2])
    for i in range(1, size+1):
        swaptest.cx(i+size,i)
        swaptest.toffoli(0,i,i+size)
        swaptest.cx(i+size,i)
    swaptest.h(0)
    swaptest.measure(range(1), range(1))
    return swaptest

swap3=swaptest(3)
print(swap3.draw())
backend = provider.get_backend("ionq_simulator")
#backend_sim = Aer.get_backend('qasm_simulator')
#job_sim = execute(circ, backend_sim, shots=1024)
job_sim = backend.run(swap3, shots=1024)
result_sim = job_sim.result()

counts = result_sim.get_counts()
print(counts)