import re
import sys
import getopt

def main(argv):
    try:
        opts, args = getopt.getopt(sys.argv[1:],"h:i:o:p:",["help","infile","outfile","patterns"])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

    input_file=None
    output_file=None
    pattern_string = None

    for x, a in opts:
     
        if x in ("-h","--help"):
            usage()
            sys.exit()
        elif x in ("-i", "--infile"):
            input_file = a
        elif x in("-o","--outfile"):
            output_file = a
        elif x in ("-p","--patterns"):
            pattern_string = str(a)
        else:
            assert False, "unknown argument"
            usage()


    infile = open(input_file, 'r')
    outfile = open(output_file, 'w')
    patt = re.compile(pattern_string)
   
    for line in infile:

        m = patt.search(line)
        if m:
            
            outfile.write(line + "\n")

    infile.close()
    outfile.close()
  


def usage():

    print 'Usage: -i infile -o outfile -p regex pattern'
    print 'specify full paths for infile and outfile'
    print 'iterates through lines in a log file and saves out any line matching regex'

    sys.exit(0)
    
if __name__=="__main__":
     main( sys.argv )
  

            