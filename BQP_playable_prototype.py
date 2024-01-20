from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer
import random, string
from random import randrange
import time

#import cv2

import qiskit
from qiskit import execute, Aer
from math import pi


#Opening Video Introduction


#def playVideo():
#    cap = cv2.VideoCapture(r"C:\Users\Student5\Desktop\BQPong\video.mp4")
#    cv2.CAP_PROP_BUFFERSIZE
#    ret, frame = cap.read()
#    while(1):
#        ret, frame = cap.read()
#        cv2.imshow('frame',frame)
#        if cv2.waitKey(1) & 0xFF == ord('q') or ret==False :
#            cap.release()
#            cv2.destroyAllWindows()
#            break
#    cv2.imshow('frame',frame)
    
#playVideo()


#INTRODUCTION

print('Sometime in the future, many countries are at war.\n People who want to send bitcoin keys to their families overseas can only do so in secret.\n The internet is long gone. Commandline style programs are the only thing left.')
print('...')
print()
time.sleep(7)

print('Sending the keys across quantum secure channels is done using Quantum One Time Pads\n but sending the random encryption key has to be done classically,\n which is unsafe.')
print('...')
print()
time.sleep(7)

print('The only alternative is to guess the random key \n in as few tries as possible, see the bitcoins and secure them\n before an eavesdropper notices anything.')
print('...')
print()
time.sleep(7)

print('To test guessing capibilities, a guessing-pong game is created.')
print('...')
print()
time.sleep(6)

print('Will you be the winner?')
print('...')
print()
time.sleep(5) 


#TYPE PLAY TO START
print(' ------       ----      -----   ')
print(' |     |     |    |     |    |  ')
print(' |____ /     |    |     |    |  ')
print(' |     \  *  |    |  *  |----   ')
print(' |     |     |    |     | |     ')
print(' |_____|     |____\     |_|     ')

print('BITCOIN   *  QUANTUM *  PONG')
print()
      
print('START GAME')
print()
print('L.E.V.E.L O.N.E')
print()

print('In this part of the game you will guess the random key \n used to encode the Bitcoin key being sent')
print()
print("TYPE 'PLAY' to get started")

player_one_tries = 0
player_two_tries = 0

player_one_score = 0
player_two_score = 0

player_one_guesses = []
      
player_two_guesses_quantum = [0,0,0,0,0,0,0,0]

