import io
import re
import argparse

def parse_order_messages(f, tags_to_print,out_file=None, sep="|"):
    tags_to_print.sort()
    line_count=0
    records=[]
    header=','.join(str(i) for i in tags_to_print)
    for line in f.readlines():
        # print(str)
        line_count+=1
        fix_msg = re.search(r"\[(.*?)]", line).group(1)
        # print(fix_msg)
        values=fix_msg.split(sep)
        values.remove('')
        # print(values)
        order={}
        for p in values:
            (tag, value) = p.split('=')
            # print(f'{tag=} {value=}')
            if int(tag) in tags_to_print:
                order[int(tag)]=value
        # print(order)
        record=''
        for tag in tags_to_print:            
            record+=order[tag] if tag in order else ''
            record+=','
        records.append(record)

    print(f'{line_count=}')
    if out_file==None:
        print(header)
        for record in records:
            print(record)
    else: 
        with open(out_file, mode='x') as output:
            output.write(f'{header}\n')      
            for record in records:
                output.write(f'{record}\n')

def menu():
    parser = argparse.ArgumentParser(description='Command line application example')
    parser.add_argument('-i','--in_fix', help='Input FIX log', type=argparse.FileType('r'), required=True)
    parser.add_argument('-o','--out_fix', help='Output FIX log. If default=None, print to screen ', default=None, required=False)
    parser.add_argument('-s','--fix_sep', help='FIX tag/value separator', default="|", required=False)
    parser.add_argument('-tags','--tags', help='List of tags to extract, separeted by comma', default="11,54,48,22,38,52,60,40,44", required=False)
    args = vars(parser.parse_args())
    return args 

def main():
    args = menu()
    # print(args)
    in_file=args['in_fix']
    out_file=args['out_fix']
    fix_sep=args['fix_sep']

    tags_to_print = list(map(int, args['tags'].split (','))) 
    parse_order_messages(in_file, tags_to_print, out_file, sep=fix_sep)

if __name__ == '__main__':
    main()