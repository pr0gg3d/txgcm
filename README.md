txgcm
=====

txgcm is a Python Twisted wrapper for [Google Cloud Messaging](http://developer.android.com/guide/google/gcm/index.html)

*This project is in an ALPHA state*

Requirements
------------
pygcm

Installation
------------

Getting Started
---------------

    from twisted.internet import reactor
    from txgcm import GcmClient

    # Create client
    API_KEY = '1234'
    c = GcmClient(API_KEY)

    # Set registration ids
    reg_ids = ['12', '23', '34']

    # Set data to send
    data = { 'score' : 100 }

    # define a callback (and an errback
    def done(result):
        print(result)

    # Send data
    d = c.send(reg_ids, data)

    # Add a callback
    d.addCallback(done)
    
    # Run the reactor
    reactor.run()

*TBF*
