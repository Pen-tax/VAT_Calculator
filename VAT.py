def VAT(total):
  return total * 0.20


def VAT_type(standard,reduced,zero):
  if VAT_type == standard:
    print(total*standard)
  if VAT_type == reduced:
    print(total*reduced)
  if VAT_type == zero:
    print(total*zero)

##main
total = 99.99
valueaddedtax = VAT(total)
topay = total + valueaddedtax
standard = 0.20
reduced = 0.05
zero = 0
##VAT Type
VATS = VAT_type(standard,reduced,zero)

print("total £{:.2f} VAT £{:.2f} To pay £{:.2f}".format(total,valueaddedtax,topay))


