django-swap-field
=================

| Easy! When you use django-swap-field if the value is saved in other
  record, values are swapped! You can configure what
| conditions must be repeated in both records to make the change.

Uses e.g.
=========

-  Uniform number in sport team.
-  Race number in an athletic competition.
-  Any scenario when you want to swap values without reordering.

Available fields
================

-  SwapIntegerField

Method
======

-  Current status allow swap values if not exists
   unique/unique\_together restriction. First, get the registry (if
   exists)
   what contains the new value to assign it the old value from registry
   what currently is saving. When current registry is
   saved, replace the other registry with old value.
-  In next versions, other method will be used when exists
   unique/unique\_together restriction.

Pendings
========

-  [ ] Two or more django-swap-field in the same object.
-  [ ] Alternative method when exists unique/unique\_together
   restriction
-  [ ] Friendly validation error with Django Admin (no Fatal error)
-  [ ] Abstract django-swap-field
-  [ ] SwapCharField