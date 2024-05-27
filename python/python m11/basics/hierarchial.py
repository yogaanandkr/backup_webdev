class chat:
    contacts = {'Dhoni': [], 'Kholi':[]}
    def convo(self, name):
        if name in self.contacts:
            message = ''
            while message != 'bye':
                message = input('enter => ')
                self.contacts[name] += [message]
                # end = input('end? yes or no? ')
                print(self.contacts)

class whatapp(chat):
    pass
        

chat1 = chat()
chat1.convo('Dhoni')