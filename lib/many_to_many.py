class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        contract_list = []
        for contract in Contract.all:
            if contract.author == self:
                contract_list.append(contract)
        return contract_list
    
    def books(self):
        book_list = []
        for contract in Contract.all:
            if contract.author == self:
                book_list.append(contract.book)
        return book_list
    
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract
    
    def total_royalties(self):
        royalties_total = 0
        for contract in Contract.all:
            if contract.author == self:
                royalties_total += contract.royalties

        return royalties_total


class Book:

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        contract_list = []
        for contract in Contract.all:
            if contract.book == self:
                contract_list.append(contract)
        return contract_list
    
    def authors(self):
        author_list = []
        for contract in Contract.all:
            if contract.book == self:
                author_list.append(contract.author)
        return author_list


    

class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        if isinstance (author, Author):
            self.author = author
        else:
            raise TypeError("Author must be an instance of Author class.")
        if isinstance (book, Book):
            self.book = book
        else:
            raise TypeError("Book must be an instance of Book class.")
        if isinstance(date, str):
            self.date = date
        else: 
            raise TypeError("Date must be a string.")
        if isinstance(royalties, int):
            self.royalties = royalties
        else:
            raise TypeError("Royalties must be an integer.")
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        contract_list = []
        for contract in Contract.all:
            if contract.date == date:
                contract_list.append(contract)
        return contract_list