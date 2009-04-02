#Martin Lacayo-Emery
#11/20/2008

import struct, datetime, decimal, itertools

class DatabaseFile:
    def __init__(self,fieldnames,fieldspecs,records):
        self.fieldnames=fieldnames
        self.fieldspecs=fieldspecs
        self.records=records

    def extend(self,other):
        """
        Plus equals
        """
        if len(self.records)!=len(other.records):
            raise ValueError, "The number of rows do not match."

        self.fieldnames.extend(other.fieldnames)
        self.fieldspecs.extend(other.fieldspecs)
        for i in range(len(self.records)):
            self.records[i].extend(other.records[i])                

    def addColumn(self,fieldname,fieldspec,record):
        if len(record)!=len(self.records):
            raise ValueError,"The column length does not match the current table."
        self.fieldnames.append(fieldname)
        self.fieldspecs.append(fieldspec)
        for id,r in enumerate(record):
            self.records[id].extend(r)

    def addRow(self,record):
        if len(record)==len(self.fieldnames):
            self.records.append(record)
        else:
            raise ValueError, "The record does have the same number of columns as the table."

    def readFile(self,inName):
        inFile=open(inName,'rb')
        self.records=list(self.read(inFile))
        self.fieldnames=self.records.pop(0)
        self.fieldspecs=self.records.pop(0)
        self.records=[map(float,r) for r in self.records]
        inFile.close()

    def read(self,f):
        """Returns an iterator over records in a Xbase DBF file.

        The first row returned contains the field names.
        The second row contains field specs: (type, size, decimal places).
        Subsequent rows contain the data records.
        If a record is marked as deleted, it is skipped.

        File should be opened for binary reads.

        """
        # See DBF format spec at:
        #     http://www.pgts.com.au/download/public/xbase.htm#DBF_STRUCT

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

    def writeFile(self,outName):
        outFile=open(outName,'wb')
        self.write(outFile)
        outFile.close()

    def write(self,f):
        """ Return a string suitable for writing directly to a binary dbf file.

        File f should be open for writing in a binary mode.

        Fieldnames should be no longer than ten characters and not include \x00.
        Fieldspecs are in the form (type, size, deci) where
            type is one of:
                C for ascii character data
                M for ascii character memo data (real memo fields not supported)
                D for datetime objects
                N for ints or decimal objects
                L for logical values 'T', 'F', or '?'
            size is the field width
            deci is the number of decimal places in the provided decimal object
        Records can be an iterable over the records (sequences of field values).
        
        """
        # header info
        ver = 3
        now = datetime.datetime.now()
        yr, mon, day = now.year-1900, now.month, now.day
        numrec = len(self.records)
        numfields = len(self.fieldspecs)
        lenheader = numfields * 32 + 33
        lenrecord = sum(field[1] for field in self.fieldspecs) + 1
        hdr = struct.pack('<BBBBLHH20x', ver, yr, mon, day, numrec, lenheader, lenrecord)
        f.write(hdr)
                          
        # field specs
        for name, (typ, size, deci) in itertools.izip(self.fieldnames, self.fieldspecs):
            name = name.ljust(11, '\x00')
            fld = struct.pack('<11sc4xBB14x', name, typ, size, deci)
            f.write(fld)

        # terminator
        f.write('\r')

        # records
        for record in self.records:
            f.write(' ')                        # deletion flag
            for (typ, size, deci), value in itertools.izip(self.fieldspecs, record):
                if typ == "N":
                    value = str(value).rjust(size, ' ')
                elif typ == 'D':
                    value = value.strftime('%Y%m%d')
                elif typ == 'L':
                    value = str(value)[0].upper()
                else:
                    value = str(value)[:size].ljust(size, ' ')
                try:
                    assert len(value) == size
                except AssertionError:
                    raise AssertionError, "value "+str(value)+" is no good "+str(size)
                f.write(value)

        # End of file
        f.write('\x1A')