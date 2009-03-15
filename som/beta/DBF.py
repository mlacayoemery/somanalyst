import struct

class dbf:
    def __init__(self):
        self.fieldnames=['temp']
        self.fieldspecs=[('C',10,0)]
        self.records=[['Hello']]

    def __str__(self):
        ver=3
        yr=34
        mon=7
        day=11
        numrec = len(self.records)
        numfields = len(self.fieldspecs)
        lenheader = numfields * 32 + 33
        lenrecord = sum(field[1] for field in self.fieldspecs) + 1

        record = struct.pack('<BBBBLHH20x', ver, yr, mon, day, numrec, lenheader, lenrecord)

        # field specs
        for i in range(len(self.fieldnames)):
            name=self.fieldnames[i-1].ljust(11, '\x00')
            typ=self.fieldspecs[i-1][0]
            size=self.fieldspecs[i-1][1]
            deci=self.fieldspecs[i-1][2]

            record+=struct.pack('<11sc4xBB14x', name, typ, size, deci)
        record+='\r'

        for r in self.records:
            #deletion flag
            record+=' '
            for i,value in enumerate(r):
                typ=self.fieldspecs[i][0]
                size=self.fieldspecs[i][1]
                deci=self.fieldspecs[i][2]
                if typ == 'N':
                    value = str(value).rjust(size, ' ')
                elif typ == 'D':
                    value = value.strftime('%Y%m%d')
                elif typ == 'L':
                    value = str(value)[0].upper()
                else:
                    value = str(value)[:size].ljust(size, ' ')
                record+=value
        # End of file
        record+='\x1A'
        return record

ofile=open("E:/mlacayo/SOManalyst/dbf.dbf",'wb')
a=dbf()
ofile.write(str(a))
ofile.close()