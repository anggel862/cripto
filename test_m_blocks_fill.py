
import unittest
import os
from m_blocks_fill import *
from m_simplifiedDES import *
    
class TestBlocksFill(unittest.TestCase):

    def test_stringToBinaryASCIIcode(self):
        self.assertEqual(stringToBinaryASCIIcode(
            stringToConvert="Ese Rodrigo jar que llega no te digo trigo por ahí"),
            "0100010101110011011001010010000001010010011011110110010001110010011010010110011101101111001000000110101001100001011100100010000001110001011101010110010100100000011011000110110001100101011001110110000100100000011011100110111100100000011101000110010100100000011001000110100101100111011011110010000001110100011100100110100101100111011011110010000001110000011011110111001000100000011000010110100011101101"
        )
        self.assertEqual(stringToBinaryASCIIcode(
            stringToConvert="patata"),
            "011100000110000101110100011000010111010001100001"
        )
        self.assertRaises(ValueError, stringToBinaryASCIIcode,
        "Va usté muy cargadoo al ataquerl diodeno no puedor a wan no te digo trigo por no llamarte Rodrigor.")

    def test_generatePseudoRandomBinary(self):
        sizeRandomGenerated = len(generatePseudoRandomBinary(length=100))
        sizeRandomGenerated2 = len(generatePseudoRandomBinary(length=50))
        sizeRandomGenerated3 = len(generatePseudoRandomBinary(length=1))
        self.assertEqual(sizeRandomGenerated, 100)
        self.assertEqual(sizeRandomGenerated2, 50)
        self.assertEqual(sizeRandomGenerated3, 1)
        self.assertEqual(generatePseudoRandomBinary(0),"0")
        self.assertRaises(ValueError, generatePseudoRandomBinary, (-1))

    def test_generateMessageBlocks(self):
        fooEntireBlocks = "0100010101110011011001010010000001010010011011110110010001110010011010010110011101101111001000000110101001100001011100100010000001110001011101010110010100100000011011000110110001100101011001110110000100100000011011100110111100100000011101000110010100100000011001000110100101100111011011110010000001110100011100100110100101100111011011110010000001110000011011110111001000100000011000010110100011101101"
        fooMessage1Converted = "0100000101101110001000000110010001101111001000000110111101101110001000000110011001110010011000010110111001101011011011100110010101110011011100110010000001110011011011110010000001100011011011110111001001100100011010010110000101101100011011000111100100100000011010010110110101101101011001010110010001101001011000010111010001100101001000000111001001100101011000110110111101101101011011010110010101101110011001000010000001100011011011110110111001110100011000010110100101101110011001010110010000101110"
        fooMessage2Converted = "01010100011010000110010100100000011101010110111001100100011001010110001101101001011100000110100001100101011100100110000101100010011011000110010100100000010101100110100101100111011001010110111011000011101010000111001001100101001001110111001100100000011000110111100101110000011010000110010101110010"
        listEntireBlocks = generateMessageBlocks(fooEntireBlocks[0:396], 12)
        listFooMessage1 = generateMessageBlocks(fooMessage1Converted, 12)
        listFooMessage2 = generateMessageBlocks(fooMessage2Converted, 12)

    def test_startBlocksTreatment(self):
        fooEntireBlocks = "0100010101110011011001010010000001010010011011110110010001110010011010010110011101101111001000000110101001100001011100100010000001110001011101010110010100100000011011000110110001100101011001110110000100100000011011100110111100100000011101000110010100100000011001000110100101100111011011110010000001110100011100100110100101100111011011110010000001110000011011110111001000100000011000010110100011101101"
        fooMessage1Converted = "0100000101101110001000000110010001101111001000000110111101101110001000000110011001110010011000010110111001101011011011100110010101110011011100110010000001110011011011110010000001100011011011110111001001100100011010010110000101101100011011000111100100100000011010010110110101101101011001010110010001101001011000010111010001100101001000000111001001100101011000110110111101101101011011010110010101101110011001000010000001100011011011110110111001110100011000010110100101101110011001010110010000101110"
        fooMessage2Converted = "01010100011010000110010100100000011101010110111001100100011001010110001101101001011100000110100001100101011100100110000101100010011011000110010100100000010101100110100101100111011001010110111011000011101010000111001001100101001001110111001100100000011000110111100101110000011010000110010101110010"
        listEntireBlocks = fillingBlockSchema(fooEntireBlocks[0:396])
        listFooMessage1 = fillingBlockSchema(fooMessage1Converted)
        listFooMessage2 = fillingBlockSchema(fooMessage2Converted)
        self.assertEqual(len(listEntireBlocks),420)
        self.assertEqual(len(listEntireBlocks),12*35)
        self.assertEqual(len(listFooMessage1),(41+2)*12)
        self.assertEqual(len(listFooMessage2),(24+2)*12)
        
        
    

if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        print("Exception SystemExit occurred!")