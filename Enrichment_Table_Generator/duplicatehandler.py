import sys

### Function which ignores, deletes, or selects most frequent ID endpoints with duplicates ###

def handle_duplicates(table, mypass):
    myid = table.columns[0]

    if mypass > 2 or mypass < 0:
        print('invalid duplicate id')
        sys.exit(0)
    else:
        pass

    lastid = 0
    count = 0
    droplist = []

    for i, row in zip(table.duplicated(subset=myid, keep=False), table.iterrows()):
        # print(i, row[0], row[1][myid], lastid, count)
        if i == True and str(lastid) != str(row[1][myid]) and count == 0:
            # print('if')
            lastid = row[1][myid]
            count += 1
            if mypass == 1:
                # print(row[0])
                droplist.append((row[0]))

        elif count > 0 and str(lastid) != str(row[1][myid]):
            # print('elif1')
            mylist = []
            for k in range(int(count)):
                mylist.append(int(row[0] - k - 1))
            table = table.append(table.iloc[mylist].mean(axis=0, numeric_only=True, skipna=True).T, ignore_index=True)
            table.iloc[-1,0] = table.iloc[mylist[0],0]
            if table.iloc[-1,1] >= 0.5:
                table.iloc[-1, 1] = 1
            else:
                table.iloc[-1,1] = 0
            droplist.extend(mylist)
            count = 0

            if i == True:
                # print('nested_if')
                lastid = row[1][myid]
                count += 1
                if mypass == 1:
                    droplist.append(row[0])
            else:
                # print('nested_else')
                lastid = row[1][myid]
                count = 0

        elif i == True and str(lastid) == str(row[1][myid]) and mypass == 2:
            # print('elif2')
            count += 1
            lastid = row[1][myid]

        elif i == True and str(lastid) == str(row[1][myid]) and mypass == 1:
            # print('elif3')
            lastid = row[1][myid]
            count = 0
            droplist.append(row[0])

        else:
            # print('else')
            lastid = row[1][myid]
            count = 0
    table = table.drop(droplist)

    # make sure column is int
    table.iloc[:,1] = table.iloc[:,1].astype(int)

    return table

# # # TEST # # #
if __name__=='__main__':
    import pandas as pd
    a = [['DTXCID101', 0], ['DTXCID101', 0], ['DTXCID101', 1], ['DTXCID202', 1], ['DTXCID202', 1], ['DTXCID303', 0], ['DTXCID303', 0], ['DTXCID404', 0]]
    a = pd.DataFrame(a)
    print('most_frequent', handle_duplicates(a, 2))
    print('remove', handle_duplicates(a, 1))
    print('leave', handle_duplicates(a, 0))
