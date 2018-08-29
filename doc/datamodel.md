# Datamodel

This document describes the conceptual datamodel, to facilitate understading of how the tool works and to support feature requests (as different Dojos might have different conceptual organizations). 

For logical and physical datamodel, take a look at the tables :-)

The datamodel is divided in coherent sets of entities:

- [Learning Material](#learning-material)
- [Resources](#resources)
- [Event Mananagement](#event-management)

# Learning material

This set includes entities used to learn / realize projects about a specific topic

## Topic (TODO)

A topic is a particular area of interest / language / development environment. Examples:

- Arduino
- Scratch
- Python
- Java

Topics are used to group learning material resources.

## Tutorial

A tutorial is a guide. In general it can:

- show how to realize a particular project 
- discuss a particular aspect of a topic (e.g. Python classes, Scratch movement blocks)

A tutorial has a title, a description, a cover image, and can have associate resource files (e.g. sprite pack, sound pack, other)

Database tables: 
- `coderdojomobile_dojoproject`
- `coderdojomobile_dojoproject_resources`

## Software

Base software used to work on a particular topic. For example, Scratch requires the Adobe Air installer and the Scratch installer.

## Level (TODO)

A learning level, e.g. beginner, intermediate, advanced. This is used to 

# Resources

Resources that can be used to build projects. Examples: sprites, sounds, software libraries

## Sprite images

Sprites are composed of an ordered list of images. 

Database tables: 
- `coderdojomobile_sprite`

## Sprite Category

Sprites are grouped into categories. A single sprite can belong to multiple categories. A category has a title, a description and a cover image

Database tables: 
- `coderdojomobile_spritecategory`
- `coderdojomobile_spritecategory_sprite`


# Event Management

This set is not implemented yet. This sections is here to discuss the possibile implementation. Its purpose is to facilitate activities such as participant check-in, badge awards, etc

## Event
Represents a single event. Note that an event is actually a specific session about a specific topic. This means that, for example, if in the same day / hour / location a Dojo holds a Scratch Session and an Arduino Session, they are two different events.

## Participant
Represents a single participant. Has a name, a surname, a type, and a unique id. Also, it has a "consent form" property (yes/no)


## Participant Type

Mentor, Ninja, etc

## Ticket

A ticket for an event, for a participant. Properties: Participant, Event, Ticket Number, status (boolean checked-in)

## Badge

A badge awarded to a Ninja. Has a title, a description, an image, (pre)requirements for award (e.g. other badges, number of presences ) 


