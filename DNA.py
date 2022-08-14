def main():
    sequence = input("Please enter Nucleic acid sequence: ")

    NA_type = input("Type: ").upper()

    if NA_type == 'DNA':
        if NA.verify_DNA(sequence, NA_type) != True :
            print("input valid nucleotide for DNA")
        else:
            print(NA.verify_DNA(sequence, NA_type))
            print(NA.transcribe(sequence, NA_type))
            print(f"Start codoon found at {NA.find_start(NA.transcribe(sequence, NA_type))} and Stop codon found at {NA.find_stop(NA.transcribe(sequence, NA_type))}")

    elif NA_type == 'RNA':
        if NA.verify_RNA(sequence, NA_type) != True:
            print("Input valid nucleotide sequence for RNA")
        else:
            print(NA.verify_RNA(sequence, NA_type))
            print(f"Start codoon found at {NA.find_start(sequence)} and Stop codon found at {NA.find_stop(sequence)}")


class NA:
    def verify_DNA(sequence, NA_type):

        if NA_type != 'DNA':
            return False

        nucleotides = ['A', 'T', 'C', 'G']
        #Handle case-insensitvely
        sequence = str(sequence.upper())

        #initialse counter to detect fakes
        counter = 0

        for i in range(len(sequence)):
            #Iterate through the keys nucleotide
            #Check if N at position i is in nucleotides
            if sequence[i] in nucleotides:
                counter += 0
            else:
                counter += 1
        if counter > 0:
            return False
        else:
            return True

    def verify_RNA(sequence, NA_type):

        if NA_type != 'RNA':
            return False

        nucleotides = ['A', 'U', 'C', 'G']
        #Handle case-insensitvely
        sequence = str(sequence.upper())

        #initialse counter to detect fakes
        counter = 0

        for i in range(len(sequence)):
            #Iterate through the keys nucleotide
            #Check if N at position i is in nucleotides
            if sequence[i] in nucleotides:
                counter += 0
            else:
                counter += 1
        if counter > 0:
            return False
        else:
            return True


    def transcribe(sequence, NA_type):
        if NA.verify_DNA(sequence, NA_type) == True:
            sequence = sequence.replace('T', 'U')
        return sequence

    def find_start(sequence):
        #scan codons from the sequence
        window_size = 3
        for i in range(0, len(sequence) - window_size +1, window_size):
            if sequence[i: i+ window_size] == "AUG":
                return i

    def find_stop(sequence):
        #scan codons to find stop codons
        window_size = 3
        for i in range(0, len(sequence)-window_size+1, window_size):
            if sequence[i: i+window_size] == "UAA" or sequence[i: i+window_size] == "UAG" or sequence[i: i+window_size] == "UGA":
                return i




if __name__ == "__main__":
    main()
