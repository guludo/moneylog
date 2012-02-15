#!/usr/bin/env python
# Aurelio Jargas, http://aurelio.net/moneylog/
#
# Generates the ok.txt file, used to test MoneyLog parsing.

year = 2000
month = 0

space_formats = [
    ' ',
    '    ',
    '\t',
    ' \t',
    '\t ',
    '\t\t ',
    ' \t \t ',
]
number_formats = [
    '0',
    '0.00',
    '0,00',
    '0000',
    '0000.00',
    '0000,00',
    '1',
    '1.00',
    '1,00',
    '10',
    '10.00',
    '10,00',
    '1000',
    '1.000',
    '1.000,00',
    '1,000.00',
    '1000,00',
    '1000.00',
    '1.234.567,89',
    '1,234,567.89',
    '1234567,89',
    '10/1',
    '10/5',
    '10.00/5',
    '10,00/5',
    '10*1',
    '10*5',
    '10.00*5',
    '10,00*5',
]

def title(msg):
    print
    print
    print "########## " + msg
    print "#"

#-------------------------------------------------------------

print "# http://aurelio.net/moneylog/"
print "# MoneyLog test file."
print "# 100% OK when: no errors raised, month balance is always zero."
print "#"
print "# DO NOT EDIT. Automatically generated by ok-generator.py."
print "#"
print "# Use these settings to test this file:"
print "#   reportType = 'm';"
print "#   checkDateFrom = false;"
print "#   useLegacyDataFormat = false;"
print "#   dataFiles = ['test/ok.txt'];"

#-------------------------------------------------------------

title("Blank lines with TABs and spaces (ignored)")

for x in space_formats:
    print x

#-------------------------------------------------------------

title("Gotchas")

month += 1

print "# Tag delimiter alone: no tag, no description"
print "%d-%02d-%02d -1 |"                                       % (year, month, 1)
print "#"
print "# Pipes in description"
print "%d-%02d-%02d -1 tag1,tag2||"                             % (year, month, 2)
print "%d-%02d-%02d -1 tag1,tag2|one|pipe"                      % (year, month, 3)
print "%d-%02d-%02d -1 tag1,tag2||two pipes around|"            % (year, month, 4)
print "#"
print "# Comma confusion in tags"
print "%d-%02d-%02d -1 tag1,,tag2|two commas"                   % (year, month, 5)
print "%d-%02d-%02d -1 , ,tag1,\t,tag2,\t \t,| comma nightmare" % (year, month, 6)
print "%d-%02d-%02d -1 ,,,,,|only commas"                       % (year, month, 7)
print "#"
print "# Now the positive values to zero the month balance"
print "%d-%02d-%02d 2 reset no tag"                             % (year, month, 99)
print "%d-%02d-%02d 5 tag1,tag2| reset tags"                    % (year, month, 99)

#-------------------------------------------------------------

title("Delimiter formats")

month += 1

for x in space_formats:
    print "%d-%02d-%02d%s-1%sdescription"           % (year, month, 1, x, x)
for x in space_formats:
    print "%d-%02d-%02d%s-1%stag|%sdescription"     % (year, month, 2, x, x, x)
for x in space_formats:
    print "%d-%02d-%02d%s-1%stag%s|%sdescription"   % (year, month, 3, x, x, x, x)
for x in space_formats:
    print "%d-%02d-%02d%s-1%stag%s|%sdescrip%stion" % (year, month, 4, x, x, x, x, x)

print "#"
print "# Leading spaces are discouraged, but they are stripped by ML"
for x in space_formats:
    print "%s%d-%02d-%02d%s-1%sdescription"         % (x, year, month, 5, x, x)

print "#"
print "# Now the positive values to zero the month balance"
print "%d-%02d-99 %d description"     % (year, month, len(space_formats)*2)
print "%d-%02d-99 %d tag|description" % (year, month, len(space_formats)*3)

#-------------------------------------------------------------

title("Tag formats")

month += 1

# single tag
single_tag_formats = ['tag|']
for s in space_formats:
    single_tag_formats.append('tag' + s + '|')

# multiple tags
multi_tag_formats = ['tag1,tag2|']
for s in space_formats:
    multi_tag_formats.append('tag1,' + s + 'tag2|')
    multi_tag_formats.append('tag1,' + s + 'tag2' + s + '|')

d = 0
for x in single_tag_formats + multi_tag_formats:
    d += 1
    print "%d-%02d-%02d -1 %s" % (year, month, d, x)            # no description
    print "%d-%02d-%02d -1 %sdescription" % (year, month, d, x) # with description

print "#"
print "# Now the positive values to zero the month balance"
print "%d-%02d-99 %d tag|"       % (year, month, len(single_tag_formats)*2)
print "%d-%02d-99 %d tag1,tag2|" % (year, month, len( multi_tag_formats)*2)

#-------------------------------------------------------------

title("Number formats")

month += 1

d = 0
for x in number_formats:
    d += 1
    print "%d-%02d-%02d %s"  % (year, month, d, x)
    print "%d-%02d-%02d +%s" % (year, month, d, x)
    print "%d-%02d-%02d -%s" % (year, month, d, x)
    print "%d-%02d-%02d -%s" % (year, month, d, x)
