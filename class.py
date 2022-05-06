# # class is a great
# class Attendee:
#     'Common base class for all attendees'

#     def __init__(self, name, tickets):
#         self.name = name
#         self.tickets = tickets

#     def displayAttendee(self):
#         print('Name : {}, Tickets: {}'.format(self.name, self.tickets))

#     def addTicket(self):
#         self.tickets += 1
#         print('{} tickets increased to {}'.format(self.name, self.tickets))
# attendee1 = Attendee('g. Ahmed', 5)
# attendee2 = Attendee('J.maher', 3)

# attendee1.displayAttendee()
# attendee2.displayAttendee()
import cowsay
import sys
if len(sys.argv) == 2:
    cowsay.cow("hello," + sys.argv[1])