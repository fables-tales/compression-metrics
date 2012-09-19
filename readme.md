#Compression metrics

My friend Luke is trying to invent his own compression algorithm, so I thought
I'd make this repo to help him out, it's got a python script in it to assess
compression metrics.

##Hey Luke, read this!

To add a new compression method you need to do a few things, I've done some
of the legwork for you already though. In the main block there's a function
call to `compare_compression_methods(bzip,gzip,luke)` this is the list of
compression methods to be tested.

A compression method is a function that takes a filename, and returns a number
of bytes and the md5 of the decompressed file (this lets you test that you've
compressed/decompressed correctly).

I've already rolled one that's called luke, you'll need to change it. Look:

    def luke(filename):
        #luke put your code here
        return len(open(filename).read()), '0'

if you put your code there you'll get some leet output, at that point you
just need to run the `compression_metrics.py` file and amazing things will
happen
