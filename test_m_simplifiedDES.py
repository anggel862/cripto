
import unittest
import os
from m_simplifiedDES import *
    
class TestMSimplifiedDES(unittest.TestCase):

    def test_inputErrors_behaviour(self):
        self.assertRaises((ValueError, TypeError),inputErrors,("message", "000000"))
        self.assertRaises((ValueError, TypeError),inputErrors,("message", ""))
        self.assertRaises((ValueError, TypeError),inputErrors,("cipherkey", "000000"))
        self.assertRaises((ValueError, TypeError),inputErrors,("cipherkey", ""))
        self.assertRaises((ValueError, TypeError),inputErrors,("ciphe", "100111100"))
        self.assertEqual(inputErrors("message","000000000000"),False)
        self.assertEqual(inputErrors("message","100111100011"),False)
        self.assertEqual(inputErrors("cipherkey","100111100"),False)

    def test_generateSubKey(self):
        generatedSubKeys = ["12345678", "23456789", "34567891", "45678912", "56789123", "67891234", "78912345", "89123456", "91234567"]
        self.assertEqual(generateSubKey(cipherKey="123456789",currentRound=1,iterations=8),generatedSubKeys[0])
        self.assertEqual(generateSubKey(cipherKey="123456789",currentRound=2,iterations=8),generatedSubKeys[1])
        self.assertEqual(generateSubKey(cipherKey="123456789",currentRound=3,iterations=8),generatedSubKeys[2])
        self.assertEqual(generateSubKey(cipherKey="123456789",currentRound=4,iterations=8),generatedSubKeys[3])
        self.assertEqual(generateSubKey(cipherKey="123456789",currentRound=5,iterations=8),generatedSubKeys[4])
        self.assertEqual(generateSubKey(cipherKey="123456789",currentRound=6,iterations=8),generatedSubKeys[5])
        self.assertEqual(generateSubKey(cipherKey="123456789",currentRound=7,iterations=8),generatedSubKeys[6])
        self.assertEqual(generateSubKey(cipherKey="123456789",currentRound=8,iterations=8),generatedSubKeys[7])

    def test_expand(self):
        self.assertEqual(expand(message="123456"),"12434356")

    def test_operationXOR(self):
        self.assertEqual(operationXOR(a="0",b="0"),"0")
        self.assertEqual(operationXOR(a="0",b="1"),"1")
        self.assertEqual(operationXOR(a="1",b="0"),"1")
        self.assertEqual(operationXOR(a="1",b="1"),"0")

    def test_xor(self):
        self.assertEqual(xor(a="10101010",b="01100101",n=8),"11001111")
        self.assertEqual(xor(a="01100101",b="10101010",n=8),"11001111")
    
    def test_sBox(self):
        self.assertEqual(sBox(1, "1100"),"000")
        self.assertEqual(sBox(1, "1001"),"100")
        self.assertEqual(sBox(1, "1011"),"010")
        self.assertEqual(sBox(1, "0001"),"010")
        self.assertEqual(sBox(1, "0011"),"110")
        self.assertEqual(sBox(1, "1010"),"110")
        self.assertEqual(sBox(2, "1111"),"100")
        self.assertEqual(sBox(2, "1110"),"001")
        self.assertEqual(sBox(2, "0101"),"001")
        self.assertEqual(sBox(2, "1001"),"011")
        self.assertEqual(sBox(2, "0111"),"010")

    def test_f(self):
        self.assertEqual(f("100110", "01100101"),"000100")
        self.assertEqual(f("011000", "11001010"),"100001")
        self.assertEqual(f("001110", "10011001"),"110010")

    def test_simplifiedDES_encrypt(self):
        self.assertEqual(simplifiedDES_Encrypt(messageToEncrypt="011101110011", cipherKey="011011011", iterations=8),"110000010100")
        self.assertEqual(simplifiedDES_Encrypt(messageToEncrypt="011100100110", cipherKey="011001010", iterations=8),"000111001110")
   
    def test_simplifiedDES_Decrypt(self):
        self.assertEqual(simplifiedDES_Decrypt(messageToDecrypt="110000010100", cipherKey="011011011", iterations=8),"011101110011")
        self.assertEqual(simplifiedDES_Decrypt(messageToDecrypt="000111001110", cipherKey="011001010", iterations=8),"011100100110")

    def test_bruteForce_simplifiedDES(self):
        self.assertEqual(bruteForce_simplifiedDES(originalMessage="011101110011", encryptedMessage="110000010100", iterations=8),True)
        self.assertEqual(bruteForce_simplifiedDES(originalMessage="011101110011", encryptedMessage="000111001110", iterations=8),False)

if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        print("Exception SystemExit occurred!")