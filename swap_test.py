from qiskit import *
from qiskit_ionq_provider import IonQProvider 
from qiskit.providers.jobstatus import JobStatus
#Call provider and set token value
provider = IonQProvider(token='BFmvdArkiCbsS12r4LZf5VgYDo4HngsS')




q = QuantumRegister(3)
c = ClassicalRegister(1)


swaptest = QuantumCircuit(q,c)

swaptest.h(0)
#swaptest.append(hashfunc, [2])
swaptest.cx(2,1)
swaptest.toffoli(0,1,2)
swaptest.cx(2,1)
swaptest.h(0)

swaptest.measure(range(1), range(1))

print(swaptest.draw())
backend = provider.get_backend("ionq_qpu")
#backend_sim = Aer.get_backend('qasm_simulator')
#job_sim = execute(circ, backend_sim, shots=1024)
job_sim = backend.run(swaptest, shots=1024)
result_sim = job_sim.result()

counts = result_sim.get_counts()
print(counts)