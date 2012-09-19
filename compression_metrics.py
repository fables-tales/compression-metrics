import os
import hashlib
import zlib
import subprocess
import bz2

NUMBER_RANDOM_BYTES = 1024*40

def get_random_sample():
    with open(".data/random_data", "wb") as data:
        urandom = open("/dev/urandom", "r")
        read_iterations = 1024
        for i in range(0,read_iterations):
            to_read = NUMBER_RANDOM_BYTES/read_iterations
            data.write(urandom.read(to_read))

def url_to_file(filename, url):
    p = subprocess.Popen(["wget",url,"-O",filename], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    p.wait()

def ensure_random_sample():
    if not os.path.exists(".data/random_data"):
        get_random_sample()

def ensure_bbc_homepage():
    if not os.path.exists(".data/bbc_homepage"):
        url_to_file(".data/bbc_homepage", "http://www.bbc.co.uk/news/")

def ensure_oliver_twist():
    if not os.path.exists(".data/oliver_twist"):
        url_to_file(".data/oliver_twist", "ftp://ftp.ibiblio.org/pub/docs/books/gutenberg/7/3/730/730.txt")

def ensure_have_data_files():
    if not os.path.exists(".data"):
        os.mkdir(".data")

    ensure_random_sample()
    ensure_bbc_homepage()
    ensure_oliver_twist()

#compression methods
def bzip(filename):
    compressed_data = bz2.compress(open(filename).read())
    compressed_size = len(compressed_data)
    decompressed_data_md5 = hashlib.md5(bz2.decompress(compressed_data)).hexdigest()

    return compressed_size, decompressed_data_md5

def gzip(filename):
    compressed_data = zlib.compress(open(filename).read())
    compressed_size = len(compressed_data)
    decompressed_data_md5 = hashlib.md5(zlib.decompress(compressed_data)).hexdigest()
    return compressed_size, decompressed_data_md5

def luke(filename):
    #luke put your code here
    return len(open(filename).read()), '0'

def run_technique(file, technique, error_techniques):
    file_data = open(file).read()
    correct_md5 = hashlib.md5(file_data).hexdigest()
    count,hash = technique(file)
    print "%10s %30d %15.1f %10s" % (technique.__name__, count, 100.0-(count*100.0/len(file_data)), file)
    if hash != correct_md5:
        error_techniques.add(technique.__name__)

def compare_compression_methods(*args):
    data_files = ["oliver_twist", "random_data", "bbc_homepage"]
    files = [".data/" + x for x in data_files]
    print "%10s %30s %15s %10s" % ("technique", "byte count after compression", "compression %", "filename")
    error_techniques = set()
    for file in files:
        for technique in args:
            run_technique(file, technique, error_techniques)
        print

    for technique in error_techniques:
        print "technique", technique, "compresses/decompresses wrong!"

if __name__ == "__main__":
    ensure_have_data_files()
    print 
    compare_compression_methods(bzip,gzip,luke)
