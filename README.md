URAP
====
sel.xpath('//span[@itemprop="street-address"]/text()').extract()
^This selects the address and gets the string I think.
I didnt have much time today to look at it, but this should give us a starting point.
This thing looks for the <span> tag with the attribute 'itemprop' set equal to "street-address" and
gets its text.

-Chris