start = input()
if start == 'PLAY':
    Bkey = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(64))
    print(Bkey)
    print()
    print('Bitcoin Key is a ',type(Bkey))
    print()
    # create random key 
    key=[] 
    for i in range(8):
        a=randrange(2)
        key.append(a)
    print('Let me tell you a secret random key : ____')
    #Guess the random key
    print('Time to guess the random key...')
    print()
    print('NOTE: Player 1 will use random guessing\n while Player 2 will use a quantum computer to\n do the guessing.')
    print('You got this ;-)')
    time.sleep(2)
    print('GOOD lUCK!')
    print()
    time.sleep(1)
          
    while player_one_tries < 8:
        print("PLAYER 1's TURN")
        print('Try Number ' + str(player_one_tries))
        print('Guessing circuitry ---> Classical guessing along a number line')
        print('---#---#---#---#---#---#---#---#---')
        print()
        print('...')
        print()
        print('Press 1 to choose randomly and 2 to use a quantum computer to do the choosing')
        print('A wrong choice will make you lose your turn')
        
        choice = input('Type your choice: ')
        if choice == '1':
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
            print('player_one_guesses is ',player_one_guesses)
            
            if player_one_guesses[player_one_tries] == key[player_one_tries]:
                print('You guessed correctly!')
                player_one_score += 1
                time.sleep(1)
            else:
                print('You guessed wrong')
                time.sleep(1)
            player_one_tries += 1
                            
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print('##########################################')
        print()
              
        if player_two_tries < 8:
            print("PLAYER 2's TURN")
            print('Try Number ' + str(player_two_tries))
            print('Guessing circuitry ---> Quantum circuit')
            print('q0-----------------')
            print('q1-----------------')
            print()
            print('...')
            print()
            print('Press 1 to choose randomly and 2 to use a quantum computer to do the choosing')
            print('A wrong choice will make you lose your turn')
            choice = input('Type your choice: ')

            if choice == '2':
                #Guess the random key
                circuit = qiskit.QuantumCircuit(3,3)
                
                print('You are given either an NOT/X gate or an Hadamard/H gate.\n Type 'X' or 'H' to pick the gate you will use,\n or you will miss your turn')
                #time.sleep(3)
        
                ans = input(' Answer: ')
                if ans == 'X':
                    target_one_in_gate = int(input('Given an X gate,\n which one of two qubits in a 3-qubit circuit will you put them on to \n capture a value and its neighbours equal to '1' ?\n Type one correct entry from the set {0, 1, 2}: '))
                    print('OK, now')
                    target_two_in_gate = int(input('Given an X gate,\n which second one of two qubits in a 3-qubit circuit will you put them on to \n capture a value and its neighbours equal to '1'?\n Type another correct entry from the set {0, 1, 2}: '))
                    circuit.x(target_one_in_gate)
                    circuit.x(target_two_in_gate)

                if ans == 'H':
                    target_one_in_gate = int(input('Given an H gate,\n which one of two qubits in a 3-qubit circuit will you put them on to \n capture a value and its neighbours equal to '1' ?\n Type one correct entry from the set {0, 1, 2}: '))
                    print('OK, now')
                    target_two_in_gate = int(input('Given an H gate,\n which second one of two qubits in a 3-qubit circuit will you put them on to \n capture a value and its neighbours equal to '1'?\n Type another correct entry from the set {0, 1, 2}: '))
                    circuit.h(target_one_in_gate)
                    circuit.h(target_two_in_gate)

                circuit.measure(range(3),range(3))

                job = execute(circuit, Aer.get_backend('qasm_simulator'),shots=1000)
                counts = job.result().get_counts()

                format_string = '0' + str(3) + 'b'

                for i in range(len(key)):
                    if key[i] == 1:
                        binary_value = format(i, format_string)
                        if binary_value in counts:
                            print('You guessed correctly!')
                            player_two_score += 1
                            player_two_guesses_quantum[i] = 1
                            time.sleep(1)
                        else:
                            print('You guessed wrong')
                            time.sleep(1)
                print('player_two_guesses_quantum is ',player_two_guesses_quantum)
                player_two_tries += 1
            print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()    

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
        for i in range(len(Bkey)):
            m1 = ord(str(Bkey[i]))
            m2 = bin(m1)[2:]
            if len(m2)== 6:
                m2 = m2+'00'
            if len(m2)== 7:
                m2 = m2+'0'
            m3 = list(m2)
            message = list(map(int, m3))
            
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

                  
            if len(player_one_guesses) == 8:
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
                if i == 63:
                    print("Random key is correct! Player ! WINS!!!")
            else:  
                print("Random key is incorrect! Player 1 LOSES")
    else:
        print('Player 1 loses :/')
        
    if player_two_guesses_quantum == key:
        print('Player 2 seems to have won. Let us try to check if he guessed the correct \n random key in the next level of the game')
        time.sleep(1)
        print('L.E.V.E.L T.W.O CHECKER')
        print()
        for i in range(len(Bkey)):
            m1 = ord(str(Bkey[i]))
            m2 = bin(m1)[2:]
            if len(m2)== 6:
                m2 = m2+'00'
            if len(m2)== 7:
                m2 = m2+'0'
            m3 = list(m2)
            message = list(map(int, m3))
            
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

            for n in range(len(player_two_guesses_quantum)):
                if player_two_guesses_quantum[n]==1:
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
                if i == 63:
                    print('Random key is correct! Player 2 WINS')
            else:   
                print("Random key is incorrect! Player 2 LOSES")
    
    else:
        print('Player 2 loses :/')

else:
    print()
    print('If you do not type PLAY you will not start the game')


print()
print()
print()
print('GAME OVER.')
print('Re-run this script to play again')
