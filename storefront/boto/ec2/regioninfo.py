# Copyright (c) 2006-2008 Mitch Garnaat http://garnaat.org/
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

class RegionInfo(object):
    """
    Represents an EC2 Region
    """
    
    def __init__(self, connection=None, name=None, endpoint=None):
        self.connection = connection
        self.name = name
        self.endpoint = endpoint

    def __repr__(self):
        return 'RegionInfo:%s' % self.name

    def startElement(self, name, attrs, connection):
        return None

    def endElement(self, name, value, connection):
        if name == 'regionName':
            self.name = value
        elif name == 'regionEndpoint':
            self.endpoint = value
        else:
            setattr(self, name, value)

    def connect(self, **kw_params):
        """
        Connect to this Region's endpoint. Returns an EC2Connection
        object pointing to the endpoint associated with this region.
        You may pass any of the arguments accepted by the EC2Connection
        object's constructor as keyword arguments and they will be
        passed along to the EC2Connection object.
        
        :rtype: :class:`boto.ec2.connection.EC2Connection`
        :return: The connection to this regions endpoint
        """
        from boto.ec2.connection import EC2Connection
        return EC2Connection(region=self, **kw_params)


