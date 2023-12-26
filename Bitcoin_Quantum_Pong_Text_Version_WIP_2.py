from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer
import random, string
from random import randrange
import time

#TYPE PLAY TO START
print('START GAME')
print()
print('L.E.V.E.L O.N.E')

print('In this part of the game you will guess the random key \n used to encode the Bitcoin key being sent')
print()
print("TYPE 'PLAY' to get started")

player_one_tries = 0
player_two_tries = 0

player_one_score = 0
player_two_score = 0

player_one_guesses = []
player_two_guesses = []

start = input()
if start == 'PLAY':
    key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(64))
    print(key)
    print()
    print('Key is a ',type(key))
    print()
    # create random key 
    key=[] 
    for i in range(8):
        a=randrange(2)
        key.append(a)
    print('Let me tell you a secret random key :',key)
    #Guess the random key
    print('Time to guess the random key...')
    time.sleep(1)
          
    while player_one_tries < 8:
        print("PLAYER 1's TURN")
        print('Try Number ' + str(player_one_tries))
        print()
        print('...')
          
        #Guess the random key
        #time.sleep(1)
        if player_one_tries == 0:
            x = int(input('Type the first digit of the random key you have guessed: '))
            player_one_guesses.append(x)
        elif player_one_tries == 7:
            x = int(input('Type the last digit of the random key : '))
            player_one_guesses.append(x)
        else:
            x = int(input('Type the next digit of the random key : '))
            player_one_guesses.append(x)
        if player_one_guesses[player_one_tries] == key[player_one_tries]:
            player_one_score += 1
        player_one_tries += 1
          
        print()
        print('##########################################')
        print()
              
        if player_two_tries < 8:
            print("PLAYER 2's TURN")
            print('Try Number ' + str(player_two_tries))
            print()
            print('...')
          
            #time.sleep(1)
            if player_two_tries == 0:
                x = int(input('Type the first digit of the random key you have guessed: '))
                player_two_guesses.append(x)
            elif player_two_tries == 7:
                x = int(input('Type the last digit of the random key : '))
                player_two_guesses.append(x)
            else:
                x = int(input('Type the next digit of the random key : '))
                player_two_guesses.append(x)
            if player_two_guesses[player_two_tries] == key[player_two_tries]:
                player_two_score += 1
            player_two_tries += 1

    print()              
    print('Player one has tried ' + str(player_one_tries) +' times')
    print('Player two has tried ' + str(player_two_tries) +' times')
    print('Wait...')
    time.sleep(1)
    print('Checking if scores == 8...')
    time.sleep(2)
          
    if player_one_score == 8:
        print('Player 1 seems to have won. Let us try to check if he guessed the correct \n random key in the next level of the game')
        time.sleep(1)
        print()
        print('L.E.V.E.L T.W.O CHECKER')
        print()
        for i in range(len(key)):
            m1 = ord(str(key[i]))
            m2 = bin(m1)[2:]
            if len(m2)== 6:
                m2 = m2+'00'
            if len(m2)== 7:
                m2 = m2+'0'
            message = list(m2)
            
            #print('Player 1 won, let us check his guessed random key')
            #time.sleep(1)
            print()
            #print('We shall now test if you guessed the right random key')
            print()
            #time.sleep(1)
            print('...')
            #time.sleep(1)
            print('...')
            #time.sleep(1)
            print('...')

            # Encryption

            qregA = QuantumRegister(8, 'q') # quantum register with 8 qubits
            cregA = ClassicalRegister(8, 'c') # classical register with 8 bits
            mycircuitA = QuantumCircuit(qregA,cregA) # quantum circuit with quantum and classical registers

            for m in range(len(message)):
                if message[m]==1:
                    mycircuitA.x(qregA[m])

            mycircuitA.barrier()

            # use random key 
            for g in range(len(key)):
                if key[g] == 1:
                    mycircuitA.x(qregA[g])
        
            mycircuitA.barrier()
            mycircuitA.measure(qregA,cregA)
            #mycircuitA.draw(output='mpl')

            # execute the circuit
            job = execute(mycircuitA,Aer.get_backend('qasm_simulator'))
            encryption = job.result().get_counts(mycircuitA)

            # display the measurement results with total count
            print("Encryption", encryption)
            # this converts the measurement result string into a list
            encrypted_message=list(map(int,[*list(encryption.keys())[0]]))

            # we reverse the list since the Qiskit considers our MSB as LSB
            encrypted_message.reverse()
            print()
            print("Message:", message)
            print("Key:", key)
            print()
            print("Encrypted Message:", encrypted_message)
            print()

            # Decryption

            qregB = QuantumRegister(8, 'q') # quantum register with 8 qubits
            cregB = ClassicalRegister(8, 'c') # classical register with 8 bits
            mycircuitB = QuantumCircuit(qregB,cregB) # quantum circuit with quantum and classical registers

            # apply x-gate to change initial states from 0 to 1, preparing the state with encrypted message
            for m in range(len(encrypted_message)):
                if encrypted_message[m]==1:
                    mycircuitB.x(qregB[m])

            mycircuitB.barrier()

            # use the same random key and apply x gates to decrypt message.
            # Hence random key should have been shared between Alice and Bob classically with RSA or via 
            # a quantum network using BB84

            for n in range(len(player_one_guesses)):
                if player_one_guesses[n]==1:
                    mycircuitB.x(qregB[n])        
    
            mycircuitB.barrier()

            mycircuitB.measure(qregB,cregB)

            #mycircuitB.draw(output='mpl')

            # execute the circuit
            job = execute(mycircuitB,Aer.get_backend('qasm_simulator'))
            decryption = job.result().get_counts(mycircuitB)

            # display the measurement results with total count
            print("Decryption", decryption)
            # this converts the measurement result string into a list
            decrypted_message=list(map(int,[*list(decryption.keys())[0]]))

            # we reverse the list since Qiskit considers our MSB as LSB
            decrypted_message.reverse()
            print()
            print("Message:", message)
            print("Decrypted Message:", decrypted_message)
            print()  
  
            if message == decrypted_message:  
                print("Random key is correct!")  
                if i == 64:
                    print("Random key is correct! Player ! WINS!!!")
            else:  
                print("Random key is incorrect! Player 1 LOSES")
        
    if player_two_score == 8:
        print('Player 2 seems to have won. Let us try to check if he guessed the correct \n random key in the next level of the game')
        time.sleep(1)
        print('L.E.V.E.L T.W.O CHECKER')
        print()
        for i in range(len(key)):
            m1 = ord(str(key[i]))
            m2 = bin(m1)[2:]
            message = list(m2)
            
            #print('Player 1 won, let us check his guessed random key')
            #time.sleep(1)
            print()
            #print('We shall now test if you guessed the right random key')
            print()
            #time.sleep(1)
            print('...')
            #time.sleep(1)
            print('...')
            #time.sleep(1)
            print('...')

            # Encryption

            qregA = QuantumRegister(8, 'q') # quantum register with 8 qubits
            cregA = ClassicalRegister(8, 'c') # classical register with 8 bits
            mycircuitA = QuantumCircuit(qregA,cregA) # quantum circuit with quantum and classical registers

            for m in range(len(message)):
                if message[m]==1:
                    mycircuitA.x(qregA[m])

            mycircuitA.barrier()

            # use random key 
            for k in range(len(key)):
                if key[k] == 1:
                    mycircuitA.x(qregA[k])
        
            mycircuitA.barrier()
            mycircuitA.measure(qregA,cregA)
            #mycircuitA.draw(output='mpl')

            # execute the circuit
            job = execute(mycircuitA,Aer.get_backend('qasm_simulator'))
            encryption = job.result().get_counts(mycircuitA)

            # display the measurement results with total count
            print("Encryption", encryption)
            # this converts the measurement result string into a list
            encrypted_message=list(map(int,[*list(encryption.keys())[0]]))

            # we reverse the list since the Qiskit considers our MSB as LSB
            encrypted_message.reverse()
            print()
            print("Message:", message)
            print("Key:", key)
            print()
            print("Encrypted Message:", encrypted_message)
            print()

            # Decryption

            qregB = QuantumRegister(8, 'q') # quantum register with 8 qubits
            cregB = ClassicalRegister(8, 'c') # classical register with 8 bits
            mycircuitB = QuantumCircuit(qregB,cregB) # quantum circuit with quantum and classical registers

            # apply x-gate to change initial states from 0 to 1, preparing the state with encrypted message
            for m in range(len(encrypted_message)):
                if encrypted_message[m]==1:
                    mycircuitB.x(qregB[m])

            mycircuitB.barrier()

            # use the same random key and apply x gates to decrypt message.
            # Hence random key should have been shared between Alice and Bob classically with RSA or via 
            # a quantum network using BB84

            for n in range(len(player_two_guesses)):
                if player_two_guesses[n]==1:
                    mycircuitB.x(qregB[n])        
    
            mycircuitB.barrier()

            mycircuitB.measure(qregB,cregB)

            #mycircuitB.draw(output='mpl')

            # execute the circuit
            job = execute(mycircuitB,Aer.get_backend('qasm_simulator'))
            decryption = job.result().get_counts(mycircuitB)

            # display the measurement results with total count
            print("Decryption", decryption)
            # this converts the measurement result string into a list
            decrypted_message=list(map(int,[*list(decryption.keys())[0]]))

            # we reverse the list since Qiskit considers our MSB as LSB
            decrypted_message.reverse()
            print()
            print("Message:", message)
            print("Decrypted Message:", decrypted_message)
            print()  
  
            if message == decrypted_message:  
                print("Random key is correct!")  
                if i == 64:
                    print('Random key is correct! Player 2 WINS')
            else:   
                print("Random key is incorrect! Player 2 LOSES")
    
    else:
        print('Neither Player seems to have WON. Sorry :/')
        print('Re-run this script to play again')

else:
    print()
    print('If you do not type PLAY you will not start the game')
