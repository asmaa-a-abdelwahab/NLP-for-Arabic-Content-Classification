#!/usr/bin/env python
# coding: utf-8

import pickle
import argparse
from Preprocess import preprocess

args = None

# ----------------------------------------------------------------------
def get_args():
    """
    get_args() function creates required and optional arguments and returns a copy of the argument list to be used within the script.
    """
    parser = argparse.ArgumentParser(
        description="VMK-mer - Standalone tool that converts mutations in VCF file into\nk-mer sequences that are affected by these mutations.",
        epilog="This is where you might put example usage"
    )

    # required argument
    parser.add_argument('-f', action="store", required=True, help='Input txt file (*.txt)')
    parser.add_argument('-m', action="store", required=True, help='Input model name (lr, rf, svc or sgd)')

    arguments = vars(parser.parse_args())
    return arguments
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
def main():
    
    # Exception handling for input files format.
    if args['f'].endswith(".txt"):
        f = open(args['f'], "r")
        text = f.read()
        print('[	  OK       ] Reading Text file is done.')
    else:
        raise FileFormatError("\n[	  ERROR    ] Input File is not in Text format.")

    if args['m'].endswith(""):
        model = pickle.load(open('../Artifacts/'+args['m'], 'rb'))
        print('[	  OK       ] Reading vcf file is done.')
    else:
        raise FileFormatError("\n[	  ERROR    ] The model name isn't available")
    
    Category_lebels = {"أخرى":3 , "علوم وتكنولوجيا":2, "ريادة أعمال":1}
    Category_en = ['Entrepreneurship', 'Science & Technology', 'Other']
    text = preprocess(text)
    #print(text)
    out = model.predict([text])
    #print(out)
    print("\n\nThe class of this text is:\t{}\t({})".format(list(Category_lebels.keys())[list(Category_lebels.values()).index(out[0])], Category_en[out[0]]))
    print('\n')
    
if __name__ == '__main__':
    args = get_args()
    main()