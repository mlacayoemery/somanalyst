import struct

class DBF:
    def __init__(self):
        self.fieldnames=[]
        self.fieldspecs=[]
        self.records=[]        

    def addRow(self,row):
        self.records.append(row)

    def addCol(self,column):
        self.fieldnames.append(column)
        for record in self.records:
            record.append("")

    def __str__(self):
        return "header: "+str(self.header)

    def read(self,file):
        numrec, lenheader = struct.unpack('<xxxxLH22x', f.read(32))    
        numfields = (lenheader - 33) // 32

        fields = []
        for fieldno in xrange(numfields):
            name, typ, size, deci = struct.unpack('<11sc4xBB14x', f.read(32))
            name = name.replace('\0', '')       # eliminate NULs from string   
            fields.append((name, typ, size, deci))
        yield [field[0] for field in fields]
        yield [tuple(field[1:]) for field in fields]

        terminator = f.read(1)
        assert terminator == '\r'

        fields.insert(0, ('DeletionFlag', 'C', 1, 0))
        fmt = ''.join(['%ds' % fieldinfo[2] for fieldinfo in fields])
        fmtsiz = struct.calcsize(fmt)
        for i in xrange(numrec):
            record = struct.unpack(fmt, f.read(fmtsiz))
            if record[0] != ' ':
                continue                        # deleted record
            result = []
            for (name, typ, size, deci), value in itertools.izip(fields, record):
                if name == 'DeletionFlag':
                    continue
                if typ == "N":
                    value = value.replace('\0', '').lstrip()
                    if value == '':
                        value = 0
                    elif deci:
                        value = decimal.Decimal(value)
                    else:
                        value = int(value)
                elif typ == 'D':
                    y, m, d = int(value[:4]), int(value[4:6]), int(value[6:8])
                    value = datetime.date(y, m, d)
                elif typ == 'L':
                    value = (value in 'YyTt' and 'T') or (value in 'NnFf' and 'F') or '?'
                result.append(value)
            yield result
        

if __name__ == "__main__":
    test = DBF()
    test.addCol("1")
    test.addCol("2")
    print "DBF Testing"
    print test

        