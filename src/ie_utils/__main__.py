from ie_utils import tokenize
import sys
def main():
    if len(sys.argv) > 1:
        sentence = sys.argv[1]
    else:
        sentence = "Hello world"
    #print(sys.argv)
    print(tokenize(sentence))

if __name__ == "__main__":
    main()