==================
Event Management
==================

The event management system allows you to manage Ninja participations to your events. To use it, first you need to create at least one event. Then, you need to create ``Participant``\ s. The ``uuid`` field allows you to give a unique id to your Ninjas. This can be used in the event check-in process.

Part of the event management system is the ``Badge``\ s feature\: you can define and assign ``Badge``\ s to participant. They will be shown in the event page so the all Ninjas can see what their friends have achieved, and be encouraged to obtain badges themselves!

Participants are connected to events using ``Ticket``\ s. A ticket is for one participant and one event. ``Ticket``\ s have their ``uuid``, too.
Currently there is no feature to import tickets, so you'll have to create them by hand.

The check-in procedure can be performed using either the participant's or the ticket's ``uuid`` (besides the participant name). This is useful if you have tickets with QR codes, or participant badges with QR codes representing the participant ``uuid``, and you are accessing the toolbox from a smartphone with a QR code keyboard (e.g. `this one <https://bit.ly/2P0iQVw>`_ ).

