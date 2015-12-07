"On my honor, as a University of Colorado at Boulder student, I have neither given nor received unauthorized assistance."
"Tyler Scott"
"ID: 103289678"

import sys
import random
import math
import time

def main(argv):
    
    #Run the cryptography algorithm for any command line arguments given
    if len(argv) >= 2:
        for k in range (1, len(argv)):
            n1 = sys.argv[k]
            print "n = " + str(n1) + " bits"
            #Start time for generating public and private keys
            startTime = time.clock()
            
            #Get values for N,e,d in the generateKeys function
            N,e,d = generateKeys(int(n1))
            
            #Get end time for generating the public and private keys
            partATime = time.clock() - startTime
            
            #Output the values for N,e,d for user 
            print "N = " + str(N)
            print "e = " + str(e)
            print "d = " + str(d) + "\n"
            
            #Variable to store the original message, given in problem
            message = 2015
            
            #Output the original message for user
            print "Original Message: " + str(message)
        
            #Start time for encoding the original message
            startTime = time.clock()
        
            #Encode the original message by running modual exponentiation function
            encodeMessage = modexp(message, e, N)
            
            #Get end time for encoding the original message
            partBTime = time.clock() - startTime
        
            #Output the encoded message for user
            print "Encoded Message: " + str(encodeMessage)
            
            #Start time for decoding the encoded message
            startTime = time.clock()
        
            #Decode the encoded message using the modular exponentiation function
            decodeMessage = modexp(encodeMessage, d, N)
            
            #Get end time for decoding the encoded message
            partCTime = time.clock() - startTime
        
            #Output the decoded message for user
            print "Decoded Message: " + str(decodeMessage) + "\n" 
            
            #Output the time it took for each part of the problem
            print "Time to generate public and private keys: " + str(partATime) + " seconds"
            print "Time to encode the message '2015': " + str(partBTime) + " seconds"
            print "Time to decode the encoded message: " + str(partCTime) + " seconds\n"
        
    #n starts out at length 128 bits
    n = 128
    
    #for i in range (0, 3):
        
    print "n = " + str(n) + " bits"
    #Start time for generating public and private keys
    startTime = time.clock()
        
    #Get values for N,e,d in the generateKeys function
    N,e,d = generateKeys(int(n))
        
    #Get end time for generating the public and private keys
    partATime = time.clock() - startTime
        
    #Output the values for N,e,d for user 
    print "N = " + str(N)
    print "e = " + str(e)
    print "d = " + str(d) + "\n"
        
    #Variable to store the original message, given in problem
    message = 2015
        
    #Output the original message for user
    print "Original Message: " + str(message)
    
    #Start time for encoding the original message
    startTime = time.clock()
    
    #Encode the original message by running modual exponentiation function
    encodeMessage = modexp(message, e, N)
        
    #Get end time for encoding the original message
    partBTime = time.clock() - startTime
    
    #Output the encoded message for user
    print "Encoded Message: " + str(encodeMessage)
        
    #Start time for decoding the encoded message
    startTime = time.clock()
    
    #Decode the encoded message using the modular exponentiation function
    decodeMessage = modexp(encodeMessage, d, N)
        
    #Get end time for decoding the encoded message
    partCTime = time.clock() - startTime
    
    #Output the decoded message for user
    print "Decoded Message: " + str(decodeMessage) + "\n" 
        
    #Output the time it took for each part of the problem
    print "Time to generate public and private keys: " + str(partATime) + " seconds"
    print "Time to encode the message '2015': " + str(partBTime) + " seconds"
    print "Time to decode the encoded message: " + str(partCTime) + " seconds\n"
        
    #n += 128;
    
    return
    
#Function used to generate the public and private keys
def generateKeys(n):
    
    #Boolean variables to store if p, q, and e are prime (relatively prime)
    isPPrime = False
    isQPrime = False
    isEPrime = False
    
    #Variables to store the values of p and q
    p = 0
    q = 0
      
    #Loop until you have two prime values for p and q of n bit length  
    while isPPrime == False or isQPrime == False:
        if isPPrime == False:
            p = random.getrandbits(n)
            if isPrime(p) == True:
                isPPrime = True
        if isQPrime == False:
            q = random.getrandbits(n)
            if isPrime(q) == True:
                isQPrime = True
                
    print "\np = " + str(p)
    print "q = " + str(q) + "\n"
    
    #Compute N and phi
    N = p * q
    phi = (p-1)*(q-1)
    
    #Variables to store the encryption key and decryption key
    encrypt = 0
    decrypt = 0
    
    #Find a value for e that is relatively prime to phi and also store the modular inverse in decrypt
    while isEPrime == False:
        encrypt = random.randint(3, phi-1)
        decrypt,y,d = extendedEuclid(encrypt, phi)
        if d == 1:
            isEPrime = True
       
     
    #If the decrypt value is negative, make it positive
    if decrypt < 0:
        decrypt += phi
        
    return N,encrypt,decrypt
            
def isPrime(number): 
    #Use Fermat's Little Theorem with base 2, 3, and 5 to check primality
    if modexp(2, number-1, number) != 1 or modexp(3, number-1, number) != 1 or modexp(5, number-1, number) != 1:
        return False
    else:
        return True
       
#Function used to compute the least common denominator as well as the modular inverse of a and modular inverse of b
def extendedEuclid(a,b):
    #Base Case    
    if b == 0:
        return 1,0,a
        
    x,y,d = extendedEuclid(b, a % b)
    
    return (y, x - (long(math.floor(a/b)))*y, d)  
   
#Function used to compute the modular exponent efficiently
#x^y (mod N)
def modexp(x, y, N):
    #Base Case    
    if y == 0:
        return 1
        
    z = modexp(x, y/2, N)
    
    if y % 2 == 0:
        return (z**2) % N
    else:
        return (x * (z**2)) % N
    
if __name__ == "__main__":
    main(sys.argv)
