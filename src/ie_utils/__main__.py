from ie_utils import tokenize
import sys
import argparse



def main():
    parser = argparse.ArgumentParser(description="Tokenizer")
    parser.add_argument("sentence", type=str, help="Sentence to tokenize.")
    args = parser.parse_args()
    sentence = args.sentence
    #print(sys.argv)
    print(tokenize(sentence))

if __name__ == "__main__":
    main()