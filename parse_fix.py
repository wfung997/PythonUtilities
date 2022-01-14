import io
import re

def parse_order_messages(f, tags_to_print,out_file=None):
    tags_to_print.sort()
    line_count=0
    records=[]
    header=','.join(str(i) for i in tags_to_print)
    for line in f.readlines():
        # print(str)
        line_count+=1
        fix_msg = re.search(r"\[(.*?)]", line).group(1)
        # print(fix_msg)
        values=fix_msg.split('|')
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
        

        # for tag in tags_to_print: 

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

def main():
    in_file='C:\\in.log'
    out_file='C:\\out.log'

    # with  open (in_File) as f:
    #     tags_to_print =[11,54,48,22,38,52,60,40,44]
    #     parse_order_messages(f,tags_to_print)
    with  open (in_file) as f:
        tags_to_print =[11,39,41,52,60,14]
        parse_order_messages(f, tags_to_print,out_file)

if __name__ == '__main__':
    main()