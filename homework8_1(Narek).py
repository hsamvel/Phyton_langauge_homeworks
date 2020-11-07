def about_books(author_name,**var):
    list_1 = [var]
    print(list_1)
    for el in list_1:
        for elem in el:
            if el[elem][0] == author_name:
                print(elem,el[elem][1])
            
        
about_books('dyuma',askanio = ('dyuma',1965),sherlock = ('conan doyle',1887),thrones=('martin george',1999))
        